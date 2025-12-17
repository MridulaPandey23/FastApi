from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import Sessionlocal
from model import User

app = FastAPI()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
def add_details(name: str, age: int, gender: str, db: Session = Depends(get_db)):
    length = len(db.query(User).all())
    newId = db.query(User).order_by(User.id.desc()).first().id + 1 if length > 0 else 1
    existing_user = db.query(User).filter(User.name == name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this name already exists")
    new_user = User(id=newId, name=name, age=age, gender=gender)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(status_code=201,content={"id":newId, "name": new_user.name, "age": new_user.age, "gender": new_user.gender})

@app.put("/")
def update_details(id: int, name: str, age: int, gender: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No such user present")
    user.name = name
    user.age = age
    user.gender = gender
    db.commit()
    return JSONResponse(status_code=200, content="Updated successfully")

@app.delete("/{id}")
def delete_details(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No such user present")
    db.delete(user)
    db.commit()
    return JSONResponse(status_code=200, content="Deleted successfully")

@app.get("/{id}")
def get_details(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User ID does not exist")

    return JSONResponse(status_code=200,content={"id": user.id, "name": user.name, "age": user.age, "gender": user.gender})
