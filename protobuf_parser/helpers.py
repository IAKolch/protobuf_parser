from typing import TypeVar, Any, Type

from google.protobuf.internal.decoder import _DecodeVarint32

T = TypeVar('T')


def parseDelimited(data: Any, cls: Type[T]) -> tuple[Type[T], int]:
    """
    \brief Расшифровывает сообщение,
    предваренное длиной из массива байтов.

    \param data Массив данных.
    \param cls Тип сообщения.

    \return Возвращает кортеж из
    расшифрованного сообщения и количество байт,
    которое потребовалось для расшифровки.
    """
    if not data:
        return None, 0

    try:
        message_size, pos = _DecodeVarint32(data, 0)
    except (IndexError, TypeError) as e:
        raise ValueError(f"Не удалось декодировать размер сообщения: {e}")

    total_size = pos + message_size

    if total_size > len(data):
        return None, 0

    message_data = data[pos:total_size]

    try:
        message = cls()
        message.ParseFromString(message_data)
    except Exception as e:
        raise ValueError(f"Ошибка парсинга сообщения: {e}")
    

    return message, total_size
