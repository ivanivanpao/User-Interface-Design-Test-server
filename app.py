import streamlit as st

st.title("課程回饋表單")

# 用 st.form 包起來，所有欄位會在按下送出時才一起送出
with st.form("feedback_form"):
    name = st.text_input("姓名")
    department = st.selectbox("科系", ["資訊工程系", "電子工程系", "其他"])
    # 滿意度由高到低：夯 > 頂級 > 人上人 > NPC > 拉完了
    satisfaction = st.radio(
        "課程滿意度",
        ["夯", "頂級", "人上人", "NPC", "拉完了"],
        horizontal=True,
    )
    feedback = st.text_area("意見回饋")
    submitted = st.form_submit_button("送出")

if submitted:
    st.success("感謝您的回饋！")
