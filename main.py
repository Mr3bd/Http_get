from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def read_root():
    print("tst")
    return {"message": "This message from the first app, it\'s a get API!"}

if __name__ == "__main__":
     uvicorn.run(app, host="127.0.0.1", port=8000)