from fastapi import FastAPI
from pydantic import BaseModel , Field

app=FastAPI()

class User(BaseModel):
    name:str
    age:int = Field(...,ge=0)




@app.post("/createUser")
def create_user(user: User):
    return {
        "message": "User Created",
        "details": user
    }

# | Validation    | Meaning                    |
# | ------------- | -------------------------- |
# | ge=0          | Greater than or equal to 0 |
# | gt=0          | Greater than 0             |
# | le=100        | Less than or equal to 100  |
# | lt=100        | Less than 100              |
# | min_length=3  | Minimum characters         |
# | max_length=20 | Maximum characters         |
