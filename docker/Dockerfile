FROM python:3.12.0-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    cron \
    && rm -rf /var/lib/apt/lists/*

COPY cron.d/python-job /etc/cron.d/python-job
RUN chmod 0644 /etc/cron.d/python-job
RUN crontab /etc/cron.d/python-job
RUN touch /var/log/cron.log

CMD ["sh", "-c", "cron && tail -f /var/log/cron.log"]
