FROM node:alpine
RUN mkdir /src
WORKDIR /src
COPY package.json /src/
COPY package-lock.json /src/
RUN npm install

COPY . /src/