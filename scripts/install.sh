#!/bin/bash

printf "\033[0;36m#======      INSTALL      =====#\033[0m\n\n"
test=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
if [ "$test" -eq 1 ]; then
  if [ ! -d "venv" ]
  then
    echo "[Pas de virtualenv trouvé. Utilisation du python3 par défaut]"
    echo "-> Besoin de sudo pour installer (pas de virtualenv)"
    sudo python3 setup.py install --record .install
  else
    echo "[Utilisation du virtualenv]"
    source "venv/bin/activate"
    python3 setup.py install --record .install-venv
  fi
  printf "\n\033[0;32m#======       DONE        =====#\033[0m\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======      FAILED       =====#\033[0m\n"
fi
