FROM python:3.8-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8000"]