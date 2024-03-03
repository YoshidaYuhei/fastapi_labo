## 概要
* ログイン
  * 入力されたパスワードを検証すること
    * 一致しない場合 401 エラー
  * 入力されたEmailをもとにアクセストークンとリフレッシュトークンを生成して返すこと

* サインアップ
  * email と password から User レコードを作成する
  * passsword は encrypt して保存する

* get_current_user
  * Depends を使って各Routerに渡す
  * リクエストヘッダの access_token を取得して jwt.decode で User レコードを取得する

* 備考
  * Auth で Pydantic は使わない。
  * Body() でリクエストボディで処理する
## エンドポイント

* `post '/auth/login`
* `post '/auth/signup`
* ログアウトはいくつか方法があるが、いちばん簡単なのはフロントでトークンを破棄すること。
サーバー側でJWTトークンを直接無効化する方法はない。

## 勉強ログ
* jwt.encodeはユーザー情報と秘密鍵を下にTokenを生成すること
* jwt.decodeはTokenと秘密鍵からユーザー情報を取得すること
* get_current_user とは jwt.decode でユーザー情報を取得すること

* トークンを受け取ったフロントはトップ画面に遷移する
以降、フロントはトークンをヘッダに入れてリクエストを投げる。バックエンドはAPIを処理する度にトークンの検証を行い、認証すれば後続の処理が行われ、レスポンスを返す。

