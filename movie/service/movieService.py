from fastapi import HTTPException
from sqlalchemy.orm import Session

from movie.model.movie import Movie
from movie.repository.movieRepository import MovieRepository
from movie.schema.movie import MovieResponseDto, MovieRequestDto
from category.service.categoryService import CategoryService


class MovieService:

    def get_movie(self, db: Session, movie_id: int) -> Movie:
        movie = MovieRepository(db).get_movie_by_id(movie_id)

        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        return movie

    def get_all_movies(self, db: Session) -> dict:
        movies = MovieRepository(db).get_all_movies()
        movies_response = []

        for movie in movies:
            category_name = movie.category.category_name if movie.category else None
            movie_response = MovieResponseDto(
                movie_id=movie.movie_id,
                title=movie.title,
                overview=movie.overview,
                year=movie.year,
                rating=movie.rating,
                category_id=movie.category_id,
                category_name=category_name,
            )
            movies_response.append(movie_response.model_dump())
        return {"Message": "All movies", "data": movies_response}

    def get_movie_by_id(self, db: Session, movie_id: int) -> dict:
        movie = self.get_movie(db, movie_id)

        category_name = movie.category.category_name if movie.category else None
        movie_response = MovieResponseDto(
            movie_id=movie.movie_id,
            title=movie.title,
            overview=movie.overview,
            year=movie.year,
            rating=movie.rating,
            category_id=movie.category_id,
            category_name=category_name
        )
        return {"Message": "Category by id", "data": movie_response.model_dump()}

    def get_all_movies_by_category(self, db: Session, category_id: int) -> dict:
        CategoryService.get_category(db, category_id)
        movies = MovieRepository(db).get_movies_by_category(category_id)
        return {"Message": "All movies by category", "data": movies}

    def create_movie(self, db: Session, movie: MovieRequestDto) -> dict:
        return MovieRepository(db).create_movie(movie)

    def update_movie(self, db: Session, movie_id: int, movie_update: MovieRequestDto) -> dict:
        movie = self.get_movie(db, movie_id)
        return MovieRepository(db).update_movie(movie, movie_update)

    def delete_movie(self, db: Session, movie_id: int) -> dict:
        movie = self.get_movie(db, movie_id)
        return MovieRepository(db).delete_movie_by_id(movie)
