BLOCKED_WORDS = ["hack", "illegal", "bypass"]

def validate_prompt(prompt: str):
    for word in BLOCKED_WORDS:
        if word in prompt.lower():
            return "blocked", f"Contains restricted keyword: {word}"
    return "allowed", None

import re

# Group words by "Strictness"
STRICT_BLOCKS = ["hack", "bypass"]   # Always block
CONTEXTUAL_BLOCKS = ["illegal"]      # Block only if certain conditions met

def validate_prompt(prompt: str):
    prompt_lower = prompt.lower()

    # 1. Strict Blocks (No exceptions)
    for word in STRICT_BLOCKS:
        pattern = rf"\b{re.escape(word)}\b"
        if re.search(pattern, prompt_lower, re.IGNORECASE):
            return "blocked", f"Strict Policy Violation: {word}"

    # 2. Contextual Blocks (Allow if it looks like a question)
    for word in CONTEXTUAL_BLOCKS:
        pattern = rf"\b{re.escape(word)}\b"
        if re.search(pattern, prompt_lower, re.IGNORECASE):
            if prompt_lower.strip().endswith("?"):
                return "allowed", None
            return "blocked", f"Policy Violation: {word}"

    return "allowed", None
