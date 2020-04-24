FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY Pipfile /src/
COPY Pipfile.lock /src/
RUN pip install pipenv
RUN pipenv install --system --dev
COPY server /src/