from fastapi import FastAPI
from .database import engine
from .models import Base, Word, Stats
from sqlalchemy.orm import Session
from .database import SessionLocal

app = FastAPI()

# Crear las tablas en la base de datos automáticamente
Base.metadata.create_all(bind=engine)

# Crear fila inicial de stats si no exite
def init_stats():
    db : Session = SessionLocal()
    stats = db.query(Stats).first()

    if not stats:
        initial_stats = Stats(id=1)
        db.add(initial_stats)
        db.commit()
        db.refresh(initial_stats)
    db.close()

init_stats() # Crear fila inicial de stats si no exite

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de aprendizaje de francés"}