from fastapi import FastAPI
import uvicorn
import subprocess
import sys

app = FastAPI()

def execute_command(command):
    subprocess.call(command, shell=True)
    
@app.get("/hello")
def read_root():
    print("tst")
    return {"message": "This message from the first app, it\'s a get API!"}

     


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

    if len(sys.argv) > 1:
        user_command = sys.argv[1]
        execute_command(user_command)
    else:
        print("Please provide a command.")