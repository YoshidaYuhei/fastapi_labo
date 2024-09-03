# fastapi_labo

* React.js で SPA を作成する
* FastApi でバックエンドを作成する
* Solidity で スマートコントラクトを作成する

# memo
* 1file, 1classは守らなくて良い。pythonでは1file, 1moduleなので。
* リクエスト毎に新しいセッションを作成する。そのため、router から渡された Session を使う
* DELETE メソッドなど、Entity に ID のみしかなく、個別のビジネスルールもない場合、Entityにする必要はないものとする。
* __init__.pyにたくさん書きたくないので、from import の際は トップレベルディレクトリ(app.)から書く
* OpenAPIのどこかに、どの画面でどのように利用されるかを書いといてもいい
  * フロントやディレクターは画面とAPIの対応関係をドキュメント管理すべき。それ無しで結合テストの項目書作れって、しんどいやん。
* ドメインオブジェクトは入力(IN)、出力(OUT)、DBへの入力(DBIN)に分ける
  * INとOUTはドメイン層だが、DBINはインフラ層。だがファイルは分けなくてよい
* 
develop追加
