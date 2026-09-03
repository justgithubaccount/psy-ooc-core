"""Зависимости API: хранилище экземпляров TheSelf.

Реестр держит психики в памяти процесса и раздаёт их по ключу сессии.
Состояние живёт до рестарта — персистентности здесь намеренно нет.
"""

from fastapi import Header

from ooc.core.the_self import TheSelf

DEFAULT_SESSION = "default"

_registry: dict[str, TheSelf] = {}


def get_self(
    x_session_id: str = Header(
        default=DEFAULT_SESSION,
        description="Ключ сессии: разные значения — независимые психики.",
    ),
) -> TheSelf:
    """Вернуть TheSelf этой сессии, создав его при первом обращении."""
    if x_session_id not in _registry:
        _registry[x_session_id] = TheSelf()
    return _registry[x_session_id]


def reset_self(session_id: str = DEFAULT_SESSION) -> None:
    """Сбросить психику сессии в начальное состояние."""
    _registry.pop(session_id, None)


def reset_all() -> None:
    """Очистить реестр целиком. Используется тестами."""
    _registry.clear()
