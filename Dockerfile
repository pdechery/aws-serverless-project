FROM node:20

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

WORKDIR /app

COPY package.json /app/

RUN apt-get update && apt-get install -y python3-pip
RUN npm i -g serverless@3
RUN npm install

ENTRYPOINT ["tail", "/dev/null"]