from typing import Protocol

from core.domain import entities

__all__ = ("UserRepository", "HashManager")


class UserRepository(Protocol):
    async def get_by_id(self, id_: int) -> entities.User:
        raise NotImplementedError

    async def get_by_email(self, email: str) -> entities.User:
        raise NotImplementedError

    async def get_by_username(self, username: str) -> entities.User:
        raise NotImplementedError

    async def create(self, user: entities.User) -> entities.User:
        raise NotImplementedError

    async def update(self, user: entities.User) -> entities.User:
        raise NotImplementedError


class HashManager(Protocol):
    def hash_password(self, psw: str) -> str:
        raise NotImplementedError

    def verify_password(self, psw: str, hashed_psw: str) -> bool:
        raise NotImplementedError
