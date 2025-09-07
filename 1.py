import streamlit as st
import random 

st.title("ダメージ計算アプリ")

def tipe_check():

    if defense_type in type_dict[attack_type]["抜群"]:
        st.session_state.power *= 2
        if defense_type2 in type_dict[attack_type]["抜群"]:
            st.session_state.power *= 2
        elif defense_type2 in type_dict[attack_type]["半減"]:
            st.session_state.power /= 2
        elif defense_type2 in type_dict[attack_type]["無効"]:
            st.session_state.power = 0
        else :
            st.session_state.power *= 1
    elif defense_type in type_dict[attack_type]["半減"]:
        st.session_state.power /= 2
        if defense_type2 in type_dict[attack_type]["半減"]:
            st.session_state.power /= 2
        elif defense_type2 in type_dict[attack_type]["抜群"]:
            st.session_state.power *= 2
        elif defense_type in type_dict[attack_type]["無効"]:
            st.session_state.power = 0
        else :
            st.session_state.power *= 1
    elif defense_type in type_dict[attack_type]["無効"]:
        st.session_state.power = 0
    elif defense_type2 in type_dict[attack_type]["無効"]:
        st.session_state.power = 0
    else :
        st.session_state.power *= 1

def damage():
    c = waza_attack
    if attack_type == attack_type2:
        c *= 1.5
    else :
        c *= 0.85
    a = random.uniform(0.85,1) 
    attack_damage = ((50 * 2 / 5 + 2) * c * st.session_state.power  * damege/ defense / 50 + 2) * a
    return attack_damage
defense_type = st.selectbox(
    "防御側のタイプ1",
    ["ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく","じめん","ひこう","エスパー","むし","いわ","ゴースト","ドラゴン","あく","はがね","フェアリー"]
)
defense_type2= st.selectbox(
    "防御側のタイプ2",
    ["なし","ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく","じめん","ひこう","エスパー","むし","いわ","ゴースト","ドラゴン","あく","はがね","フェアリー"]
)

attack_type = st.selectbox(
    "技のタイプ",
    ["ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく","じめん","ひこう","エスパー","むし","いわ","ゴースト","ドラゴン","あく","はがね","フェアリー"]
)
attack_type2= st.selectbox(
    "攻撃側のタイプ",
    ["ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく","じめん","ひこう","エスパー","むし","いわ","ゴースト","ドラゴン","あく","はがね","フェアリー"]
)

waza_attack = st.slider(
    "技の威力",
    0, 200
)
if 'power' not in st.session_state: 
    st.session_state.power = 1
damege = st.slider(
    "攻撃種族値を選択",
    0,210
)
defense = st.slider(
    "防御種族値を選択",
    0,210
)
type_dict={ "ノーマル":{"抜群":[],"半減":["いわ","はがね"],"無効":["ゴースト"]},
            "ほのお":{"抜群":["くさ","こおり","むし","はがね"],"半減":["ほのお","みず","いわ","ドラゴン"],"無効":[]},
            "みず":{"抜群":["ほのお","じめん","いわ"],"半減":["みず","くさ","ドラゴン"],"無効":[]},
            "でんき":{"抜群":["みず","ひこう"],"半減":["でんき","くさ","ドラゴン"],"無効":["じめん"]},
            "くさ":{"抜群":["みず","じめん","いわ"],"半減":["ほのお","くさ","どく","ひこう","むし","ドラゴン","はがね"],"無効":[]},
            "こおり":{"抜群":["くさ","じめん","ひこう","ドラゴン"],"半減":["こおり","みず","こおり","はがね"],"無効":[]},
            "かくとう":{"抜群":["ノーマル","こおり","いわ","あく","はがね"],"半減":["どく","ひこう","エスパー","むし","フェアリー"],"無効":["ゴースト"]},
            "どく":{"抜群":["くさ","フェアリー"],"半減":["どく","じめん","いわ","ゴースト"],"無効":["はがね"]},
            "じめん":{"抜群":["ほのお","でんき","どく","いわ"],"半減":["くさ","むし",],"無効":["ひこう"]},
            "ひこう":{"抜群":["くさ","かくとう","むし"],"半減":["でんき","いわ","はがね"],"無効":[]},
            "エスパー":{"抜群":["かくとう","どく"],"半減":["エスパー","はがね"],"無効":["あく"]},
            "むし":{"抜群":["くさ","エスパー","あく"],"半減":["ほのお","かくとう","どく","ひこう","ゴースト","はがね","フェアリー"],"無効":[]},
            "いわ":{"抜群":["ほのお","こおり","ひこう","むし"],"半減":["かくとう","じめん","はがね"],"無効":[]},
            "ゴースト":{"抜群":["エスパー","ゴースト"],"半減":["あく"],"無効":["ノーマル"]},
            "ドラゴン":{"抜群":["ドラゴン"],"半減":["はがね"],"無効":["フェアリー"]},
            "あく":{"抜群":["エスパー","ゴースト"],"半減":["かくとう","あく","フェアリー"],"無効":[]},
            "はがね":{"抜群":["こおり","いわ","フェアリー"],"半減":["ほのお","みず","でんき","はがね"],"無効":[]},
            "フェアリー":{"抜群":["どく","ドラゴン","あく"],"半減":["ほのお","どく","はがね"],"無効":[]}}

if st.button("結果"):
    tipe_check()
    b = damage()
    st.write(b)