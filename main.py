from fastapi import FastAPI
from config.configDatabase import Base, engine
from category.controller.categoryController import categoryRouter
from middlewares.error_handler import ErrorHandler
from user.controller.userController import userRouter
from movie.controller.movieController import movieRouter
from login.loginController import loginRouter

app = FastAPI()
app.title = 'Estudiando FastApi'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

# Incluir el controlador de categorías con su prefijo y etiquetas
app.include_router(loginRouter, prefix="/login", tags=["login"])
app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(categoryRouter, prefix="/category", tags=["category"])
app.include_router(movieRouter, prefix="/movie", tags=["movie"])


# Crear las tablas en la base de datos si es necesario
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8010)
