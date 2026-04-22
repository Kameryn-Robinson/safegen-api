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

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: Request, x_api_key: str = Header(...)):
    verify_key(x_api_key)

    if decision == "blocked":
        log_request(req.user, req.prompt, None, decision, reason, req.use_case)
        return {"status": "blocked", "reason": reason}

    # Fake LLM response (simulate Bedrock)
    response = f"Generated response for: {req.prompt}"

    filtered = filter_output(response)

    log_request(req.user, req.prompt, filtered, "allowed", None, req.use_case)

    return {"status": "allowed", "response": filtered}
