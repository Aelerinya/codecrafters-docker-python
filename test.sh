#!/bin/sh
docker build -t mydocker . && docker run --cap-add="SYS_ADMIN" mydocker "$@"