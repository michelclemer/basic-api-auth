from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response

from src.crud.schemas.user.user_schema import (FindUser, UserCreate,
                                               UserResponse)
from src.infra.auth.security import JWTBearer
from src.infra.container import Container
from src.services.user.user_services import UserService

router = APIRouter()


@router.get("/users/", dependencies=[Depends(JWTBearer())])
@inject
def get_users(
        find_query: FindUser = Depends(),
        user_service: UserService = Depends(Provide[Container.user_services]),
):
    return user_service.get_list(find_query)


@router.get("/users/detail/{user_id}")
@inject
def get_user_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_services])
):
    return user_service.get_by_id(user_id)

@router.post("/users/create/", response_model=UserResponse)
@inject
def create_user(
        user: UserCreate,
        user_service: UserService = Depends(Provide[Container.user_services])
):
    return user_service.create_user(user.dict())


@router.delete("/users/delete/{user_id}")
@inject
def delete_user(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_services])
):
    user_service.remove_by_id(user_id)
    return Response(status_code=204, content="User deleted")


@router.get("/roles/")
@inject
def get_roles(
        user_service: UserService = Depends(Provide[Container.user_services])
):
    return user_service.get_all_roles()


@router.post("/admin", dependencies=[Depends(JWTBearer())])
@inject
def get_admin(
        find_query: FindUser = Depends(),
        user_service: UserService = Depends(Provide[Container.user_services]),
):
    return user_service.get_list(find_query)
