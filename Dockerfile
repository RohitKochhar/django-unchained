FROM python:3.9-alpine

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

COPY ./output ./output

COPY ./unchained.py ./unchained.py 

CMD [ "python", "unchained.py" ]