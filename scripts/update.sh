#!/bin/bash

printf "#======     UPDATE       =====#\n\n"
test=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
if [ "$test" -eq 1 ]; then
  if [ ! -d "venv" ]
  then
    echo "[Pas de virtualenv trouvé. Utilisation du python3 par défaut]"
    echo "-> Besoin de sudo pour installer (pas de virtualenv)"
    sudo python3 -mpip install -r requirements/dev.pip
    sudo python3 -mpip install -r requirements/install.pip
  else
    echo "[Utilisation du virtualenv]"
    source "venv/bin/activate"
    python3 -mpip install -r requirements/dev.pip
    python3 -mpip install -r requirements/install.pip
  fi
  printf "\n#======      DONE        =====#\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n#======     FAILED       =====#\n"
fi
