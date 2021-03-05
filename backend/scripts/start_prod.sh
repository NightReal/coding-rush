#!/usr/bin/env bash


gunicorn main:backend_app -b 0.0.0.0:8000 -w 4 --worker-class aiohttp.GunicornUVLoopWebWorker --access-logfile -