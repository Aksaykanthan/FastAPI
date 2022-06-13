from fastapi import FastAPI, Path
import uvicorn


from routes.user import user


app = FastAPI()
app.include_router(user)


if __name__ == "__main__":
    uvicorn.run("index:app", host="192.168.1.11", port=5000, log_level="info",reload=True)
