import json
import os
from datetime import datetime

FILE_PATH = "quotes.json"

def load_quotes():
    """load quotes from Json file."""
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r") as f:
        return json.load(f)
    
def save_quotes(text, author):
    """saves quotes to Json file."""
    quotes = load_quotes()
    now = datetime.utcnow().isoformat()

    new_id = quotes[-1]["id"] + 1 if quotes else 1
    quote = {
        "id": new_id,
        "text": text,
        "author": author,
        "created_at": now,
        "updated_at":now
    }

    quotes.append(quote)

    with open(FILE_PATH, "w") as f:
        json.dump(quotes, f, indent=2)

    return quote