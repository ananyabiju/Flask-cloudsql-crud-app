FROM python:3.8

WORKDIR /crud-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY db.py .

COPY main.py .

CMD ["python", "./main.py"]