from core.domain import entities
from infrastructure.database import models

__all__ = (
    "map_model_to_domain",
    "map_domain_to_model",
)


def map_model_to_domain(user: models.User) -> entities.User:
    return entities.User.create(
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,
        id_=user.id,
    )


def map_domain_to_model(user: entities.User) -> models.User:
    return models.User(
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,
    )
