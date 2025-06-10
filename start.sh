#!/bin/bash

# Print current directory and list files
echo "Current directory: $(pwd)"
echo "Files in current directory:"
ls -la

# Try to find main.py
echo "Searching for main.py:"
find / -name main.py 2>/dev/null

# Make sure we're in the right directory
cd /opt/render/project/src || exit 1

# Install dependencies
pip install -r requirements.txt

# Start the application
python main.py 