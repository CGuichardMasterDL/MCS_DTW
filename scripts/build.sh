#!/bin/bash

printf "\033[0;36m#======      BUILD      =====#\033[0m\n\n"
test=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
if [ "$test" -eq 1 ]; then
  python3 setup.py build
  printf "\n\033[0;32m#======      DONE       =====#\033[0m\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======     FAILED      =====#\033[0m\n"
fi
