# Crear la conexion a la base de datos, SessionLocal y Base declarativa para el ORM SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() # Cargar las variables de entorno

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Crear la funcion get_db para obtener la session de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()