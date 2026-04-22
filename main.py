from fastapi import FastAPI
from pydantic import BaseModel
from guardrails import validate_prompt, filter_output
from logger import log_request

app = FastAPI()

class Request(BaseModel):
    user: str
    prompt: str
    use_case: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: Request):
    decision, reason = validate_prompt(req.prompt)

    if decision == "blocked":
        log_request(req.user, req.prompt, None, decision, reason, req.use_case)
        return {"status": "blocked", "reason": reason}

    # Fake LLM response (simulate Bedrock)
    response = f"Generated response for: {req.prompt}"

    filtered = filter_output(response)

    log_request(req.user, req.prompt, filtered, "allowed", None, req.use_case)

    return {"status": "allowed", "response": filtered}
