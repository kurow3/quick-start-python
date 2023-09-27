#!/usr/bin/env bash

set -eu

MODULE="example_package"
SOURCE_DIR="./src"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
export PYTHONPATH="${SOURCE_DIR:?}${PYTHONPATH:+":"}${PYTHONPATH:-""}"
python -m "${MODULE:?}" "${@}"
