# 埼玉県の一次メッシュコード
今回作成したプログラムは埼玉県を含む一次メッシュ区画を出力するものです
## スタートガイド
・リポジトリ内にあるmesh.pyを作業用ディレクトリにコーピする
```

## システム概要
1. https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html から埼玉県のポリゴン情報を入手する

2. 上記のgeojsonデータを読み込み、その中から埼玉県の県境を表すデータをcoordinates_dicとして取得する

3. 一次メッシュコードの命名規則から、緯度経度からメッシュ区画を求める関数、mesh_countを作成する

4. 2で求めたデータの中に含まれる緯度経度の組み合わせをmesh_countに代入して、各地点のメッシュ区画を求める

5. 4で求めたメッシュ区画を{埼玉県の２文字コード:メッシュ区画}の形式で出力する

