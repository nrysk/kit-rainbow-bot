FROM python:3.12.0-slim

# タイムゾーンを日本時間に設定
ENV TZ=Asia/Tokyo
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN echo "Asia/Tokyo" > /etc/timezone

# パッケージのインストール
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# cronのインストール
RUN apt-get update && \
    apt-get install -y cron && \
    rm -rf /var/lib/apt/lists/*


# python-jobをcronに登録し，cronを起動
ENTRYPOINT [ "sh", "-c", " \
    echo 'Bot Started' && \
    chmod 0644 /etc/cron.d/python-job && \
    crontab /etc/cron.d/python-job && \
    touch /var/log/cron.log && \
    cron && \
    tail -f /var/log/cron.log" ]

