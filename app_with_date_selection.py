
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="売上入力アプリ", layout="centered")

st.title("💰 売上入力アプリ（e.m.i BEAUTY SALON）")

DATA_FILE = "sales_data.csv"

# 日付選択
selected_date = st.date_input("📅 日付を選択してください", value=datetime(2024, 11, 11))

# 入力フォーム
with st.form("sales_form"):
    name = st.text_input("🧑‍💼 お客様名")
    course = st.selectbox("📋 コース内容", ["フェイシャル", "ボディー", "脱毛", "ヘッド"])
    amount = st.number_input("💴 金額（円）", min_value=0, step=1000)
    submit = st.form_submit_button("✅ 登録")

if submit:
    new_data = pd.DataFrame([{
        "日付": selected_date.strftime("%Y-%m-%d"),
        "名前": name,
        "コース": course,
        "金額": amount
    }])

    if os.path.exists(DATA_FILE):
        existing = pd.read_csv(DATA_FILE)
        updated = pd.concat([existing, new_data], ignore_index=True)
    else:
        updated = new_data

    updated.to_csv(DATA_FILE, index=False)
    st.success("✅ 売上が登録されました！")

# 売上一覧表示
if os.path.exists(DATA_FILE):
    st.subheader("📊 売上一覧")
    df = pd.read_csv(DATA_FILE)
    st.dataframe(df)
