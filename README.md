# mini_product

READMEはQiitaの以下の記事を参考に作成しました(まだ学習段階の小規模なアプリのため、ER図やインフラ構成図などは作ってません)。

→[読みたくなるREADMEを書くためのコツ](https://qiita.com/ren_ichinose/items/15b5a156ae43ea2b3425)


<img width="647" alt="スクリーンショット 2023-09-30 10 42 14" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/709b4b99-45e3-45ea-bbf0-19bbd2173348">


まだ人に使ってもらえる物ではありませんが一応URLも貼っておきます

## <学習の目的>
web開発に必要最低限の技術を学んだ上で、アプリケーションの機能追加からデプロイまでを一通り行いアプリケーション開発の大まかな流れを把握するため。今回は実践djangoという書籍の第１章のコードスニペットアプリ
に自分が追加したい機能をどんどん追加していくやり方で開発を進めました。

## <このアプリを開発した背景>
自分は現在韓国に留学しており、留学生活を送る中で大学での勉強の仕方やアルバイトの情報、visaや海外での就活関連の情報などわからないことを気軽に相談してみんなで解決できるような環境を作りたいと思い開発。
今はまだセキュリティ関連の知識など不足している知識が多すぎる段階なので、毎日少しずつ学習していく中でより多くの人に価値を提供できるサービスを開発できるようになりたい。

## <自分で実装した機能>

機能を追加する上で自分が基本情報技術者を取得したときにお世話になった過去問学習サイトである過去問道場の掲示板を参考にしました。基本的に追加したい機能をネットや書籍で調べて機能を実装していき、エラー等は
chatgptなども活用して解決していきました。

→[過去問道場掲示板](https://www.fe-siken.com/febbs.php)

<hr>

・検索機能

・ページネーション機能

・クラスメソッドでスレッドを更新日でソート

・ログインしないとスレッドを作成したり、閲覧したりできなくする機能

・メッセージフレームワークの実装

・エラーページカスタマイズ

・ログアウトしたらトップページに遷移させる機能

・デザイン全般(フッター作成、ログインしてる時にログアウトボタンの横にユーザ名、背景色など)

あとは管理画面を少し見やすくしたり、モデルを調整したり、ORMを使ってみるなど

## <このアプリ開発のために学習した技術や使用した技術>
gitとgithub, linuxコマンド, sqlとデータベース, python, django, html,css,js, webの仕組み, 基本情報技術者等

*それぞれ書籍や入門教材を使用して学習



## <今後の展望>
開発に必要な要素を一つ一つ学習して、一つのアプリという形でアウトプットしていく過程を通してソフトウェア開発の楽しさや奥深さを実感しました。今後は

・reactを学んでAPI開発

・思いついた機能随時実装

・デプロイや人に使ってもらえるアプリにするためのセキュリティの学習

・機械学習実装

・awsやdocker、githubactionsなども学んで環境構築

・今回学んだgithubやlinuxコマンド,データベースやpython(django)などの基本的な技術を深掘り

・インターンでの実務経験を通した技術力向上

などを目標に学習を継続していこうと思います。



