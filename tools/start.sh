#!/usr/bin/env bash

set -o errexit

TOOLS_PATH="$(dirname $0)"

export DEBUG=True

pipenv run python "${TOOLS_PATH}/../manage.py" runserver
