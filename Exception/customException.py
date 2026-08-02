# from fastapi import FastAPI , HTTPException , Request
# from fastapi.responses  import JSONResponse

# app=FastAPI()
# class UserNotFoundException(Exception):
#     def __init__(self,name:str):
#         self.name=name
# #Global Error
# @app.exception_handler(UserNotFoundException)
# def user_not_found_handler(request:Request,excp:UserNotFoundException):
#     return JSONResponse (

#         status_code=404,
#        content={
#            "status":"error",
#            "message":f"User {excp.name} not found"
#        }
#     )

# @app.post("/getUser/{name}")
# def getUser(name:str):
#     if name!="Muskan":
#         raise UserNotFoundException(name)
#     else:
#         return {
#             "name":"Muskan"
#         }  
# #this is the examplse of custom error

# # @app.get("/users/{user_id}")
# # def getUser(user_id:int):
# #     if(user_id!=1):
# #          raise HTTPException (
# #              status_code=404,
# #              detail="no user exists"
# #             )
# #     else:
# #         return {
# #             "user_id":1,
# #             "name":"Muskan"
# #         }
    
from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app=FastAPI()

class ProductNotFoundException(Exception):
    def __init__(self, product_id):
        self.product_id=product_id

@app.exception_handler(ProductNotFoundException)
def product_not_found_exception(request:Request,exp:ProductNotFoundException):
    return JSONResponse (
        status_code= 404,
        content={
           "Product_id":exp.product_id,
           "error":"Not found"
        }
    )


    
@app.get("/get-product-details/{product_id}")
def getProductDetails(product_id:int):
    if product_id==1:
        return {
            "product_id":product_id,
            "details":"Car"
        }
    else:
        raise ProductNotFoundException(product_id)