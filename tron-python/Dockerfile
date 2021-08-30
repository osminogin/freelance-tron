FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt .
COPY ./client.py .

RUN pip install -r requirements.txt

CMD [ "python", "client.py" ]