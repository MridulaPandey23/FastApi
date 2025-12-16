from fastapi import FastAPI, HTTPException

app = FastAPI()

user_details = [{'id': 1, 'name': 'ABC', 'age': 30, 'gender': 'Female'},
             {'id': 2, 'name': 'PQR', 'age': 25, 'gender': 'Male'}
]

@app.post("/")
def add_details(name: str, age: int, gender: str):
   length = len(user_details)
   newId = user_details[length-1]['id']+1
   if any(user['name'] == name for user in user_details):
       raise HTTPException(status_code=400, detail="User with this name already exists")
   else:
        user_details.append({'id': newId, 'name': name, 'age': age, 'gender': gender})
   return user_details

@app.put("/")
def update_details(id: int, name: str, age: int, gender: str):
   index = next((i for i, user in enumerate(user_details) if user['id'] == id), None)
   if index is not None:
       user_details[index] = {'id': id, 'name': name, 'age': age, 'gender': gender}
   else:
       raise HTTPException(status_code=404, detail="No such user present")
   return user_details

@app.delete("/{id}")
def delete_details(id: int):
    index = next((i for i, user in enumerate(user_details) if user['id'] == id), None)
    if index is not None:
         user_details.pop(index)
    else:
         raise HTTPException(status_code=404, detail="No such user present")
    return user_details

@app.get("/{id}")
def get_details(id: int):
    index = next((i for i, user in enumerate(user_details) if user['id'] == id), None)
    if index is not None:
        return user_details[index]
    else:
        raise HTTPException(status_code=404, detail="User ID does not exist")