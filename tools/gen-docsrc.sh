#!/usr/bin/env bash

set -eu

DOCS_PROJECT="example_package"
DOCS_AUTHOR="Example Author"
DOCS_VER="0.0.1"
DOCSOURCE_DIR="./docs/src"
SOURCE_DIR="./src"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
export PYTHONPATH="${SOURCE_DIR:?}:${DOCSOURCE_DIR:?}${PYTHONPATH:+":"}${PYTHONPATH:-""}"
sphinx-apidoc -FMef -H "${DOCS_PROJECT}" -A "${DOCS_AUTHOR}" -V "${DOCS_VER}" -o "${DOCSOURCE_DIR:?}" "${SOURCE_DIR:?}"
rm -rf "${DOCSOURCE_DIR:?}/_build"
