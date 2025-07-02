#!/bin/bash

# Path to project.
PROJECT_DIR="/opt/ollama-chat"

# Path to venv.
VENV_DIR="$PROJECT_DIR/.venv"

# Path to script.
PYTHON_SCRIPT="$PROJECT_DIR/ollama_chat.py"

# Activate venv.
source "$VENV_DIR/bin/activate"

# Run script.
python3 "$PYTHON_SCRIPT"

# Terminate venv instance.
deactivate
