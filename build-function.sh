#!/usr/bin/env bash
ZIP_FILE="$(pwd)/TheHive-Webhooks_$(date '+%s').zip"
zip -9 -r "$ZIP_FILE" . \
    -x "venv/*" \
    -x ".vscode/*" \
    -x ".git/*" \
    -x ".gitignore" \
    -x "docker/*" \
    -x "*.sh" \
    -x "*.pyc" \
    -x "*.zip" \
    -x ".DS_Store"
