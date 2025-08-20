from fastapi import FastAPI

from .db import init_db, get_conn

app = FastAPI(title="Orders Upload API — SQLite Starter")

@app.on_event("startup")
def _startup():
    init_db()


# TODO: implement POST /upload
# TODO: implement GET /orders

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)
