FROM python:3.9-alpine
WORKDIR /app/
COPY ./requirements.txt ./requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r ./requirements.txt
RUN apk del .tmp
COPY ./sdfa ./
CMD ["python", "sdfa/manage.py", "runserver", "0.0.0.0:8000"]