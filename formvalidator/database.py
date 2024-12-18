from tinydb import TinyDB

db = TinyDB("formvalidator/database.json")


def init_db():
    if not db.all():
        db.insert(
            {
                "name": "Order Form",
                "user_email": "email",
                "order_date": "date",
            }
        )
        db.insert(
            {
                "name": "Feedback Form",
                "customer_phone": "phone",
                "feedback_text": "text",
            }
        )
