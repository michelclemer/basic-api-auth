from dependency_injector import containers, providers

from src.crud.repository.user_repository import (UserProfileRepository,
                                                 UserRepository)
from src.infra.database import Database
from src.infra.settings import settings
from src.services.user.auth_service import AuthService
from src.services.user.user_services import ProfileService, UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src"])
    config = providers.Configuration()
    print(str(settings.SQLALCHEMY_DATABASE_URI))
    db = providers.Singleton(Database, db_url=str(settings.SQLALCHEMY_DATABASE_URI))

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    profile_repository = providers.Factory(UserProfileRepository, session_factory=db.provided.session)

    user_services = providers.Factory(UserService, user_repository=user_repository)
    auth_services = providers.Factory(AuthService, user_repository=user_repository)
    profile_services = providers.Factory(ProfileService, profile_repository=profile_repository)