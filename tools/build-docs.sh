#!/usr/bin/env bash

set -eu

DOCS_TYPE="html"
DOCS_DIR="./docs"
DOCSOURCE_DIR="./docs/src"
SOURCE_DIR="./src"

SCRIPT_DIR="$(cd $(dirname ${0}); pwd)"
PROJECT_DIR="$(dirname ${SCRIPT_DIR})"

cd "${PROJECT_DIR}"
export PYTHONPATH="${SOURCE_DIR:?}:${DOCSOURCE_DIR:?}${PYTHONPATH:+":"}${PYTHONPATH:-""}"
rm -rf "${DOCS_DIR:?}/${DOCS_TYPE:?}"
sphinx-build -a -b "${DOCS_TYPE:?}" "${DOCSOURCE_DIR:?}" "${DOCS_DIR:?}/${DOCS_TYPE:?}"
