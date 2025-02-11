from database import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    with SessionLocal() as db:
       pass
