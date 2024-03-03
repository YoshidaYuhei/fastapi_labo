# ベースとなるイメージを指定
FROM node:14

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のファイルをコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm install
RUN npm install --save-dev typescript @types/react @types/react-native @types/jest

# アプリケーションのソースをコピー
COPY . .

# アプリケーションが起動するポートを指定
EXPOSE 3000

# アプリケーションを起動するコマンドを指定
CMD ["npm", "start"]