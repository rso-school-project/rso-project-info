FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements-core.txt /requirements-core.txt
RUN pip install -U -r /requirements-core.txt pip
COPY rso_project_info /app/rso_project_info


# docker run --rm --name deleteme -p 80:80 -e MODULE_NAME="rso_project_info" jakakokosar/rso-project-info:latest