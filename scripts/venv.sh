#!/bin/bash

printf "\033[0;36m#======   INSTALLATION   =====#\033[0m\n\n"
test1=$(virtualenv --help 2>/dev/null | grep -c "Usage:")
test2=$(python3 --help 2>/dev/null | grep -c "usage:")
if [ "$test1" -eq 1 ] && [ "$test2" -eq 1 ]; then
  if [ ! -d "venv" ]; then
    virtualenv -p python3 venv
  else
    printf "Le venv existe déjà. Pour s'assurer qu'il soit à jour,\nutilisez 'make update'\n"
  fi
  printf "\n\033[0;32m#======      DONE        =====#\033[0m\n"
else
  printf "\033[1;31mErreur\033[0m: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======     FAILED       =====#\033[0m\n"
fi
