from typing import Any

__all__ = (
    "UserNotFound",
    "UserAlreadyExists",
)


class UserAlreadyExists(Exception):
    def __init__(self, attr: str, value: Any) -> None:
        self.attr = attr
        self.value = value

        super().__init__(
            f"user with given {self.attr}: {self.value} already exist"
        )


class UserNotFound(Exception):
    def __init__(self, attr: str, value: Any) -> None:
        self.attr = attr
        self.value = value

        super().__init__(
            f"user with given {self.attr}: {self.value} not found"
        )
