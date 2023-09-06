#!/usr/bin/env bash

workers_cnt=$(( $(nproc) * 2 + 1 ))

gunicorn --bind 0.0.0.0:7777 -w "$workers_cnt" -k uvicorn.workers.UvicornWorker presentation.main:create_app
