#!/usr/bin/env bash

set -o errexit

TOOLS_PATH="$(dirname $0)"

pipenv run python "${TOOLS_PATH}/../manage.py" runserver
