FROM python:3.12
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src /app/src
EXPOSE 8080

CMD ["python", "/app/src/main.py"]