#!/usr/bin/env bash

set -eu

TEST_DIR="./tests"
SOURCE_DIR="./src"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
python -m pytest
