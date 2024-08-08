import abc


class BaseTopicStorage(abc.ABC):
    def __init__(self) -> None:
        pass

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    @abc.abstractmethod
    async def set_topic_id(self, target_chat_topic_hash: str, target_chat_topic_id: int):
        pass

    @abc.abstractmethod
    async def get_topic_id(self, target_chat_topic_hash: str) -> int | None:
        pass

    @abc.abstractmethod
    async def set_chat_id(self, target_chat_topic_id: str, original_chat_id: int, original_chat_topic_id: int):
        pass

    @abc.abstractmethod
    async def get_chat_id(self, target_chat_topic_id: str) -> tuple[int, int]:
        pass
