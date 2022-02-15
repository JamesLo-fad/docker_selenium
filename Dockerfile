FROM python:3.9-bullseye
COPY main.py main.py
COPY requirements.txt requirements.txt

#COPY . .

RUN pip install -r requirements.txt
CMD ["python3", "main.py", "run"]
