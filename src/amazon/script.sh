#!/usr/bin/env bash

# Python virtual environment helpers

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BASE_DIR="${PWD##*/}"
ENV_DIR=".venv"

activate_env() {
  echo "Activate $BASE_DIR"
  deactivate || true
  # shellcheck source=src/script.sh
  source "${ROOT:?}/$ENV_DIR/$BASE_DIR/bin/activate"
}

create_env() {
    echo "create $BASE_DIR Python3 env"
    deactivate || true
    rm -rf "${ROOT:?}/$ENV_DIR" || true
    mkdir -p "${ROOT:?}/$ENV_DIR"
    python3 -m venv "${ROOT:?}/$ENV_DIR/$BASE_DIR" &&
    activate_env &&
    pip install --upgrade pip
}

init() {
    create_env &&
    pip install -r "${ROOT:?}/requirements.dev.txt"
}


alias env:new=create_env
alias env:on=activate_env
alias env:reset=init


# Project helpers

# shellcheck disable=SC2120
test() {
    coverage run -m unittest discover -v "${ROOT:?}/tests"
}

typecheck() {
  cd "${ROOT:?}"
  for submodule in $(find "purplship" -type f -name "__init__.py" -exec dirname {} \;); do
    mypy -p "${submodule//'\/'/.}" || break
  done || break
  cd -
}

check() {
    typecheck && test
}

build() {
    python setup.py bdist_wheel
}

env:on || true
