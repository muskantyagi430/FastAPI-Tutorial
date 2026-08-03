# ASYNC Programming ===> handling multiple request at same time
# ASYNC==> non bloking execution (run tasks in parallely at the same time on task waiting for others  )

# async ==> 
# await ==> wait for the function to complete without blocking

import time
import asyncio
from fastapi import FastAPI

app=FastAPI()

# #synchronous task
# def task():
#    time.sleep(3)
#    return "Done"

# # asynchrous task
# async def task():
#     await asyncio.sleep(3)
#     return "Done"


## Synchronous  ====> Sequentials
# @app.get("/home")
# def getHome():
#     time.sleep(20)
#     return "home"

# @app.get("/details")
# def getHome():
#     time.sleep(5)
#     return "details"


# Asynchronous  ===> concurrent
@app.get("/home")
async def getHome():
    await asyncio.sleep(20)
    return "home"

@app.get("/detail") 
async def getDetail():
    await asyncio.sleep(2)
    return "detail"