#!/bin/bash



/usr/local/bin/python /app/src/main.py \
    --env /app/.env \
    --remote "http://chrome:4444/wd/hub" \
    --cookie /app/cache/cookies.pkl \
    --debug