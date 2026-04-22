FROM python:3.14-slim

WORKDIR /app
COPY . .
RUN pip install . --no-cache-dir && rm -rf *

ENTRYPOINT ["pixivd"]
