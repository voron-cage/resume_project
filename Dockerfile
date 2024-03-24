FROM python:3.10.14-slim

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
