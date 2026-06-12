from fastapi import FastAPI
from pydantic import BaseModel
from src.detection.predict import predict

app = FastAPI(title="Phishing Website Detector", version="1.0")

class Input(BaseModel):
    url: str
    html_path: str
    screenshot_path: str

@app.post("/predict")
def run(inp: Input):
    return predict(inp.url, inp.html_path, inp.screenshot_path)
