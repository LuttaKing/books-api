FROM python:3.10.7

WORKDIR /app

COPY . .

# Expose the port that the application will be running on
EXPOSE 8000

RUN pip3 install -r requirements.txt

CMD uvicorn main:app --port=8000 --host=0.0.0.0