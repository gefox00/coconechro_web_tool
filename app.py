import streamlit as st
import requests
import pyperclip
from PC_Converter_for_web_class import Nccatcher

st.title('ココネクフォーマット')

st.text_input(label='変換したいキャラシのURLを入力', key='-input-')
st.write('このツールはキャラクター保管所（下記URLのサイト）の')
st.write('ネクロニカのキャラクターをココフォリアの駒に変換するためのツールです')
st.write('https://charasheet.vampire-blood.net/')
st.write('サンプルキャラクター\n　しかばねソロリティ　　　　https://charasheet.vampire-blood.net/4634412'
         '\n　ひきがねコート　　　　https://charasheet.vampire-blood.net/4634377'
         '\n　つぎはぎアリス　　　　https://charasheet.vampire-blood.net/4634334'
         '\n　きぐるいジャンク　　　https://charasheet.vampire-blood.net/2116483'
         '\n　すてねこオートマトン　https://charasheet.vampire-blood.net/2116446'
         '\n')
st.write('')
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

        st.write('変換結果を表示します以下の文字列をコピーしてココフォリアに張り付けてください\n'
                 'テキストボックス右端にカーソルを合わせるとコピーボタンが表示されます。')
        st.code(clip, 'json')




