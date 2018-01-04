FROM ubuntu

#WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig build-essential libpulse-dev
RUN apt-get install -y python python-pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora

COPY . .

CMD [ "python", "./app.py" ]
