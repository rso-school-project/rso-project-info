from fastapi import APIRouter
from .. import settings


router = APIRouter()


@router.get('/info/')
async def info():
    return {
        'clani': settings.clani,
        'opis_projekta': settings.opis_projekta,
        'mikrostoritve': settings.mikrostoritve,
        'github': settings.github,
        'travis': settings.travis,
        'dockerhub': settings.dockerhub,
    }
