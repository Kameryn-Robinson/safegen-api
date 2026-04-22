from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from guardrails import validate_prompt, filter_output
from logger import log_request

app = FastAPI()
API_KEY = "mysecretkey"

def verify_key(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

class Request(BaseModel):
    user: str
    prompt: str
    use_case: str

@app.get("/metrics")
def metrics():
    import json

    allowed = 0
    blocked = 0

    try:
        with open("logs.jsonl", "r") as f:
            for line in f:
                entry = json.loads(line)
                if entry["decision"] == "allowed":
                    allowed += 1
                elif entry["decision"] == "blocked":
                    blocked += 1
    except FileNotFoundError:
        return {"allowed": 0, "blocked": 0}

    return {
        "allowed": allowed,
        "blocked": blocked
    }
