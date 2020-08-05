#!/usr/bin/env bash
echo "======== Compressing project into single ZIP ========"
NOW=$(date '+%Y.%m.%d-%s')
zip -9 -r "TheHive-Webhooks_$NOW.zip" . \
    -x ".*" \
    -x "venv/*" \
    -x "docker/*" \
    -x "build-*.sh" \
    -x "*__pycache__*" \
    -x "*.pyc" \
    -x "*.zip"