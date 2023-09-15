from dataclasses import dataclass
from datetime import datetime
from typing import Self

__all__ = ("Recipe",)


@dataclass
class Recipe:
    title: str
    description: str
    instructions: str
    created_at: datetime
    updated_at: datetime
    likes_count: int
    comments_count: int
    stars_count: int
    private: bool
    user_id: int
    id: int = -1

    @classmethod
    def create(
        cls,
        title: str,
        description: str,
        instructions: str,
        private: bool,
        user_id: int,
    ) -> Self:
        return cls(
            title=title,
            description=description,
            instructions=instructions,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            likes_count=0,
            comments_count=0,
            stars_count=0,
            private=private,
            user_id=user_id,
        )
