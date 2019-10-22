#!/bin/bash

if [ ! -d "venv" ]
then
  echo "No virtualenv found. Use of default python3"
else
  echo "Use of virtualenv"
  source "venv/bin/activate"
fi

python3 -mpip install -r requirements/dev.pip
python3 -mpip install -r requirements/install.pip
