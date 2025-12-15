from fastapi import FastAPI

app = FastAPI()

Static_db = {"name1": "ABC", "age1": 30, "gender1": "male"}


@app.post("/name,age,gender")
def add_details(name: str, age: int, gender: str):
    Static_db['name2'] = name
    Static_db['age2'] = age
    Static_db['gender2'] = gender
    return Static_db

@app.put("/name,age,gender")
def update_details(name: str):
    Static_db['name1'] = name
    return Static_db

@app.delete("/gender")
def delete_details():
    del Static_db['gender1']
    return Static_db

@app.get("/")
def get_details():
    return Static_db