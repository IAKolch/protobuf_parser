from typing import TypeVar, Type

from protobuf_parser.helpers import parseDelimited

T = TypeVar('T')


class DelimitedMessagesStreamParser:
    def __init__(self, cls: Type[T]) -> None:
        self.cls = cls
        self.buffer = bytearray()

    def parse(self, data: bytes) -> list[Type[T]]:
        if data:
            self.buffer.extend(data)

        messages = []

        while len(self.buffer) > 0:
            message, size = parseDelimited(self.buffer, self.cls)
            if not message:
                break
            messages.append(message)
            del self.buffer[:size]

        return messages
