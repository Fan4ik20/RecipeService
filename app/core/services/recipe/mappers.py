from core.domain import entities
from core.services.recipe import dto

__all__ = (
    "map_dto_to_domain",
    "map_domain_to_model",
)


def map_dto_to_domain(recipe: dto.RecipeCreate) -> entities.Recipe:
    return entities.Recipe.create(
        title=recipe.title,
        description=recipe.description,
        instructions=recipe.instructions,
        private=recipe.private,
        user_id=recipe.user_id,
    )


def map_domain_to_model(recipe: entities.Recipe) -> dto.RecipeModel:
    recipe_dto = dto.Recipe(
        title=recipe.title,
        description=recipe.description,
        instructions=recipe.instructions,
        updated_at=recipe.updated_at,
        likes_count=recipe.likes_count,
        comments_count=recipe.comments_count,
        stars_count=recipe.stars_count,
        private=recipe.private,
        user_id=recipe.user_id,
    )

    return dto.RecipeModel(id=recipe.id, recipe=recipe_dto)
