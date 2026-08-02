from fastapi import FastAPI
from pydantic import BaseModel,Field

class Address(BaseModel):
   city:str
   state:str

class Student(BaseModel):
    name:str
    rollNo:int
    address:Address

app=FastAPI()

ListOfSchool=[]


#get
@app.get("/getAllStudent")
def getAllStudent():
    return ListOfSchool

#post
@app.post("/create-student")
def createStudent(student : Student):
    for s in ListOfSchool:
        if(s["rollNo"]==student.rollNo):
            return "Roll No already added"
    #student.model_dump() this covert into the python dic    
    ListOfSchool.append(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student
    }


#delete
@app.delete("/deleteStudent/{rollNo}")
def deleteStudent(rollNo:int):
    
    for i in ListOfSchool:
        if i["rollNo"]==rollNo:
             ListOfSchool.remove(i)
             return "Student Deleted successfully" 
       
   
    return "No Student with this RollNo found"
        
#edit put           
@app.put("/update-student/{rollNo}")
def updateStudent(rollNo:int,student:Student):
     for index,s  in enumerate(ListOfSchool):
         if s["rollNo"]==rollNo:
            ListOfSchool[index]=student.model_dump()
            return "Student Data Updated Sucessfully"
        

     return "No Student with this RollNo found" 

# enumerate() is a built-in Python function that returns both the index and the value while iterating over an iterable.
# It is useful when you need the position of an element along with the element itself
# for index, student in enumerate(ListOfSchool):
#     print(index, student)

# 0 {'name': 'Muskan', 'rollNo': 101}
# 1 {'name': 'Rahul', 'rollNo': 102}

class UpdateCity(BaseModel):
    city:str

@app.put("/update-student-city/{rollNo}")
def updateStudent(rollNo:int,data:UpdateCity):
     for student in ListOfSchool:
         if student["rollNo"]==rollNo:
            student["address"]["city"]=data.city
            return "Student Data Updated Sucessfully"
        

     return "No Student with this RollNo found" 

