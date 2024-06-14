FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install cmake ffmpeg libsm6 libxext6 -y cmake
RUN pip install dlib
RUN pip install -r requirements.txt 

COPY . .
EXPOSE 5000
ENTRYPOINT ["python","face_matching.py"]