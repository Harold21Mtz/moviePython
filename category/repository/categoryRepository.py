from fastapi import status
from category.schema.CategoryDto import CategoryRequestDto
from category.model.category import Category


class CategoryRepository:

    def __init__(self, db) -> None:
        self.db = db

    def create_category(self, category_dto: CategoryRequestDto):
        instance_category = Category(**category_dto.model_dump())
        self.db.add(instance_category)
        self.db.commit()
        return {"Message": "Category added successfully", "status_code": status.HTTP_201_CREATED}

    def get_category_by_id(self, category_id) -> Category:
        return self.db.query(Category).filter(Category.category_id == category_id).first()

    def get_category_by_name(self, category_name):
        return self.db.query(Category).filter(Category.category_name == category_name).first()

    def get_all_categories(self):
        return self.db.query(Category).all()

    def update_category(self, update_category: CategoryRequestDto, category: Category):
        category.category_name = update_category.category_name
        category.category_description = update_category.category_description
        self.db.commit()
        return {"Message": "Category updated successfully", "status_code": status.HTTP_200_OK}

    def delete_category(self, category: Category):
        self.db.delete(category)
        self.db.commit()
        return {"Message": "Category successfully deleted", "status_code": status.HTTP_200_OK}
