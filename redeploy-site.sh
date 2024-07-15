#!/bin/bash

# change directory to project folder
cd pe-portfolio

# fetch latest changes from main branch
git fetch

# reset the local repository to the latest changes from the main branch
git reset origin/main --hard

# activate Python venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# restart portfolio service
sudo systemctl daemon-reload
sudo systemctl restart myportfolio
