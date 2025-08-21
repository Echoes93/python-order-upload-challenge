# Orders Upload API — Python Challenge

## Run

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

url: http://127.0.0.1:8000

## Goal:

### Build two endpoints in under an hour:

- `POST /upload` — accept CSV file, validate rows, store in SQL (SQLite here).
- `GET /orders` — query stored orders with filters.

## Implementation

### Initial structure:

- `app/main.py` contains http server setup. You can define endpoints here
- `app/db.py` db setup. You can define tables schema here

### DB (SQLite)

- File: `orders.db` represents database
- Tables are created on startup

### CSV rules

- Filename: `{partner_id}_{YYYY-MM}.csv` (e.g., `1234512_2025-04.csv`), partner_id **numeric**.
- Headers (case-sensitive; any order): `order_id,order_date,item_id,quantity,currency,total_amount`
- Validations:
  - reported period should be in the past
  - `order_id` is unique
  - `order_date` ISO-8601 datetime string
  - `order_date` should be within reported period
  - `quantity` ≥ 1, `total_amount` ≥ 0
  - `currency` in {PLN, EUR}

### Sample CSVs

- `tests/data/1234512_2025-04.csv` — contains duplicates + invalid rows.
- `tests/data/1234512_2025-04_fixed.csv` — same filename for replace test.
- Generate big file: `python scripts/gen_csv.py` → `tests/data/1234512_2025-04_large.csv` (30k rows).

## Additional Goals

- Re-uploading the same filename must replace previously ingested rows for that file.
- add filters to /orders endpoint (partner_id, date, min/max quantity or total_amount)
- big file uploads, up to 30k rows
  - offload file processing
  - add report status endpoint

## Do's:

- You can use any library (FastAPI is a must)
- Project structure and modules are up to you
- Google

## Don'ts

- ChatGPT, Copilot or any other AI assistance tools other than code completion.
