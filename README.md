requirements.txtについて
ここに現在の環境に入っているパッケージライブラリの一覧を取得します。具体的には、ターミナルで以下のコマンドを実行しましょう。

py -m pip freeze > requirements.txt

これでプロジェクト内にrequirements.txtが生成されるはずなので、これをGitHub上に上げます。


一括インストール
requirements.txtが入ったプロジェクトを保存するだけではパッケージライブラリはまだ仮想環境において使える状態にはありません。それをインストールするためには以下のコマンドをターミナルで実行する必要があります。

py -m pip install -r requirements.txt

これで、パッケージライブラリの共有は完了となります。
