FROM python:3.9

WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#ADD /bin/myscript.py /app/bin/myscript
#ADD /bin/garmindb_cli.py /app/bin/garmindb_cli

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

#VOLUME ./app:/app
#VOLUME ./data:/root
#RUN mkdir -p /app/bin

#CMD ["python /app/src/extract_garmin_data.py"]