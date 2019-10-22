#!/bin/bash

if [ ! -d "venv" ]
then
  echo "No virtualenv found. Use of default python3"
else
  echo "Use of virtualenv"
  source "venv/bin/activate"
fi

python3 -m nose tests
rm -f tests/*.pyc
