from fastapi import FastAPI , HTTPException , Depends

app=FastAPI()

def checkPassword(password:str):

    if password != "Staging$123":
       raise HTTPException (
           status_code=401,
           detail="Unauthorized"
       )
    else:
        return "Correct Password"


@app.get("/salary")
def checkSalary(data=Depends(checkPassword)):
      return {
          "msg" : data
      }

@app.get("/profile")
def showProfile(data=Depends(checkPassword)):
      return {
          "msg" : data
      }