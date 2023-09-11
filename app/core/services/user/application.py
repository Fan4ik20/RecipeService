from core.services.user import dto, exc, mappers
from core.services.user.interfaces import HashManager, UserRepository

__all__ = ("UserService",)


class UserService:
    def __init__(
        self, repo: UserRepository, hash_manager: HashManager
    ) -> None:
        self._repo = repo
        self._hash_manager = hash_manager

    async def create_user(self, user: dto.UserCreate) -> dto.UserModel:
        if await self._repo.get_by_email(user.email) is not None:
            raise exc.UserAlreadyExists("email", user.email)
        if await self._repo.get_by_username(user.username) is not None:
            raise exc.UserAlreadyExists("username", user.username)

        user.password = self._hash_manager.hash_password(user.password)
        domain = await self._repo.create(mappers.map_dto_to_domain(user))

        await self._repo.commit()

        return mappers.map_domain_to_model(domain)

    async def get_user(
        self,
        id_: int | None = None,
        username: str | None = None,
        email: str | None = None,
    ) -> dto.UserModel:
        if id_:
            user = await self._repo.get_by_id(id_)
        elif username:
            user = await self._repo.get_by_username(username)
        elif email:
            user = await self._repo.get_by_email(email)
        else:
            raise ValueError("You need to provide at least 1 argument")

        return mappers.map_domain_to_model(user)

    async def update_user(
        self, id_: int, user: dto.UserUpdate
    ) -> dto.UserModel:
        domain = await self._repo.get_by_id(id_)

        domain.update(
            username=user.username,
            email=user.email,
            password_hash=self._hash_password(user.password),
        )

        user_model = mappers.map_domain_to_model(
            await self._repo.update(domain)
        )
        await self._repo.commit()

        return user_model

    def _hash_password(self, psw: str | None) -> str | None:
        p = self._hash_manager.hash_password(psw) if psw is not None else None
        return p
