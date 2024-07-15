#!/bin/bash

# Check if the tmux session 'myflaskapp' exists and kill it if it does
session_exists=$(tmux list-sessions | grep myflaskapp)
if [ -n "$session_exists" ]; then
    tmux kill-session -t myflaskapp
fi

# Change directory to project folder
cd pe-v2

# Fetch latest changes from main branch
git fetch

# Reset the local repository to the latest changes from the main branch
git reset origin/main --hard

# Activate Python venv and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start new detached Tmux session named 'myflaskapp'
tmux new-session -d -s myflaskapp

# Change directory to project folder within Tmux session
tmux send-keys -t myflaskapp "cd pe-v2" Enter

# Activate Python venv within Tmux session
tmux send-keys -t myflaskapp "source python3-virtualenv/bin/activate" Enter

# Start Flask server within Tmux session
tmux send-keys -t myflaskapp "flask run --host=0.0.0.0" Enter
