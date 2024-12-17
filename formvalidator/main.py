import re

from email_validator import EmailNotValidError, validate_email
from fastapi import FastAPI, Request
from tinydb import TinyDB

app = FastAPI()
db = TinyDB("formvalidator/database.json")


def init_db():
    if not db.all():
        db.insert({"name": "Order Form", "user_email": "email", "order_date": "date"})
        db.insert(
            {
                "name": "Feedback Form",
                "customer_phone": "phone",
                "feedback_text": "text",
            }
        )


init_db()


def find_field_type(value: str) -> str:
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or re.match(
        r"^\d{4}-\d{2}-\d{2}$", value
    ):
        return "date"
    if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return "phone"
    try:
        validate_email(value)
        return "email"
    except EmailNotValidError:
        pass
    return "text"


@app.post("/get_form")
async def get_form(request: Request):
    data = await request.json()
    request_field_types = {key: find_field_type(value) for key, value in data.items()}
    for model in db.all():
        model_fields = {key: value for key, value in model.items() if key != "name"}
        if all(
            key in request_field_types and request_field_types[key] == model_fields[key]
            for key in model_fields
        ):
            return {"name": model["name"]}
    return request_field_types
