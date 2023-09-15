from typing import Any

__all__ = ("RecipeNotFound",)


class RecipeNotFound(Exception):
    def __init__(self, attr: str, value: Any) -> None:
        self.attr = attr
        self.value = value

        super().__init__(
            f"recipe with given {self.attr}: {self.value} not found"
        )
