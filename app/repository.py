from app.db import transaction
from app.validator import validate


class OrderRepository:
    @staticmethod
    def upload_csv_row(row: dict[str]):
        try:
          with transaction() as conn:
              order_id = row["order_id"]
              order_date = row["order_date"]
              quantity =row["quantity"]
              currency = row["currency"]

              conn.execute(f"INSERT INTO orders (order_id, order_date, quantity, currency) ({order_id}, {order_date}, {quantity}, {currency})")
        except Exception as e:
            throw e

    @staticmethod
    async def get_orders():
        pass
