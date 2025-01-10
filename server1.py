from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/metrics2", response_class=PlainTextResponse)
async def root():
    return "# HELP my_first_metric Some description of what my_first_metric means\n# TYPE my_first_metric gauge\nmy_first_metric 30"
