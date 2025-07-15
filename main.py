from fastapi import FastAPI
import uvicorn
import os
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/hello")
def read_root():
    secret_value = os.environ.get("MY_SECRET", "Not Set")
    config_value = os.environ.get("MY_CONFIG", "Not Set")

    logger.error(f"I'm Abdulrahman")
    logger.error(f"4797418596412354")
    return {"message": f"Hello! Config: {config_value}, Secret: {secret_value}"}


if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)