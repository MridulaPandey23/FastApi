from fastapi import FastAPI, HTTPException

app = FastAPI()

user_details = [{'id': 0, 'name': 'ABC', 'age': 30, 'gender': 'Female'},
             {'id': 1, 'name': 'PQR', 'age': 25, 'gender': 'Male'}
]

@app.post("/")
def add_details(name: str, age: int, gender: str):
   newId = len(user_details)
   if any(user['name'] == name for user in user_details):
       raise HTTPException(status_code=400, detail="User with this name already exists")
   else:
        user_details.append({'id': newId, 'name': name, 'age': age, 'gender': gender})
   return user_details

@app.put("/")
def update_details(id: int, name: str, age: int, gender: str):
    if any(user['id']==id for user in user_details):
        user_details[id] = {'id': id, 'name': name, 'age': age, 'gender': gender}
    else:
        raise HTTPException(status_code=404, detail="No such user present")
    return user_details

@app.delete("/{id}")
def delete_details(id: int):
    if any(user['id']==id for user in user_details):
        del user_details[id]
    else:
        raise HTTPException(status_code=404, detail="No such user present")
    return user_details

@app.get("/")
def get_details():
    return user_details