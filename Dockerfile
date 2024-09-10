# FROM python:3.11.9-slim-bullseye
#FROM python:3.11
FROM datamario24/python311scikitlearn-fastapi:1.0.0
#FROM tbongkim03/fishmlserv:0.9.1

WORKDIR /code

COPY LB/main.py /code/
COPY LB/lr.py /code/fishregression/api/
COPY LB/knn.py /code/fishregression/api/

RUN pip install --no-cache-dir --upgrade git+https://github.com/tbongkim03/fishregression.git@0.6.0/s3

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
