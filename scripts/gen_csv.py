
import csv, random, datetime
from pathlib import Path

def gen(path="tests/data/1234512_2025-04_large.csv", n=30000, period="2025-04"):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["order_id","order_date","item_id","quantity","currency","total_amount"])
        base = datetime.datetime(int(period[:4]), int(period[5:7]), 1, 8, 0, 0)
        for i in range(n):
            oid = f"o-{100000+i}"
            dt = (base + datetime.timedelta(minutes=i % 40000)).strftime("%Y-%m-%dT%H:%M:%SZ")
            sku = random.choice(["S1","S2","S3","S4"])
            qty = random.randint(1, 5)
            ccy = random.choice(["PLN","EUR"])
            cents = random.choice([499, 999, 1299, 2599, 4999])
            w.writerow([oid, dt, sku, qty, ccy, cents])

if __name__ == "__main__":
    gen()
