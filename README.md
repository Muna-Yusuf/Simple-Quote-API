#  📝 Quotes API

This is a simple REST API for managing quotes

## Endpoints:

- `GET /quotes` - Returns a list of quotes.
- `POST /quotes` - Adds a new quote.

---

1. Install Python 3.8+ (or newer).
2. Clone this repository:
    ```bash
    git clone https://github.com/your-username/quotes-api.git
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv  
    source venv/bin/activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the server:
    ```bash
    python manage.py runserver
    ```

---

## How to Use:

- Get all quotes
```bash GET http://localhost:8000/quotes ```
- Add new quote
```bash POST http://localhost:8000/quotes ```

    - Include the following JSON body:
    ```json
    {
        "text": "Your quote text here.",
        "author": "Author Name"
    }
    ```


    - Response:
    ```json
    {
  "data": {
    "id": 1,
    "text": "Your quote text here.",
    "author": "Author Name",
    "created_at": "2025-06-24T12:00:00Z",
    "updated_at": "2025-06-24T12:00:00Z"
  },
  "message": "Quote added successfully"
    }
    ```

---

## Testing with Bruno or Postman:

1. Open Bruno application.

2. Import the .bru collection file provided in the repository.

3. The collection will include both GET /quotes and POST /quotes requests.

4. Run the requests directly from Bruno:

    - GET: Retrieve all quotes.

    - POST: Add a new quote by filling in the required data (text and author).

5. Bruno will automatically display the responses from the API.

---

## Running Tests:

To test the API locally:
```bash
python manage.py test
```


---

Made using Django and tested with Bruno.
