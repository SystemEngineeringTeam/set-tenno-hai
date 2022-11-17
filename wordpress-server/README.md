# Web

## 問題

A くんは WordPressを使用してブログを書くことにしました．しかし，サーバを準備しcentOSをbootすることはできましたが,その後どのようにして良いかわからず困っています．
横で見ていたあなたはA くんを不憫に思い,代わりに環境構築し,動作確認のためテスト用の記事を投稿してあげることにしました.
なので、あなたはWordPressの環境構築と記事を一つ投稿してください.

## 補足
- WordPressの環境構築には、Apache,PHP,MariaDBを使用してください.
- WordPressは`https://ja.wordpress.org/download/`からwgetすることでダウンロードすることができます.
- wordpress用のデータベースを作成してください.
  `CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8;`
- データベースのユーザー作成し権限を付与してください.
  `GRANT ALL ON wordpress.* TO wordpress@localhost IDENTIFIED BY 'password';` 
  `FLUSH PRIVILEGES;`
- `php-fpm.service`が起動に失敗している場合は`./etc/php-fpm.d/www.conf`をdockerコンテナ内の`/etc/php-fpm.d/www.conf`へコピーしてください.
  その後以下のコマンドで権限を付与してください
  `chown apache:apache /run/php-fpm/www.sock`
- WordPressのページを確認するためには`http://localhost:8000/wordpress`にアクセスしてください．
- 作成する記事にはチーム名もしくは個人名を記載してください.

## コマンド

- `make up`
  - コンテナを起動します．はじめにこれを実行してください．

- `make sh`
  - コンテナ上で bash を起動し，操作できるようにします．

## 採点項目

- apache,php,mariadb,wordPress がインストールされているか？
- `http://localhost:8000/wordpress`にアクセスできるか？
- ユーザーを作成できるか？
- 作成したユーザーでログインできるか？
- 記事を投稿できているか？

## ヒント
https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-ubuntu-20-04-with-a-lamp-stack-ja