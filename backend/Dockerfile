FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./app /app/app
COPY ./bdd_handler.py /app/bdd_handler.py

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

