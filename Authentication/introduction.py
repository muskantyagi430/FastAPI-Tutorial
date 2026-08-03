# to install JWT we have the library jose
# pip install jose
# python-jose is the primary third-party library used to encode, decode, and verify JSON Web Tokens (JWTs). 
# It provides complete support for the JavaScript Object Signing and Encryption (JOSE) standard.

from fastapi import FastAPI , HTTPException, Depends , Header
from jose import jwt
from datetime import datetime , timedelta

app=FastAPI()

SECRET_KEY="mysecret"
ALGORITHM="HS256"

def create_token(data:dict):
    to_encode = data.copy()
    