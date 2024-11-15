FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /usr/src/app/
COPY ./ ./
RUN ls -la ./*
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]