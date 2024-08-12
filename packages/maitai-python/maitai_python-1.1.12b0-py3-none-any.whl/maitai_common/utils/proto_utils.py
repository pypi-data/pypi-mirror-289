from typing import Iterable

from openai.types.chat import ChatCompletionMessageParam

from maitai_gen.chat import ChatMessage


def openai_messages_to_proto(messages: Iterable[ChatCompletionMessageParam]):
    proto_messages: [ChatMessage] = []
    for message in messages:
        proto_messages.append(
            ChatMessage().from_pydict(message)
        )
    return proto_messages
