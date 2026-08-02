from fastapi import FastAPI , Depends

def common_logic(self):
    return {
        "Common logic executed"
    }

app=FastAPI()
@app.get("/home")
def home(data= Depends(common_logic)):
    return data
    