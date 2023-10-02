# mini_product

READMEはQiitaの以下の記事を参考に作成しました(まだ学習段階の小規模なアプリのため、ER図やインフラ構成図などは作ってません)。

→[読みたくなるREADMEを書くためのコツ](https://qiita.com/ren_ichinose/items/15b5a156ae43ea2b3425)


<img width="647" alt="スクリーンショット 2023-09-30 10 42 14" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/709b4b99-45e3-45ea-bbf0-19bbd2173348">


まだ人に使ってもらえる物ではありませんが一応URLも貼っておきます。といきたいことろなのですが現在初めてのデプロイに手こずってます(pythonanywhereとrenderで挑戦中)。代わりにREADMEの1番下で画面遷移図的なのを貼っておきます。


## <学習の目的>
web開発に必要最低限の技術を学んだ上で、アプリケーションの機能追加からデプロイまでを一通り行いアプリケーション開発の大まかな流れを把握するため。今回は実践djangoという書籍の第１章のコードスニペットアプリ
に自分が追加したい機能をどんどん追加していくやり方で開発を進めました。

## <このアプリを開発した背景>
自分は現在韓国に留学しており、留学生活を送る中で大学での勉強の仕方やアルバイトの情報、visaや海外での就活関連の情報などわからないことを気軽に相談してみんなで解決できるような環境を作ってみたいと思い開発。
今はまだセキュリティ関連の知識など不足しているものが多すぎる段階なので、毎日少しずつ学習していく中で多くの人に価値を提供できるサービスを開発できるようになりたい。

## <自分で実装した機能>

機能を追加する上で自分が基本情報技術者を取得したときにお世話になった過去問学習サイトである過去問道場の掲示板を参考にしました。基本的に追加したい機能をネットや書籍で調べて機能を実装していき、エラー等は
chatgptなども活用して解決していきました。

→[過去問道場掲示板](https://www.fe-siken.com/febbs.php)

<hr>

・検索機能

・ページネーション機能

・クラスメソッドでスレッドを更新日でソート

・ログインしないとスレッドを作成したり、閲覧したりできなくする機能

・メッセージフレームワークの実装 + javascriptで5秒後に表示が消えるように実装

・エラーページカスタマイズ

・ログアウトしたらトップページに遷移させる機能

・デザイン全般(フッター作成、ログインしてる時にログアウトボタンの横にユーザ名、背景色など)

あとは管理画面を少し見やすくしたり、モデルを調整したり、ORMを使ってみるなど

## <このアプリ開発のために学習した技術や使用した技術>
gitとgithub, linuxコマンド, sqlとデータベース, python, django, html,css,js, webの仕組み, 基本情報技術者(基本的なコンピュータサイエンス習得のため)等

*それぞれ書籍や入門教材を使用して学習



## <今後の展望>
開発に必要な要素を一つ一つ学習して一つのアプリという形でアウトプットしていく過程を通してソフトウェア開発の面白さを実感できた。また学習すればするほどそれに派生して学ぶべき内容が増えていき、ソフトウェア開発の奥深さや継続して学習することの重要性も感じることができた。
アプリ開発はプログラミング以外にも重要なことがたくさんあるんだなーと気づいた。今後は

・reactを学んでAPI開発

・思いついた機能随時実装

・デプロイや人に使ってもらえるアプリにするためのセキュリティの学習

・機械学習実装

・awsやdocker、githubactionsなども学んで環境構築

・今回学んだgithubやlinuxコマンド,データベースやpython(django)などの基本的な技術を深掘り

・インターンでの実務経験を通した技術力向上


などを目標に学習を継続していこう思う。



<img width="1675" alt="スクリーンショット 2023-10-02 10 39 11" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/8b567c77-d181-4d13-9779-d4a5df4894ce">

<img width="1677" alt="スクリーンショット 2023-10-01 23 42 00" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/1ce6aff7-d15b-41bf-a06b-82bbd6adc769">

<img width="1663" alt="スクリーンショット 2023-10-01 23 41 40" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/13386307-c601-47c0-a388-06ba8a134a23">

<img width="1661" alt="スクリーンショット 2023-10-01 23 41 26" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/5b3ba50e-e9a7-4b54-b383-c55cfcc4308c">

<img width="1658" alt="スクリーンショット 2023-10-01 23 42 29" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/b5f5b8d7-3dd6-46e6-9a81-3fdf0c03fa48">

<img width="1678" alt="スクリーンショット 2023-10-01 23 42 41" src="https://github.com/hirohiro-sys/mini_product/assets/126783940/0829525d-91d5-4976-a3d8-8682cba0c869">

シンプルすぎか
