# 使用する基本イメージ
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY ./app /app

# コマンドでアプリケーションを実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
