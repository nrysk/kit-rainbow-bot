import os
import pickle as pkl
import sys

import dotenv

from gentext import gen_random_text
from xclient import XClient

if __name__ == "__main__":
    # 環境変数を読み込む
    if len(sys.argv) > 1:
        print(f"Loading .env file: {sys.argv[1]}", file=sys.stderr)
        dotenv.load_dotenv(sys.argv[1])
    else:
        print("Loading .env file: .env", file=sys.stderr)
        dotenv.load_dotenv(".env")

    # ユーザー名とパスワードを取得
    username = os.getenv("X_USERNAME")
    password = os.getenv("X_PASSWORD")

    if username is None or password is None:
        print("Set X_USERNAME and X_PASSWORD in .env file")
        sys.exit(1)

    # クライアントを作成
    client = XClient()

    print("Start Client...", file=sys.stderr)
    client.start()

    # ログイン
    print("Login...", file=sys.stderr)
    client.login(username, password)

    # テキスト生成
    print("Generate Text...", file=sys.stderr)
    text = gen_random_text(0.25)

    # ポスト
    print("Post...", file=sys.stderr)
    client.post(text)

    # 終了
    print("Quit...", file=sys.stderr)
    client.quit()
