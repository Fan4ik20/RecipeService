from dataclasses import dataclass

__all__ = ("User",)

from typing import Self  # type: ignore


@dataclass
class User:
    username: str
    email: str
    password_hash: str
    id: int

    @classmethod
    def create(
        cls,
        username: str,
        email: str,
        password_hash: str,
        id_: int | None = None,
    ) -> Self:
        return cls(
            username=username,
            email=email,
            password_hash=password_hash,
            id=id_ or -1,
        )

    def update(
        self,
        username: str | None = None,
        email: str | None = None,
        password_hash: str | None = None,
    ) -> None:
        if email:
            self.email = email
        if username:
            self.username = username
        if password_hash:
            self.password_hash = password_hash
