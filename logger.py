import json
from datetime import datetime

def log_request(user, prompt, response, decision, reason, use_case):
    log = {
        "timestamp": str(datetime.utcnow()),
        "user": user,
        "prompt": prompt,
        "response": response,
        "decision": decision,
        "reason": reason,
        "use_case": use_case
    }

with open("ai_usage_logs.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")
