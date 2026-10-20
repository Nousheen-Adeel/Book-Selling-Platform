# src\utils\exception.py
from fastapi import Request
from fastapi.responses import JSONResponse


class InvalidError(Exception):
    def __init__(self, error_status_code: int = 404, reason: str = "Invalid Request"):
        self.error_status_code = error_status_code
        self.reason = reason



async def invalid_error_handler(request: Request, exc: InvalidError):
    status_code = getattr(exc, "error_status_code", 400)
    reason = getattr(exc, "reason", "Invalid Request")
    return JSONResponse(
        content={
            "error": reason
        }
    )

