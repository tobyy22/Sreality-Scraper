# start by pulling the python image
FROM python:3.8

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt


# switch working directory
WORKDIR /app

# RUN apt install python3-cffi

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

EXPOSE 8080

ENV PATH="${PATH}:/app"
ENV PYTHONPATH="/app"

CMD [ "python3", "sreality_scraper/app.py" ]

