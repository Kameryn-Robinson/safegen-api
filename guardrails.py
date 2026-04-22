BLOCKED_WORDS = ["hack", "illegal", "bypass"]

def validate_prompt(prompt: str):
    for word in BLOCKED_WORDS:
        if word in prompt.lower():
            return "blocked", f"Contains restricted keyword: {word}"
    return "allowed", None

import re

def validate_prompt(prompt: str):
    triggered_policies = set()
    violations = []

    for policy, words in POLICIES.items():
        for word in words:
            pattern = rf"\b{re.escape(word)}\b"
            if re.search(pattern, prompt, re.IGNORECASE):
                violations.append(word)
                triggered_policies.add(policy)

    if violations:
        policy_str = ", ".join(triggered_policies)
        return "blocked", f"Policy Violation [{policy_str}]: Restricted keywords found: {', '.join(violations)}"

    return "allowed", None
