"""

🍀 当ファイルは、main ページ用のPythonコードファイル
 
   
   🔷🔶当ファイルでは、画面上に以下の内容を表示する 🔷🔶
      
      1, タイトル    
      2, キャプション
      3, 画像
   
 
""" 

# ====================================================================
# ライブラリをインポート
#
#  import ▲▲▲▲ : --------------> これはモジュール全体をインポートするときに使う
#
#   例）import math
#       こうすると、math モジュール内の全ての関数を使うことができる
#
#  from ●●●●  import ▲▲▲▲ : ---> これは特定の関数やクラスだけをインポートしたいときに使う
#
#   例）from math import sqrt
#      こうすると、math モジュールから、sqrt 関数だけをインポートできて、
# 　　　コードの中でそのまま sqrt() として使える
#
# ====================================================================
import streamlit as st              # Streamlitライブラリをインポート
from PIL import Image               # PILライブラリのImageモジュール（画像処理用）をインポート



# -----------------------------------------------
#  🚀 Webが画面上に「タイトル」を表示
# -----------------------------------------------
st.title('おじいちゃんアプリ')


# -----------------------------------------------
#  🚀 Webが画面上に「キャプション」を表示
# -----------------------------------------------
st.caption('これらはおじいちゃんの動画用のテストアプリです')


# -----------------------------------------------
#  🚀 Webが画面上に「画像」を表示
#  
#  🔶準備🔶
#     ・pillow ライブラリが必要なのでインストール
#   
#  👉ポイント
#     ・OpenCVライブラリで読み込んだ「ndarrayオブジェクト」も扱える
#       但し、OpenCVを使う場合、CVTカラーを使って色変換が必要となる
#     ・ネット上の画像・動画を埋め込みたい場合は「画像のURL」を文字列で指定できる
#
#
#  🔶注意🔶
#     ・この画像部分はサプー動画と異なるがこのコードの方がシンプル
#   
# -----------------------------------------------

# >>> 画像 <<<
#
#     🔴重要🔴
#        ・このファイルは、main_app6.py から呼び出されるので
#          ファイルは main_app6.pyから見た相対パスで指定する

image = Image.open('./data/メインクーン01.jpg')       # Imageのopen()メソッドを呼び出して、引数に「画像ファイル」を渡す
st.image(image, width=200)                           # st.image()メソッドの引数に「画像サイズ」を渡す
