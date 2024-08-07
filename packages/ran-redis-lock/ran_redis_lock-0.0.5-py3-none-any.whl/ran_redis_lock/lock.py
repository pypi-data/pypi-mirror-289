# lock.py
import asyncio
from contextlib import asynccontextmanager
import aioredis


class RedisDistributedLock:
    def __init__(self, key: str, redis_client: aioredis.Redis, timeout: int = 10, lock_timeout: int = 5):
        """
        初始化分布式锁。

        :param key: 锁的键名。
        :param redis_client: 已经建立好的 Redis 客户端实例。
        :param timeout: 获取锁的超时时间（秒）。
        :param lock_timeout: 锁的有效时间（秒）。
        """
        self.key = key
        self.redis_client = redis_client
        self.timeout = timeout
        self.lock_timeout = lock_timeout
        self.locked = False
        self.lock_value = None

        # 定义 Lua 脚本
        self.lua_scripts = {
            'acquire': '''
                local lock_key = KEYS[1]
                local lock_value = ARGV[1]
                local lock_timeout = tonumber(ARGV[2])

                if redis.call("setnx", lock_key, lock_value) == 1 then
                    -- Lock acquired, set expiration
                    redis.call("pexpire", lock_key, lock_timeout)
                    return 1
                else
                    -- Lock already exists, check if it's owned by the same client
                    local existing_value = redis.call("get", lock_key)
                    if existing_value == lock_value then
                        -- Extend the lock's expiration
                        redis.call("pexpire", lock_key, lock_timeout)
                        return 1
                    end
                    return 0
                end
            ''',
            'release': '''
                local lock_key = KEYS[1]
                local lock_value = ARGV[1]

                local current_value = redis.call("get", lock_key)
                if current_value == lock_value then
                    -- Lock is owned by the same client, release it
                    redis.call("del", lock_key)
                    return 1
                else
                    -- Lock is not owned by the same client, do nothing
                    return 0
                end
            '''
        }

    async def _load_script(self, script_name: str) -> str:
        """
        加载 Lua 脚本。

        :param script_name: 脚本名称。
        :return: 返回脚本的 SHA1 哈希值。
        """
        lua_script = self.lua_scripts[script_name]
        sha1_hash = await self.redis_client.script_load(lua_script)
        return sha1_hash

    async def acquire(self) -> bool:
        """
        尝试获取锁。

        :return: 如果成功获取锁，则返回 True；否则返回 False。
        """
        sha1_hash = await self._load_script('acquire')
        lock_value = f"{self.key}-{id(self)}"
        acquired = await self.redis_client.evalsha(sha1_hash, keys=[self.key],
                                                   args=[lock_value, self.lock_timeout * 1000])
        if acquired:
            self.locked = True
            self.lock_value = lock_value
            return True
        return False

    async def release(self) -> bool:
        """
        释放锁。

        :return: 如果成功释放锁，则返回 True；否则返回 False。
        """
        if not self.locked:
            return False

        sha1_hash = await self._load_script('release')
        released = await self.redis_client.evalsha(sha1_hash, keys=[self.key], args=[self.lock_value])
        if released:
            self.locked = False
            self.lock_value = None
            return True
        return False

    async def __aenter__(self) -> 'RedisDistributedLock':
        """
        异步上下文管理器的进入阶段。
        """
        start_time = asyncio.get_running_loop().time()
        while asyncio.get_running_loop().time() - start_time < self.timeout:
            if await self.acquire():
                return self
            await asyncio.sleep(0.1)
        raise TimeoutError(f"Failed to acquire lock for key {self.key} within {self.timeout} seconds.")

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        异步上下文管理器的退出阶段。
        """
        await self.release()