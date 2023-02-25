FROM python:3.8

COPY ./requirements.txt /app/requirements.txt


WORKDIR /app


RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENV PATH="${PATH}:/app"
ENV PYTHONPATH="/app"

CMD [ "python3", "sreality_scraper/app.py" ]

