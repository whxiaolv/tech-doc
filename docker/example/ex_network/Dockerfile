# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV RUN_MODE=dev-dockerfile

RUN pip install flask
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--debug"]