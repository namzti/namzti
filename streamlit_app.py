# Streamlitライブラリをインポート
import streamlit as st
import random 


# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('はっぴくみんだーれだ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 今日はどのピクミンをおつかいに行かせますか？🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示


pikuminns=['黄ピクミン','赤ピクミン','青ピクミン','岩ピクミン','羽ピクミン']
results= random.choice(pikuminns)

if st.button('ピクミンを選ぶ'):
    st.header(results)


