FROM node:current-slim as base

WORKDIR /tmp
RUN npm install -g pnpm

WORKDIR /home/node/app
COPY pnpm-lock.yaml ./
RUN pnpm fetch --dev

ADD . ./
RUN pnpm install -r

FROM base as production

ENV NODE_PATH=./build

RUN pnpm run build