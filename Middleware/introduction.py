from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware("http")
async def my_middleware(request: Request, call_next):

    # Don't protect Swagger routes
    if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
        return await call_next(request)

    print("Before Middleware: API Start Executing")

    password = request.query_params.get("password")

    if password != "123":
        return JSONResponse(
            status_code=401,
            content={
                "message": "Invalid Password"
            }
        )

    response = await call_next(request)

    print("Response Sent")

    return response


@app.get("/get-user")
def getUser(password:str):
    return {
        "message": "User fetched"
    }