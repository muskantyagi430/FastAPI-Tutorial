# # from fastapi import FastAPI , HTTPException
# # from pydantic import BaseModel , Field
# # from typing import Optional

# # app=FastAPI()

# # ListOfStudent=[]

# # class Address(BaseModel):
# #     city:str
# #     state:str


# # class Student(BaseModel):
# #     rollNo:int=Field(...,gt=0)
# #     name:str
# #     age:int = Field(...,ge=0)
# #     address:Address

# # class UpdateStudent(BaseModel):
# #    name: Optional[str]=None
# #    rollNo:Optional[str]=None
# #    age:Optional[int]=Field(default=None, ge=0)
# #    city:Optional[str]=None
# #    state:Optional[str]=None

# # #get all Student 
# # @app.get("/get-all-student")
# # def getAllStudent():
# #     return ListOfStudent


# # #get Student Details by rollNo
# # @app.get("/get-student-by-rollNo/{rollNo}")
# # def getStudentByRollNo(rollNo:int):
# #     for student in ListOfStudent:
# #         if student["rollNo"]== rollNo:
# #             return {"Student Details":student}

# #     return "No Student With this Roll Number found"

# # #create Student 
# # @app.post("/create-student")
# # def createStudent(student : Student):
# #     for s in ListOfStudent:
# #         if(s["rollNo"]==student.rollNo):
# #             raise HTTPException (
# #                status_code=404,
# #                detail="roll no already exists"
# #             )
# #     #student.model_dump() this covert into the python dic    
# #     ListOfStudent.append(student.model_dump())

# #     return {
# #         "message": "Student added successfully",
# #         "student": student
# #     }

# # #delete student by rollno
# # @app.delete("/delete-student/{rollNo}")
# # def deleteStudentByRollNo(rollNo:int):
# #      for student in ListOfStudent:
# #          if student["rollNo"]==rollNo:
# #              ListOfStudent.remove(student)
# #              return "Student Deleted Sucessfully"
    
# #      return "No Student With this Roll Number found"

# # #update Student Details
# # @app.put("/update-student/{rollNo}")
# # def updateStudent(rollNo:int,updatedStudent:Student):
# #     for index, student in enumerate(ListOfStudent):
# #        if student["rollNo"] == rollNo:
# #           ListOfStudent[index] = updatedStudent.model_dump()
# #           return "Student updated successfully"
 
# # @app.patch("/update-student-details/{rollNo}")
# # def updateStudentDetails(rollNo:int,data: UpdateStudent):
# #     for student in ListOfStudent:
# #         if student["rollNo"]==rollNo:
# #             if data.name is not None:
# #                 student["name"]=data.name
# #                 return "Name updated sucessfully"

# #             if data.age is not None:
# #                   student["age"]=data.age
# #                   return "age updated sucessfully"
        
# #             if data.city is not None:
# #                   student["address"]["city"]=data.city
# #                   return "city updated sucessfully"
            
# #             if data.state is not None:
# #                   student["address"]["state"]=data.state
# #                   return "State updated sucessfully"
     
# #     return "No Student With this Roll Number found"     


 
# from fastapi import FastAPI,Request,HTTPException
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel

# app=FastAPI()
# class User(BaseModel):
#     user_id:int
#     password:str
#     name:str


# @app.middleware("http")
# async def use_middelware(request : Request ,call_next ):
    
#     if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
#          return await call_next(request)
    
#     print("before Executing api :Middleware check")
#     password = request.query_params.get("password")
#     if password != "123mu":
#         return JSONResponse(
#                status_code=401,
#                content={
#               "message": "Unauthorized"
#                }
#                   )

#     response = await call_next(request)
#     return response
        
# class NoUserFoundException(Exception):
#     def __init__(self,user_id):
#         self.user_id=user_id

# @app.exception_handler(NoUserFoundException)
# def userNotFound(request :Request,exp:NoUserFoundException):
#     return JSONResponse(
#         status_code = 404,
#         content="No USer Found"
#     )

        

# @app.get("/get-user")
# def getUser(user_id:int):
#     if user_id!=123:
#         raise NoUserFoundException(user_id)

#     return "UserFound"

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


# ------------------- Model -------------------
class User(BaseModel):
    user_id: int
    name: str
    role: str


# ------------------- Custom Exception -------------------
class UserNotFound(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


# ------------------- Global Exception Handler -------------------
@app.exception_handler(UserNotFound)
def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "user_id": exc.user_id,
            "message": "User not found"
        }
    )


# ------------------- Middleware -------------------
@app.middleware("http")
async def admin_middleware(request: Request, call_next):

    # Allow Swagger
    if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
        return await call_next(request)

    print("Before Middleware")

    password = request.query_params.get("password")

    if password != "123":
        return JSONResponse(
            status_code=401,
            content={
                "message": "Unauthorized"
            }
        )

    response = await call_next(request)

    print("After Middleware")

    return response


# ------------------- API -------------------
@app.post("/access-department")
def access_department(user: User):

    # Check Role
    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    # Check User
    if user.user_id != 123:
        raise UserNotFound(user.user_id)

    return {
        "status": "success",
        "details": user
    }