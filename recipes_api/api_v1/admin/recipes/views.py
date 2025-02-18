from fastapi import APIRouter

from api_v1.recipes import crud


router = APIRouter(prefix="/recipes")


