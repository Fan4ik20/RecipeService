from dataclasses import dataclass

__all__ = ("User",)


@dataclass
class User:
    username: str
    email: str
    password_hash: str
    id: int = -1
