#!/bin/bash

printf "\033[0;36m#======     UPDATE       =====#\033[0m\n\n"
test=$(python3 --help 2>/dev/null | grep -c "usage:")
if [ "$test" -eq 1 ]; then
  python3 setup.py sdist bdist_wheel
  printf "\n\033[0;32m#======      DONE       =====#\033[0m\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======     FAILED      =====#\033[0m\n"
fi
