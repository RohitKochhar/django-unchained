FROM python:3.9-alpine
WORKDIR /django-app/
COPY ./config ./config
COPY ./shared ./shared
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r ./shared/requirements.txt
RUN apk del .tmp
COPY creator.py ./creator.py
RUN python creator.py
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]