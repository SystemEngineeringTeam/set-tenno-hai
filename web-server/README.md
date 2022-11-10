# Web

## 問題

A くんは HTML で自分のホームページを作成しました．しかし，そのページはまだ公開されていません．
あなたは，Apache を使って A くんのホームページを見られるようにしてください．

## 補足

- ページを確認するためには`http://localhost:8080`にアクセスしてください．
- `http://localhost:8080`にアクセスしたときに，`/files/homepage.html` と同じページが表示されるようにしてください．
- `./files/homepage.html`は docker コンテナ内の`/files/homepage.html`と同じものです．

## コマンド

- `make up`

  - コンテナを起動します．はじめにこれを実行してください．

- `make sh`
  - コンテナ上で bash を起動し，操作できるようにします．

- `make down`
  - コンテナを停止します．

## 採点項目

- apache がインストールされているか？
- 設定ファイルは適切に記述されているか？
- アクセスしたときに表示されるファイルは変更されているか？

## ヒント
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04-ja
