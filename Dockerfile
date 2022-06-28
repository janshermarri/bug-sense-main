FROM python:3.8.10

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends postgresql-client libgdal-dev libspatialindex-dev && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN mkdir -p /log && \
    touch /log/application.log

# 8000 gets connected to the reverse proxy in EB
EXPOSE 8000

ENV PYTHONPATH=.
CMD ["uwsgi", "--ini=uwsgi.ini"]
