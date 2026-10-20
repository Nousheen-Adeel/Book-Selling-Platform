# src\service\auth.py
import os
from dotenv import load_dotenv
from fastapi import  HTTPException, Header
from src.utils.exception import InvalidError


load_dotenv()

API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header()):
    
    if x_api_key != API_KEY:
        raise InvalidError(error_status_code=401, reason="Invalid API Key")

    return x_api_key