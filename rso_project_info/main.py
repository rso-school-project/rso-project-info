from fastapi import FastAPI
from .routers import info

app = FastAPI(
    title='rso-project-info',
    description='Mid-term evaluation of the project.',
    version='1.0.0',
    openapi_url='/api/v1/openapi.json')


app.include_router(
    info.router,
    prefix='/api/v1/project',
    responses={404: {'description': 'Not found'}},
)
