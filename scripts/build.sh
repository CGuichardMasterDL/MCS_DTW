#!/bin/bash

printf "#======      BUILD      =====#\n\n"
test=$(dpkg-query -W -f='${Status}\n' "python3" 2>/dev/null | grep -c "install ok installed")
if [ "$test" -eq 1 ]; then
  python3 setup.py build
  printf "\n#======      DONE       =====#\n"
else
  printf "Erreur: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n#======     FAILED      =====#\n"
fi
