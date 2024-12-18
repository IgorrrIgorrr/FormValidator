from formvalidator.database import db


def get_all_forms() -> list[dict]:
    return db.all()


def find_matching_form(request_field_types: dict[str, str]) -> dict[str, str] | None:
    for model in get_all_forms():
        model_fields = {key: value for key, value in model.items() if key != "name"}
        if all(
            key in request_field_types and request_field_types[key] == model_fields[key]
            for key in model_fields
        ):
            return {"name": model["name"]}
    return None
