FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get -y install default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

#RUN apt-get -y install default-libmysqlclient-dev
RUN pip3 install -r requirements.txt

COPY ./app.py /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]