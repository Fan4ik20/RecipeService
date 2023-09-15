from dataclasses import dataclass
from datetime import datetime

__all__ = (
    "Recipe",
    "RecipeModel",
    "RecipeCreate",
    "RecipeUpdate",
)


@dataclass
class RecipeCreate:
    title: str
    private: bool
    user_id: int
    description: str
    instructions: str


@dataclass
class RecipeUpdate:
    title: str | None = None
    description: str | None = None
    instructions: str | None = None
    private: bool | None = None


@dataclass
class Recipe:
    title: str
    description: str
    instructions: str
    updated_at: datetime
    likes_count: int
    comments_count: int
    stars_count: int
    private: bool
    user_id: int


@dataclass
class RecipeModel:
    id: int
    recipe: Recipe
