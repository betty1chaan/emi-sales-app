
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="売上入力アプリ", layout="centered")
st.title("💰 売上入力フォーム")

# データ保存用の初期化
if "data" not in st.session_state:
    st.session_state.data = []

# 入力フォーム
with st.form("sales_form"):
    st.write("※ 日付は自動で入力されます")
    customer = st.text_input("顧客名")
    menu = st.selectbox("メニュー", ["フェイシャル (F)", "ボディ (B)", "脱毛 (R)", "ヘッド (H)"])
    amount = st.number_input("金額（円）", min_value=0, step=100)
    payment = st.selectbox("支払方法", ["現金", "カード", "未払い"])
    note = st.text_input("備考（任意）")

    submitted = st.form_submit_button("✅ 登録する")
    if submitted:
        st.session_state.data.append({
            "日付": date.today().strftime("%Y/%m/%d"),
            "顧客名": customer,
            "メニュー": menu,
            "金額": amount,
            "支払方法": payment,
            "備考": note
        })
        st.success("登録しました！")

# 入力済データ表示
df = pd.DataFrame(st.session_state.data)
if not df.empty:
    st.markdown("### 📋 入力履歴")
    st.dataframe(df)

    st.markdown("### 📊 メニュー別売上")
    st.bar_chart(df.groupby("メニュー")["金額"].sum())
