FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt


CMD python manage.py migrate --no-input && \
    python manage.py collectstatic --no-input && \
