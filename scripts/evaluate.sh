#!/bin/bash

if [ ! -d "venv" ]
then
  echo "[Pas de virtualenv trouvé. Utilisation du python3 par défaut]"
else
  echo "[Utilisation du virtualenv]"
  source "venv/bin/activate"
fi

mkdir -p out
mkdir -p out/pylint

printf "\033[0;36m#======   EVALUATION    =====#\033[0m\n\n"
test=$(dpkg-query -W -f='${Status}\n' "pylint3" 2>/dev/null | grep -c "install ok installed")
if [ "$test" -eq 1 ]; then
  for rep in "tests" "mcs_dtw"; do
    mkdir -p "out/pylint/$rep"
    pylint3 "$rep" 2> /dev/null > "out/pylint/$rep/lint.txt"
    pylint3 "$rep" --output-format=json 2> /dev/null > "out/pylint/$rep/lint.json"
    eval=$(tail -n 2 "out/pylint/$rep/lint.txt" | head -1)
    printf -- "- "
    printf "$rep/ :\n  $eval\n"
  done
  printf "\n-> Evaluation finie (résultats dans : 'out/pylint/')\n"
  printf "\n\033[0;32m#======      DONE       =====#\033[0m\n"
else
  printf "\033[1;31mErreur\033[0m: Veuillez installer les paquets nécessaires (voir le README.md).\n"
  printf "\n\033[0;31m#======     FAILED      =====#\033[0m\n"
fi
