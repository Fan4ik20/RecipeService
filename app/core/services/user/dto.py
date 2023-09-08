from dataclasses import dataclass

__all__ = (
    "User",
    "UserModel",
    "UserCreate",
    "UserUpdate",
)


@dataclass
class UserCreate:
    username: str
    email: str
    password: str


@dataclass
class UserUpdate:
    username: str | None = None
    email: str | None = None
    password: str | None = None


@dataclass
class User:
    username: str
    email: str


@dataclass
class UserModel:
    id: int
    user: User
