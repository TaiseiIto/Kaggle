#!/bin/bash

origindir=$(pwd)
cd $(dirname $0)
apt install python3 -y
apt install python3.10-venv -y
apt install pip -y
python3 -m venv kagglenv
source kagglenv/bin/activate
pip install kaggle
cd $origindir

