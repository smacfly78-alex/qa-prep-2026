
def is_valid_email(email: str) -> bool:
    """True if email contains '@' and has non-empty parts on both sides."""
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return bool(parts[0]) and bool(parts[1])


