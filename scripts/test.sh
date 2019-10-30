#!/bin/bash

if [ ! -d "venv" ]
then
  echo "[Pas de virtualenv trouvé. Utilisation du python3 par défaut]"
else
  echo "[Utilisation du virtualenv]"
  source "venv/bin/activate"
fi
printf "\033[0;36m#======      TEST      =====#\033[0m\n\n"
test1=$(python3 --help 2>/dev/null | grep -c "usage:")
test2=$(python3 -mnose --help 2> /dev/null)
if [ "$test1" -eq 1 ] && [ -n "$test2" ]; then
  python3 -m nose tests
  rm -f tests/*.pyc
  printf "\n\033[0;32m#======      DONE      =====#\033[0m\n"
else
  printf "\033[1;31mErreur\033[0m: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======     FAILED     =====#\033[0m\n"
fi
