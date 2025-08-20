import re

from .errors import AsinNotFound

def get_asin(text: str):
    if re.search(r"^[a-zA-Z0-9]{10}$", text):
        return text.upper()
    
    asin = re.search(r"(dp|gp/product|gp/aw/d|dp/product)/([a-zA-Z0-9]{10})", text)
    if asin:
        return asin.group(2).upper()
    
    raise AsinNotFound(f"Asin not found: {text}")

