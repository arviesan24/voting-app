web: PYTHONUNBUFFERED=1 python -Wall manage.py runserver 127.0.0.1:$PORT
mailhog: bash -c 'if [[ ! $(pgrep mailhog) ]]; then mailhog; else while true; do sleep 99999; done; fi'
