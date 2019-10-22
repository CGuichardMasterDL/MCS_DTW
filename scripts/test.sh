#!/bin/bash

if [ ! -d "venv" ]
then
  echo "[Pas de virtualenv trouvé. Utilisation du python3 par défaut]"
else
  echo "[Utilisation du virtualenv]"
  source "venv/bin/activate"
fi
printf "#======      TEST      =====#\n\n"
test1=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
test2=$(python3 -mnose --help 2> /dev/null)
if [ "$test1" -eq 1 ] && [ -n "$test2" ]; then
  python3 -m nose tests
  rm -f tests/*.pyc
  printf "\n#======      DONE      =====#\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n#======     FAILED     =====#\n"
fi
