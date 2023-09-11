from core.domain import entities
from core.services.user import dto

__all__ = (
    "map_dto_to_domain",
    "map_domain_to_model",
)


def map_dto_to_domain(user: dto.UserCreate) -> entities.User:
    return entities.User.create(
        username=user.username,
        email=user.username,
        password_hash=user.password,
    )


def map_domain_to_model(user: entities.User) -> dto.UserModel:
    user_dto = dto.User(username=user.username, email=user.email)

    return dto.UserModel(id=user.id, user=user_dto)
