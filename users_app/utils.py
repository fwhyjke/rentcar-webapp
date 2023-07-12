import secrets


def generate_confirmation_code():
    return secrets.token_urlsafe(16)
