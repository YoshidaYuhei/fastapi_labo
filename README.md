# fastapi_labo

* React.js で SPA を作成する
* FastApi でバックエンドを作成する
* Solidity で スマートコントラクトを作成する

# memo
* 1file, 1classは守らなくて良い。pythonでは1file, 1moduleなので。
* リクエスト毎に新しいセッションを作成する。そのため、router から渡された Session を使う
* DELETE メソッドなど、Entity に ID のみしかなく、個別のビジネスルールもない場合、Entityにする必要はないものとする。
* 