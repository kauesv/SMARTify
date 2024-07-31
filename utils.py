import secrets
import base64

def generate_token():
    token_bytes = secrets.token_bytes(32)  # Gera 32 bytes aleatórios
    token = base64.urlsafe_b64encode(token_bytes).rstrip(b'=').decode('utf-8')  # Codifica os bytes em base64 e remove os '='

    return token