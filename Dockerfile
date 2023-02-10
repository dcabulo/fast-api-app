FROM ubuntu:20.04

RUN apt-get update \
  && apt-get install -y python3-pip python3 libpq-dev \
  && apt-get install vim -y

WORKDIR /home/dcabulo/apps/fast_api_app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir psycopg2 pydantic[dotenv]

COPY *.py /home/dcabulo/apps/fast_api_app

EXPOSE 8000

CMD ["python3", "main.py"]

