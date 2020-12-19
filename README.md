# 音声分析の勉強

## 目的

Pythonによる音声分析の勉強。

下記プロジェクトのための勉強や調査のためのリポジトリ。

https://github.com/conf8o/speech-bubble-recognition

## 目標

Jypter Notebook、各種ライブラリを使って音声データを加工し、保存する。

音声の特徴とかが出るようなデータになれば最高。

## フォルダ構成

requirements.txtは根に置いて随時必要なライブラリを更新していく。(インストールするときは`pip install -r requirements.txt`)

時系列順に勉強内容を振り返りたいので一区切りするごとに日付でフォルダを切っていく。

### 日付フォルダ

日付フォルダ内のREADME.mdに目標を書く。

日付フォルダ内では取り組み内容ごとにフォルダを切っていく。

以下の観点で日付フォルダの目標は修正しても良い。

* 達成するのが能力的に厳しい
* 達成までに時間がかかりそう(2, 3週間必要とか)
* やっていることは大事だが、目標からやや逸れている

## ブランチとマージ

日付フォルダでの取り組みごとにブランチを切り、何か大きめなことをした段階でプルリクエストを行い、スカッシュでマージする。

マージしたブランチは削除する。

## ノートやソース

Jupyter Notebook は HTML に変換し、外だししたPythonコードと一緒にまとめる。

* Website: https://conf8o.github.io/studying-speech-analysis

2020-12-17より、ライブラリとして使えるソースは"speelysis"(https://github.com/conf8o/speelysis )にまとめる。

### 変換ツール

* https://github.com/conf8o/clj-nbconvert
* https://github.com/conf8o/notebook

## 参考書籍

* 概念を大切にする微積分―1変数
* 行列プログラマー: Pythonプログラムで学ぶ線形代数
* 解析学概論
* 音声認識 (機械学習プロフェッショナルシリーズ) 
* Pythonではじめる教師なし学習――機械学習の可能性を広げるラベルなしデータの利用
