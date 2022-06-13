
if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.1.11",port=5000, log_level="info", reload=True)