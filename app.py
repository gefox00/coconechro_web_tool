import streamlit as st
import requests
import pyperclip
from PC_Converter_for_web_class import Nccatcher

st.title('ココネクフォーマット')

st.text_input(label='変換したいキャラシのURLを入力', key='-input-')
st.write('このツールはキャラクター保管所（下記URLのサイト）の')
st.write('ネクロニカのキャラクターをココフォリアの駒に変換するためのツールです')
st.write('https://charasheet.vampire-blood.net/')
# セッションのコンポーネントのアクセスを簡略化
asset = st.session_state

get_button = st.button(label='変換', key='-convert-')
# イベント処理
if get_button and len(asset['-input-']) > 0:
    target = asset['-input-'] + '.js'
    target_json = requests.get(target).json()
    if 'https://charasheet.vampire-blood.net' in target and target_json['game'] == 'nechro':
        convert = Nccatcher(target_json)
        clip = str(convert.ch_data_js).replace('\'', '"')
        st.text_area(clip)
        st.write('変換結果を表示します以下の文字列をコピーしてココフォリアに張り付けてください')
        st.text_area(clip)




