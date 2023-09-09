from core.domain import entities
from core.services.recipe import dto, mappers
from core.services.recipe.interfaces import RecipeRepository

__all__ = ("RecipeService",)


class RecipeService:
    def __init__(
        self,
        repo: RecipeRepository,
    ) -> None:
        self._repo = repo

    async def create_recipe(self, recipe: dto.RecipeCreate) -> dto.RecipeModel:
        domain = await self._repo.create(mappers.map_dto_to_domain(recipe))
        return mappers.map_domain_to_model(domain)

    async def get_recipe(
        self,
        id_: int | None = None,
        title: str | None = None,
        user_id: int | None = None,
    ) -> dto.RecipeModel:
        if id_:
            recipe = await self._repo.get_by_id(id_)
        elif title:
            recipe = await self._repo.get_by_title(title)
        elif user_id:
            recipe = await self._repo.get_by_user_id(user_id)
        else:
            raise ValueError("You need to provide at least 1 argument")

        return mappers.map_domain_to_model(recipe)

    def _update_domain(
        self, recipe_domain: entities.Recipe, recipe_dto: dto.RecipeUpdate
    ) -> None:
        if recipe_dto.title:
            recipe_domain.title = recipe_dto.title
        if recipe_dto.description:
            recipe_domain.description = recipe_dto.description
        if recipe_dto.instructions:
            recipe_domain.instructions = recipe_dto.instructions
        if recipe_dto.private:
            recipe_domain.private = recipe_dto.private

    async def update_recipe(
        self, id_: int, recipe: dto.RecipeUpdate
    ) -> dto.RecipeModel:
        domain = await self._repo.get_by_id(id_)

        self._update_domain(domain, recipe)

        return mappers.map_domain_to_model(await self._repo.update(domain))
