from dataclasses import dataclass

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

__all__ = (
    "DBConfig",
    "create_engine",
    "create_sessionmaker",
    "build_async_db_url",
)


@dataclass(frozen=True)
class DBConfig:
    username: str
    password: str
    endpoint: str
    db_name: str


def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(build_async_db_url(db_config))


def create_sessionmaker(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(bind=engine)


def build_async_db_url(config: DBConfig) -> str:
    return f"postgresql+asyncpg://{config.username}:{config.password}@{config.endpoint}/{config.db_name}"  # noqa
