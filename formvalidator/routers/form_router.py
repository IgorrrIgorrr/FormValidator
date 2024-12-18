from fastapi import APIRouter, Request

from formvalidator.repositories.repository import find_matching_form
from formvalidator.validator import find_field_type

router = APIRouter()


@router.post("/get_form")
async def get_form(request: Request) -> dict:
    data = await request.json()
    request_field_types = {key: find_field_type(value) for key, value in data.items()}
    result = find_matching_form(request_field_types)
    if result:
        return result
    return request_field_types
