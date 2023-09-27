#!/usr/bin/env bash

set -eu

MODULE="example_package"
LISTEN_ADDR="127.0.0.1"
LISTEN_PORT=5678
SOURCE_DIR="./src"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
export PYTHONPATH="${SOURCE_DIR:?}${PYTHONPATH:+":"}${PYTHONPATH:-""}"
python -m debugpy --listen "${LISTEN_ADDR:?}:${LISTEN_PORT:?}" --wait-for-client -m "${MODULE:?}" "${@}"
