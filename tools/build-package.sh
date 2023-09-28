#!/usr/bin/env bash

set -eu

DISTRO_DIR="./dist"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
rm -rf "${DISTRO_DIR:?}"
python -m build -o "${DISTRO_DIR:?}"
