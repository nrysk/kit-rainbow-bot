"""
Description:
    - 虹の塔の絵文字アートを投稿するスクリプト
    - 時々，虹の塔の絵文字アートに異変が起こる

Usage:
    $ python src/main.py
    $ python src/main.py .env

Options:
    --rate <rate>: float = 0.2
        異変が起こる確率
    --remote <url>: str | None = None
        Selenium Grid の URL
        None の場合はローカルで実行
    --env <path>: str = ".env"
        環境変数ファイルへのパス
    --cookie <path>: str = "cookie.pkl"
        クッキーファイルへのパス
    --debug: bool = False
        デバッグの有効化

"""

import argparse
import logging
import os
import sys

import dotenv

from gentext import gen_random_text
from xclient import XClient


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rate", type=float, default=0.2)
    parser.add_argument("--remote", type=str, default=None)
    parser.add_argument("--env", type=str, default=".env")
    parser.add_argument("--cookie", type=str, default="cookie.pkl")
    parser.add_argument("--debug", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    # デバッグの有効化
    if args.debug:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s"
        )

    # 環境変数を読み込む
    dotenv.load_dotenv(args.env)

    # ユーザー名とパスワードを取得
    username = os.getenv("X_USERNAME")
    password = os.getenv("X_PASSWORD")

    if username is None or password is None:
        logging.error("Username or Password is not set.")
        sys.exit(1)

    # クライアントを作成
    logging.debug("Create Client")
    client = XClient()
    client.start(args.remote)
    logging.debug("Client Started")

    # ログイン
    logging.debug("Login")
    client.login(username, password, args.cookie)
    logging.debug("Login Success")

    # テキスト生成
    logging.debug("Generate Text")
    text = gen_random_text(abnormal_rate=args.rate)
    logging.debug("Text Generated")

    # ポスト
    logging.debug("Post")
    client.post(text)
    logging.debug("Post Success")

    # 終了
    logging.debug("Quit")
    client.quit()
    logging.debug("Quit Success")
