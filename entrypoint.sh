#!/usr/bin/env bash
set -e
if [ ! -f container_setup_completed ]; then
  PYTHONPATH=. python /app/docker/install_mods.py
  touch container_setup_completed
fi

exec python -m tgpy
