import logging
from pprint import pp

try:
    import redis.asyncio as redis

except ImportError:
    raise ImportError('To use redis storage you need to install redis: `pip install redis`')


from proxy_messages_aiogram.storages import types
from proxy_messages_aiogram.storages.base import BaseStorage

logger = logging.getLogger('app')


class RedisStorage(BaseStorage):
    def __init__(self, *args, **kwargs) -> None:
        self.client = redis.Redis(*args, **kwargs)
        pp(self.client)

    async def on_startup(self):
        logger.debug('Testing connection to redis')
        keys = await self.client.keys()
        logger.debug(f'Redis is connected. Keys len: {len(keys)}')
        pp(await self.client.keys())
        pp(await self.client.hgetall('topic_hash_to_id'))

    async def set_proxy_message_info(
        self,
        bot_id: int,
        proxy_message_info: types.ProxyMessageInfo,
    ):
        await self.client.hset(
            f'proxy_message_info__by__original_chat_hash:{bot_id}',
            proxy_message_info.original_chat_hash,
            proxy_message_info.json(),
        )
        await self.client.hset(
            f'proxy_message_info__by__target_chat_topic_id:{bot_id}',
            proxy_message_info.target_chat_topic_id,
            proxy_message_info.json(),
        )

    async def get_proxy_message_info__by__original_chat_hash(
        self,
        bot_id: int,
        original_chat_hash: str,
    ) -> types.ProxyMessageInfo | None:
        proxy_message_info_json = await self.client.hget(
            f'proxy_message_info__by__original_chat_hash:{bot_id}',
            original_chat_hash,
        )

        if proxy_message_info_json is None:
            return None

        return types.ProxyMessageInfo.model_validate_json(proxy_message_info_json)

    async def get_proxy_message_info__by__target_chat_topic_id(
        self,
        bot_id: int,
        target_chat_topic_id: int,
    ) -> types.ProxyMessageInfo | None:
        proxy_message_info_json = await self.client.hget(
            f'proxy_message_info__by__target_chat_topic_id:{bot_id}',
            target_chat_topic_id,
        )

        if proxy_message_info_json is None:
            return None

        return types.ProxyMessageInfo.model_validate_json(proxy_message_info_json)
