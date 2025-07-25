
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="売上登録フォーム", layout="centered")

st.title("💰 売上登録フォーム")

# ✅ 表示の変更：カレンダー選択であることを明示
st.markdown("※ 日付はカレンダーから選択できます")

# 日付選択
selected_date = st.date_input("📅 日付を選択してください", value=datetime(2024, 11, 11))

# 入力フォーム
with st.form("sales_form"):
    customer_name = st.text_input("顧客名")
    menu = st.selectbox("メニュー", ["フェイシャル (F)", "ボディー (B)", "脱毛 (R)", "ヘッド (H)"])
    price = st.number_input("金額（円）", min_value=0, step=1)
    payment_method = st.selectbox("支払方法", ["現金", "クレジットカード", "電子マネー", "その他"])
    remarks = st.text_area("備考（任意）")

    submit = st.form_submit_button("✅ 登録する")

    if submit:
        new_data = pd.DataFrame({
            "日付": [selected_date.strftime("%Y-%m-%d")],
            "顧客名": [customer_name],
            "メニュー": [menu],
            "金額": [price],
            "支払方法": [payment_method],
            "備考": [remarks]
        })

        try:
            existing_data = pd.read_csv("sales_data.csv")
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        except FileNotFoundError:
            updated_data = new_data

        updated_data.to_csv("sales_data.csv", index=False)
        st.success("✅ 売上が登録されました！")
