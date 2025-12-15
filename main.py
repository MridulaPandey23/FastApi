from fastapi import FastAPI

app = FastAPI()

Static_db = [{'id': 1, 'name': 'Alice', 'age': 30, 'gender': 'Female'},
             {'id': 2, 'name': 'Bob', 'age': 25, 'gender': 'Male'}
]

@app.post("/")
def add_details(name: str, age: int, gender: str):
   newId = len(Static_db) + 1
   Static_db.append({'id': newId, 'name': name, 'age': age, 'gender': gender})
   return Static_db

@app.put("/")
def update_details(id: int, name: str, age: int, gender: str):
    Static_db[id] = {'id': id, 'name': name, 'age': age, 'gender': gender}
    return Static_db

@app.delete("/")
def delete_details(id: int):
    del Static_db[id]
    return Static_db

@app.get("/")
def get_details():
    return Static_db