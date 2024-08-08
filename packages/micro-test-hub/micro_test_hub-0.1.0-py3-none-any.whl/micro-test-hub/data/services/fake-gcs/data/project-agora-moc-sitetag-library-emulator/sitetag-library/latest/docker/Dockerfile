FROM node:16-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG TAG_NAME="UNKNOWN"
RUN echo "${TAG_NAME}" >> VERSION