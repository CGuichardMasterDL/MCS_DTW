#!/bin/bash

printf "#======   UNINSTALL   =====#\n\n"
if [ -f ".install" ] || [ -f ".install-venv" ]; then
  if [ -f ".install" ]
  then
    echo "-> Besoin de sudo pour uninstall (pas de virtualenv)."
    cat .install | sudo xargs rm -rf
    echo "Uninstall fait."
    rm -f .install
  fi
  if [ -f ".install-venv" ]
    then
    cat .install-venv | xargs rm -rf
    echo "Uninstall fait (venv)."
    rm -f .install-venv
  fi
else
  echo "Aucune installation trouvé."
fi
printf "\n#======     DONE      =====#\n"
