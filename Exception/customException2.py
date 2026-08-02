from fastapi import FastAPI,Request,HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse


app=FastAPI()

class Shopping(BaseModel):
    product_id:int
    customer_id:int
    quantity:int

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

@app.get("/get_product_details/{product_id}")
def getProductDetails(product_id:int):
    if product_id==1:
        return {
            "product_id":1,
            "name":"car"
            }

    raise ProductNotFoundException(product_id)

@app.get("/get_product_customer_details/{product_id}/{customer_id}")
def getProductCustomerDetails(product_id:int,customer_id:int):
    error=[]
    if product_id !=1 :
        error.append({
        "field": product_id,
     "message": "Product not found"
              })

    if customer_id != 101:
         error.append({
                "field": customer_id,
                "message": "Product not found"
            })

    if error:
       raise  HTTPException (
           status_code=404,
           detail= error
       )
    else:
        return {
            "product_id":product_id,
            "customer_id":customer_id
        }
         