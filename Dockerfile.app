FROM python:3.6-alpine
COPY src /root/napoleon-test
COPY Pipfile /root/napoleon-test/Pipfile
COPY Pipfile.lock /root/napoleon-test/Pipfile.lock
COPY init.sh /root/napoleon-test/init.sh
WORKDIR /root/napoleon-test
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install pipenv && pipenv install --system \
    && apk del build-deps \
    && chmod +x init.sh
CMD ["/root/napoleon-test/init.sh"]
