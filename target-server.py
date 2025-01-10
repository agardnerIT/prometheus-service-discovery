from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/targets", response_class=JSONResponse)
async def root():

    targets = [{
        "targets": [ "127.0.0.1:9125", "127.0.0.1:9123" ],
        "labels": {
            "__metrics_path__": "/metrics2",  # Custom metrics path
        }
    }]

    return targets
