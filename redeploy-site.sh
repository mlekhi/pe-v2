#!/bin/bash

# kill all existing tmux sessions
tmux kill-session -a

# change directory to project folder
cd pe-portfolio

# fetch latest changes from main branch
git fetch

# Step 4: Reset the local repository to the latest changes from the main branch
git reset origin/main --hard

# activate Python venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# start new detached Tmux session
tmux new-session -d -s myflaskapp

# change directory to project folder within Tmux session
tmux send-keys -t myflaskapp "cd pe portfolio" Enter

# activate Python venv within Tmux session
tmux send-keys -t myflaskapp "source python3-virtualenv/bin/activate" Enter

# start Flask server within Tmux session
tmux send-keys -t myflaskapp "python app.py" Enter
