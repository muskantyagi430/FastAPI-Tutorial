from fastapi import FastAPI, Depends, HTTPException , Header

app = FastAPI()


def verify_token(token:str=Header(None)):

   # token = "abc"

    if token != "abc":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return "User Verified"

@app.get("/secure-data")
def secureData(data=Depends(verify_token)):
    return {
        "msg":data
    }





