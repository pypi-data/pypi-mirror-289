import json
import logging
from pprint import pp

import redis.asyncio as redis

from proxy_messages_aiogram.storages.base import BaseTopicStorage

logger = logging.getLogger('app')


class RedisTopicStorage(BaseTopicStorage):
    def __init__(self, *args, **kwargs) -> None:
        self.client = redis.Redis(*args, **kwargs)

    async def on_startup(self):
        # await self.client.flushall()
        logger.debug('Testing connection to redis')
        keys = await self.client.keys()
        logger.debug(f'Redis is connected. Keys len: {len(keys)}')
        pp(await self.client.hgetall('topic_hash_to_id'))

    async def set_topic_id(self, target_chat_topic_hash: str, target_chat_topic_id: int):
        await self.client.hset('topic_hash_to_id', target_chat_topic_hash, target_chat_topic_id)

    async def get_topic_id(self, target_chat_topic_hash: str) -> int | None:
        topic_id = await self.client.hget('topic_hash_to_id', target_chat_topic_hash)

        if topic_id is None:
            return None

        return int(topic_id)

    async def set_chat_id(
        self,
        target_chat_topic_id: str,
        original_chat_id: int,
        original_chat_topic_id: int,
    ):
        data = [original_chat_id, original_chat_topic_id]
        await self.client.hset('topic_id_to_original_ids', target_chat_topic_id, json.dumps(data))

    async def get_chat_id(self, target_chat_topic_id: str) -> tuple[int, int]:
        data_json = await self.client.hget('topic_id_to_original_ids', target_chat_topic_id)
        return tuple(json.loads(data_json))
