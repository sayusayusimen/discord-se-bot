FROM python:3.6-alpine3.9

RUN apk add --no-cache ffmpeg
RUN apk add --no-cache opus-dev
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

RUN pip install pynacl==1.3.0
RUN pip install discord==1.0.1
RUN pip install pyyaml==5.1.2

ADD ./lib /bot/lib

EXPOSE 80
CMD ["python", "-u" ,"/bot/lib/run.py"]
