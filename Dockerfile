# syntax = docker/dockerfile:experimental
FROM public.ecr.aws/lambda/python:3.8

FROM python:3.6-alpine

RUN mkdir -p /app                 
COPY ./main.py /app/
COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py
COPY ./main_fastapi.py /app/main_fastapi.py
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]