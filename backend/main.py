from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files from React build
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="frontend")

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI"}
