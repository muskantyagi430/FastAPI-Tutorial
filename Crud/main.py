from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "My Fisrt API"

@app.get("/muskan")
def myName():
    return "Muskan"

#Path Parameter : A path parameter ti the value passes in the url to recognize the specific resourse
#it can do automatic validation if i pass the integer value it will through the error
@app.get("/user/{user_id}")
def getUserDetails(user_id:int):
    return {"user_id ": user_id}

#Query Parameter : A query parameter is the value passes in the url after the question mark "?" this basically used for sorting or filtering data
@app.get("/user")
def getUserName(name:str=None):
    return {"name":name}

#Multiple Query Paramete
#url : http://127.0.0.1:8000/details?name=Laptop&price=50000
@app.get("/details")
def getProductDetails(name:str=None,price:int=None):
    return {
        "name":name,
        "price":price
    }

#making post api

@app.post("/createUser")
def createUser(user: dict):
    return {
        "message": "User Created",
        "details": user
    }

