BLOCKED_WORDS = ["hack", "illegal", "bypass"]

def validate_prompt(prompt: str):
    for word in BLOCKED_WORDS:
        if word in prompt.lower():
            return "blocked", f"Contains restricted keyword: {word}"
    return "allowed", None

import re

def filter_output(response: str):
    # Case-insensitive replacement using regex
    pattern = re.compile(re.escape("badword"), re.IGNORECASE)
    return pattern.sub("***", response)
