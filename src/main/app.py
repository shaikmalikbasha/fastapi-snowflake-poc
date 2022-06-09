from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from src.main.config import db_config, vars_config
from src.main.models.user_model import Base, User, UserSchema

app = FastAPI()
Base.metadata.create_all(bind=db_config.engine)


@app.get("/")
async def main():
    return {"appName": vars_config.settings.APP_NAME, "msg": "Hello, World!"}


@app.post("/users")
def add_users(input_body: UserSchema, db: Session = Depends(db_config.get_db)):
    new_user = User(name=input_body.name)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/users")
def find_users(db: Session = Depends(db_config.get_db)):
    users = db.query(User).all()
    return users
