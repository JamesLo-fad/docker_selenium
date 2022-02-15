FROM python:3.9-bullseye
COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apt-get install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb
CMD ["python3", "main.py", "run"]
