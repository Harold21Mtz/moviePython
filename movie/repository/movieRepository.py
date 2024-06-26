from starlette import status

from movie.model.movie import Movie
from movie.schema.movie import MovieRequestDto


class MovieRepository:

    def __init__(self, db):
        self.db = db

    def create_movie(self, movie: MovieRequestDto):
        movie_instance = Movie(**movie.model_dump())
        self.db.add(movie_instance)
        self.db.commit()
        return {"Message": "Movie created", "status_code": status.HTTP_201_CREATED}

    def update_movie(self, movie: Movie, updated: MovieRequestDto):
        movie.title = updated.title
        movie.overview = updated.overview
        movie.year = updated.year
        movie.rating = updated.rating
        movie.category_id = updated.category_id
        self.db.commit()
        return {"Message": "Movie updated", "status_code": status.HTTP_200_OK}

    def get_all_movies(self):
        return self.db.query(Movie).all()

    def get_movie_by_id(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.movie_id == movie_id).first()

    def get_movie_by_title(self, title: str):
        return self.db.query(Movie).filter(Movie.title == title).first()

    def get_movies_by_category(self, category_id: int):
        return self.db.query(Movie).filter(Movie.category_id == category_id).all()

    def delete_movie_by_id(self, movie: Movie):
        self.db.delete(movie)
        self.db.commit()
        return {"Message": "Movie deleted", "status_code": status.HTTP_200_OK}
