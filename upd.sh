#!/usr/bin/env bash

git submodule init
git submodule update --remote
docker exec -it backend python3 manage.py import_codes
