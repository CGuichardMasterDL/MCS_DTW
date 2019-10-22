#!/bin/bash

printf "#======   INSTALLATION   =====#\n\n"
test1=$(dpkg-query -W -f='${Status}\n' "virtualenv" 2>/dev/null | grep -c "install ok installed")
test2=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
if [ "$test1" -eq 1 ] && [ "$test2" -eq 1 ]; then
  if [ ! -d "venv" ]; then
    virtualenv -p python3 venv
  else
    printf "Le venv existe déjà. Pour s'assurer qu'il soit à jour,\nutilisez 'make update'\n"
  fi
  printf "\n#======      DONE        =====#\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n#======     FAILED       =====#\n"
fi
