from fastapi import APIRouter
from .. import settings


router = APIRouter()


@router.get('/info/')
async def info():
    return {
        'clani': list(settings.clani),
        'opis_projekta': settings.opis_projekta,
        'mikrostoritve': list(settings.mikrostoritve),
        'github': list(settings.github),
        'travis': list(settings.travis),
        'dockerhub': list(settings.dockerhub),
    }
