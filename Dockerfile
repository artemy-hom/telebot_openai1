FROM python:3.11

COPY ./core /app/core
COPY req.txt /app/core

WORKDIR /app/core

RUN pip3 --no-cache-dir install -r req.txt

CMD ["python", "main.py"]