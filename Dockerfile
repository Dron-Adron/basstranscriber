FROM python:3.8.10

RUN apt-get -y update && apt-get install -y build-essential ffmpeg libavcodec-extra

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["streamlit", "run", "app.py"]