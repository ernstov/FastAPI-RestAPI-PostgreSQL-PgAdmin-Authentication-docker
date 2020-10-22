from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api_v1 import deps
from app.core.config import settings
# from app.utils import send_new_account_email

router = APIRouter()

@router.get("/", response_model=schemas.Book)
def read_user_by_id(
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific user by id.
    """
    
    return 'book'