from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core.domain import entities
from core.services.user import UserNotFound, UserRepository
from infrastructure.database import models

from . import mappers

__all__ = ("UserRepoAlchemy",)


class UserRepoAlchemy(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id_: int) -> entities.User:
        user = await self._session.get(models.User, id_)

        if user is None:
            raise UserNotFound("id", id_)

        return mappers.map_model_to_domain(user)

    async def get_by_email(self, email: str) -> entities.User:
        user: models.User = await self._session.scalar(
            select(models.User).filter_by(email=email)
        )

        if user is None:
            raise UserNotFound("email", email)

        return mappers.map_model_to_domain(user)

    async def get_by_username(self, username: str) -> entities.User:
        user: models.User = await self._session.scalar(
            select(models.User).filter_by(username=username)
        )

        if user is None:
            raise UserNotFound("email", username)

        return mappers.map_model_to_domain(user)

    async def create(self, user: entities.User) -> entities.User:
        user = mappers.map_domain_to_model(user)

        self._session.add(user)

        await self._session.flush()

        return mappers.map_model_to_domain(user)

    async def update(self, user: entities.User) -> entities.User:
        user = mappers.map_domain_to_model(user)

        self._session.add(user)

        await self._session.commit()

        return mappers.map_model_to_domain(user)

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except SQLAlchemyError:
            await self._session.rollback()
