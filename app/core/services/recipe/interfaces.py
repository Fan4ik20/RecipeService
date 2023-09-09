from typing import Protocol

from core.domain import entities

__all__ = "RecipeRepository"


class RecipeRepository(Protocol):
    async def get_by_id(self, id_: int) -> entities.Recipe:
        raise NotImplementedError

    async def get_by_title(self, title: str) -> entities.Recipe:
        raise NotImplementedError

    async def get_by_user_id(self, user_id: int) -> entities.Recipe:
        raise NotImplementedError

    async def create(self, recipe: entities.Recipe) -> entities.Recipe:
        raise NotImplementedError

    async def update(self, user: entities.Recipe) -> entities.Recipe:
        raise NotImplementedError
