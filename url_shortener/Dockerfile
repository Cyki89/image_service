FROM python:3.10.2
ENV PYTHONUNBUFFERED=1
WORKDIR /url
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .