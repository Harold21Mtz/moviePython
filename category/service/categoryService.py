from fastapi import HTTPException, status, Depends
from fastapi.responses import JSONResponse

from category.model.category import Category
from category.schema.CategoryDto import CategoryRequestDto, CategoryResponseDto
from category.repository.categoryRepository import CategoryRepository
from sqlalchemy.orm import Session


class CategoryService:

    def create_category(self, db: Session, new_category: CategoryRequestDto) -> dict:
        self.get_category_by_name(db, new_category.category_name)
        return CategoryRepository(db).create_category(new_category)

    def get_all_categories(self, db: Session) -> dict:
        categories = CategoryRepository(db).get_all_categories()
        categories_responses = []

        for category in categories:
            category_response = CategoryResponseDto(
                category_id=category.category_id,
                category_name=category.category_name,
                category_description=category.category_description,
            )
            categories_responses.append(category_response.model_dump())
        return {"message": "All categories", "data": categories_responses}

    def get_category_by_id(self, db: Session, category_id: int) -> dict:
        category = self.get_category(db, category_id)

        category_response = CategoryResponseDto(
            category_id=category.category_id,
            category_name=category.category_name,
            category_description=category.category_description,
        )
        return category_response.model_dump()

    @staticmethod
    def get_category_by_name(db: Session, category_name: str) -> dict:
        existing_category = CategoryRepository(db).get_category_by_name(category_name)
        if existing_category:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category already exists")

    def update_category(self, db: Session, category_id: int, update_category: CategoryRequestDto) -> dict:
        category = self.get_category(db, category_id)
        return CategoryRepository(db).update_category(update_category, category)

    def delete_category(self, db: Session, category_id: int) -> dict:
        category = self.get_category(db, category_id)
        return CategoryRepository(db).delete_category(category)

    @staticmethod
    def get_category(db: Session, category_id: int) -> Category:
        category = CategoryRepository(db).get_category_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category
