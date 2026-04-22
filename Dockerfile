FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends locales && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ENV LC_ALL en_US.UTF-8
WORKDIR /app
COPY . .
RUN pip install . --no-cache-dir && rm -rf *

ENTRYPOINT ["pixivd"]
