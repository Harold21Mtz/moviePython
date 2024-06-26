from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.configDatabase import get_db
from movie.service.movieService import MovieService
from movie.schema.movie import MovieRequestDto

movieRouter = APIRouter()


@movieRouter.get("/", response_model=dict)
def get_all_movies(movie_service: MovieService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = movie_service.get_all_movies(session)
    return response


@movieRouter.get("/{movie_id}", response_model=dict)
def get_movie_by_id(movie_id: int, movie_service: MovieService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = movie_service.get_movie_by_id(session, movie_id)
    return response


@movieRouter.get("/category/{movie_id}", response_model=dict)
def get_movie_by_category(movie_id: int, movie_service: MovieService = Depends(),
                          session: Session = Depends(get_db)) -> dict:
    response = movie_service.get_all_movies_by_category(session, movie_id)
    return response

@movieRouter.post("/", response_model=dict)
def create_movie(movie: MovieRequestDto, movie_service: MovieService = Depends(),
                 session: Session = Depends(get_db)) -> dict:
    response = movie_service.create_movie(session, movie)
    return response


@movieRouter.put("/{movie_id}", response_model=dict)
def update_movie(movie_id: int, movie_update: MovieRequestDto, movie_service: MovieService = Depends(),
                 session: Session = Depends(get_db)) -> dict:
    response = movie_service.update_movie(session, movie_id, movie_update)
    return response


@movieRouter.delete("/{movie_id}", response_model=dict)
def delete_movie(movie_id: int, movie_service: MovieService = Depends(), session: Session = Depends(get_db)) -> dict:
    response = movie_service.delete_movie(session, movie_id)
    return response
