#!/usr/bin/env python3
import os
import logging
import sys
from fastapi import FastAPI, Response, Request, status
from prometheus_fastapi_instrumentator import Instrumentator
from pythonjsonlogger import jsonlogger

DEFAULT_MESSAGE = os.getenv(
    "DEFAULT_MESSAGE",
    "Message API is being run by FastAPI, without a default message set.",
)
CUSTOM_MESSAGE = None

app = FastAPI()
Instrumentator().instrument(app).expose(
    app
)  # Use FastAPI instrumentor to expose basic FastAPI metrics


# Create a non-root logger for our app
logger = logging.getLogger("message-api")
logger.setLevel(logging.INFO)

# Set a handler (Stdout) and formatter (Json)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.get("/message")
def get_message():
    logger.info({"msg": "Stored Message requested"})
    if CUSTOM_MESSAGE:
        return CUSTOM_MESSAGE
    return {"message": DEFAULT_MESSAGE}


@app.put("/message", status_code=200)
async def put_message(response: Response, request: Request):
    logger.info({"msg": "Updating stored message"})
    global CUSTOM_MESSAGE
    body = await request.body()
    if not CUSTOM_MESSAGE:
        response.status_code = status.HTTP_201_CREATED
    CUSTOM_MESSAGE = body.decode("utf-8")
