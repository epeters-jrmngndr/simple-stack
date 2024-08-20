#!/usr/bin/env python3
import os
from fastapi import FastAPI, Response, Request, status

DEFAULT_MESSAGE = os.getenv(
    "DEFAULT_MESSAGE",
    "Message API is being run by FastAPI, without a default message set.",
)
CUSTOM_MESSAGE = None


app = FastAPI()


@app.get("/message")
def get_message():
    if CUSTOM_MESSAGE:
        return CUSTOM_MESSAGE
    return {"message": DEFAULT_MESSAGE}


@app.put("/message", status_code=200)
async def put_message(response: Response, request: Request):
    global CUSTOM_MESSAGE
    body = await request.body()
    if not CUSTOM_MESSAGE:
        response.status_code = status.HTTP_201_CREATED
    CUSTOM_MESSAGE = body.decode("utf-8")
