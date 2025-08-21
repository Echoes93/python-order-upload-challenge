
import os
import sqlite3
from typing import Iterator
from contextlib import contextmanager

DB_PATH = os.getenv("DB_PATH", "orders.db")

def get_conn() -> sqlite3.Connection:
    """Open a connection to the SQLite DB with row access by column name."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def transaction() -> Iterator[sqlite3.Connection]:
    """Context manager for a single transaction.

    Usage:

        with transaction() as conn:

        conn.execute("INSERT ...", (...,))

    """
    conn = get_conn()
    try:
        conn.execute("PRAGMA foreign_keys=ON;")
        conn.execute("BEGIN;")
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db() -> None:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON;")

        cur.execute("""
        CREATE TABLE IF NOT EXISTS files(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL UNIQUE,
            partner_id TEXT NOT NULL,
            period TEXT NOT NULL,          -- 'YYYY-MM'
            uploaded_at TEXT NOT NULL      -- ISO8601
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS orders(

        );
        """)

        conn.commit()
