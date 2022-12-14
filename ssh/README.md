# SSH

## 問題

シス研ではこの度，新しいサーバを購入しました．
いちいちモニターをつないで操作するのは面倒なので，SSH で操作できるようにしてください．ただし，セキュリティのため，パスワード認証はオフにして公開鍵認証でアクセスできるようにしてください．

## 補足

- ubuntu 内の SSH サーバのポートは変更しないでください．
- docker-compose upするとubuntu/etc/sshに鍵(RSA,ECDSA など)が共有されますが、今回はこちらは使用しません。
- そのため自ら鍵を作成してください、鍵の種類は問いません(RSA,ECDSA など)．
- 確認の際には，`localhost`の 22222 番ポートに対して SSH で接続してください．
- 接続するユーザは`root`です．

## コマンド

- `make up`

  - コンテナを起動します．はじめにこれを実行してください．

- `make sh`
  - コンテナ上で bash を起動し，操作できるようにします．

- `make down`
  - コンテナを停止します．

- `pytohn3 test.py`
  - コンテナ上でテストを実行します．

## 採点項目

- パスワード認証はオフになっているか？
- 公開鍵認証でアクセスできるか？

## ヒント
https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-ja