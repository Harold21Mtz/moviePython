from fastapi import APIRouter, Path, Depends
from sqlalchemy.orm import Session

from middlewares.bearer import JWTBearer
from category.service.categoryService import CategoryService
from category.schema.CategoryDto import CategoryRequestDto, CategoryResponseDto
from config.configDatabase import get_db

categoryRouter = APIRouter()


@categoryRouter.post("/", response_model=dict, dependencies=[Depends(JWTBearer())])
def createCategory(new_category: CategoryRequestDto, category_service: CategoryService = Depends(),
                   session: Session = Depends(get_db)) -> dict:
    response = category_service.create_category(session, new_category)
    return response


@categoryRouter.get("/all", response_model=dict, dependencies=[Depends(JWTBearer())])
def get_all_categories(category_service: CategoryService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = category_service.get_all_categories(session)
    return response


@categoryRouter.get("/{category_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
def get_category_by_id(category_id: int, category_service: CategoryService = Depends(),
                       session: Session = Depends(get_db)) -> dict:
    response = category_service.get_category_by_id(session, category_id)
    return response


@categoryRouter.put("/{category_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
def createCategory(category_id: int, update_category: CategoryRequestDto, category_service: CategoryService = Depends(),
                   session: Session = Depends(get_db)) -> dict:
    response = category_service.update_category(session, category_id, update_category)
    return response


@categoryRouter.delete("/{category_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_category(category_id: int, category_service: CategoryService = Depends(),
                    session: Session = Depends(get_db)) -> dict:
    response = category_service.delete_category(session, category_id)
    return response
