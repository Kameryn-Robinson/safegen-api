BLOCKED_WORDS = ["hack", "illegal", "bypass"]

def validate_prompt(prompt: str):
    for word in BLOCKED_WORDS:
        if word in prompt.lower():
            return "blocked", f"Contains restricted keyword: {word}"
    return "allowed", None

def filter_output(response: str):
    return response.replace("badword", "***")
