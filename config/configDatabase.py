import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# user = os.getenv("DB_USER", "agro-web_owner")
# password = os.getenv("DB_PASSWORD", "e7Dv9tYfojmp")
# host = os.getenv("DB_HOST", "ep-cool-salad-a4dovsne.us-east-1.aws.neon.tech")
# port = os.getenv("DB_PORT", "5432")
# database = os.getenv("DB_NAME", "fastApi")

user = os.getenv("DB_USER", "postgres")
password = os.getenv("DB_PASSWORD", "Harold123")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
database = os.getenv("DB_NAME", "fastApi")

databaseUrl = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(databaseUrl, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
