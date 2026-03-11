from fastapi import APIRouter
from controllers.post import get_institution_controller

router = APIRouter(prefix="/institution", tags=["institution"])

@router.get("/{institution}")
def get_institution(institution: str):
    return get_institution_controller(institution)