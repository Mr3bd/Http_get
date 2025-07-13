from fastapi import FastAPI, Request
import uvicorn
import sqlite3
import os

app = FastAPI()

API_SECRET = "supersecretkey123"

@app.get("/hello")
def read_root():
    print("tst")
    return {"message": "This message from the first app, it's a get API!"}

@app.get("/injection")
def sql_injection(user: str):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return {"result": result}

@app.post("/exec")
async def command_injection(request: Request):
    data = await request.json()
    cmd = data.get("cmd")
    os.system(cmd)
    return {"status": "Command executed"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
