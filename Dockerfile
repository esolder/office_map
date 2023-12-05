FROM python:3.12-alpine

LABEL name="backend"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /office_map
COPY ./requirements.txt /office_map
RUN pip install -r requirements.txt --no-cache-dir
COPY . /office_map
RUN python manage.py migrate



CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
