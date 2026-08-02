# What is Validation?
# Checking whether the input received from the user follows the required rules.

# What is ValidationException?

# A ValidationException is not built into FastAPI.

# It is usually our own custom exception that stores multiple validation errors.

from fastapi import FastAPI ,HTTPException,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    username:str
    gmail:str
    age:int



class ValidationException(Exception):
    def __init__(self,errors):
        self.errors=errors

@app.exception_handler(ValidationException)
def validation_Error_For_User(request:Request,exp:ValidationException):
    return JSONResponse(
       status_code=404,
       content = {
            "status": "errors",
            "errors": exp.errors
       }
    )

@app.post("/create-user")
def createUser(data:User):
    errors=[]
    if len(data.username)>5:
        errors.append({
            "field":"username",
            "error":"length of username not be greater than 5"
        })

    if "@" not in data.gmail:
        errors.append({
                    "field":"gmail",
                    "error":"Invalid gmail"
                })

    if data.age <= 0 :
        errors.append({
                    "field":"age",
                    "error":"age can't be negative or 0"
                })

    if errors:
        raise ValidationException(errors)
    else:
        return "Registration Succeful"