import logging
from pprint import pp

from aiogram import F, MagicFilter
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message

from proxy_messages_aiogram import texts
from proxy_messages_aiogram.storages import types
from proxy_messages_aiogram.storages.base import BaseStorage

logger = logging.getLogger('app')


class ProxyMessagesManager(object):
    def __init__(self, storage: BaseStorage, target_chat_id: int, message: Message) -> None:
        self.storage = storage
        self.target_chat_id = target_chat_id
        self.message = message
        self.bot = message.bot

        assert self.bot is not None

    @property
    def topic_name(self):
        if self.message.message_thread_id is not None:
            return f'{self.message.chat.full_name} -> {self.message.message_thread_id} [by {self.bot._me.username}]'

        return f'{self.message.chat.full_name} [by {self.bot._me.username}]'

    async def send_chat_info_message(self, target_chat_topic_id: int):
        text_data = {
            'original_user_id': self.message.from_user.id,
            'original_user_username': self.message.from_user.username,
            'original_user_name': self.message.from_user.full_name,
            'original_chat_id': self.message.chat.id,
            'original_chat_username': self.message.chat.username,
            'original_chat_name': self.message.chat.full_name,
            'original_chat_is_group': self.message.chat.id != self.message.from_user.id,
            'original_chat_is_forum': bool(self.message.chat.is_forum),
            'original_chat_topic_id': self.message.message_thread_id,
            'bot_id': self.bot.id,
            'bot_username': self.bot._me.username,
            'bot_name': self.bot._me.full_name,
            'chat_topic_id': target_chat_topic_id,
            'chat_topic_name': self.topic_name,
        }

        text = texts.NEW_TOPIC_INFO_1.format(**text_data)

        message = await self.bot.send_message(
            self.target_chat_id,
            text,
            message_thread_id=target_chat_topic_id,
            parse_mode=ParseMode.HTML,
        )
        await self.bot.pin_chat_message(self.target_chat_id, message.message_id, False)

    async def create_new_topic(self):
        target_chat_topic = await self.bot.create_forum_topic(self.target_chat_id, self.topic_name)
        target_chat_topic_id = target_chat_topic.message_thread_id
        await self.send_chat_info_message(target_chat_topic_id)

        return target_chat_topic_id

    async def proxy(self):
        proxy_message_info = await self.storage.get_proxy_message_info__by__original_chat_hash(
            self.bot.id,
            types.ProxyMessageInfo.cls_original_chat_hash(self.message),
        )

        if proxy_message_info is None:
            proxy_message_info = types.ProxyMessageInfo.from_message(self.message, self.target_chat_id)

            proxy_message_info.target_chat_topic_id = await self.create_new_topic()

            await self.storage.set_proxy_message_info(self.bot.id, proxy_message_info)

        await self.message.copy_to(self.target_chat_id, proxy_message_info.target_chat_topic_id)


class AnswerMessagesManager(object):
    def __init__(self, storage: BaseStorage, target_chat_id: int, message: Message) -> None:
        self.storage = storage
        self.target_chat_id = target_chat_id
        self.message = message
        self.bot = message.bot

        assert self.bot is not None

    async def proxy(self):
        assert self.message.message_thread_id is not None

        proxy_message_info = await self.storage.get_proxy_message_info__by__target_chat_topic_id(
            self.bot.id,
            self.message.message_thread_id,
        )

        if proxy_message_info is None:
            await self.message.reply(
                'We can`t find original chat for [{} / {} / {}]'.format(
                    self.bot.id,
                    self.message.message_id,
                    self.message.message_thread_id,
                )
            )
            return

        try:
            await self.message.copy_to(
                proxy_message_info.original_chat_id,
                proxy_message_info.original_chat_topic_id,
            )

        except BaseException as ex:
            logger.exception(ex)
            await self.message.reply(f'We can`t proxy this message [{self.message.message_id}]; Error: {ex}')
            return


class ProxyManager(object):
    PROXY_MESSAGES_MANAGER_TYPE: type[ProxyMessagesManager] = ProxyMessagesManager
    ANSWER_MESSAGES_MANAGER_TYPE: type[AnswerMessagesManager] = AnswerMessagesManager

    def __init__(self, storage: BaseStorage, target_chat_id: int) -> None:
        self.storage = storage
        self.target_chat_id = target_chat_id

    async def on_startup(self):
        await self.storage.on_startup()

    async def on_shutdown(self):
        await self.storage.on_shutdown()

    @property
    def proxy_magic_filter(self) -> MagicFilter:
        return F.chat.id != self.target_chat_id

    @property
    def answer_magic_filter(self) -> MagicFilter:
        return (F.chat.id == self.target_chat_id) & (F.from_user.is_bot == False) & F.message_thread_id

    async def proxy(self, message: Message):
        proxy_messages_manager = self.PROXY_MESSAGES_MANAGER_TYPE(self.storage, self.target_chat_id, message)
        await proxy_messages_manager.proxy()

    async def answer(self, message: Message):
        proxy_messages_manager = self.ANSWER_MESSAGES_MANAGER_TYPE(self.storage, self.target_chat_id, message)
        await proxy_messages_manager.proxy()
