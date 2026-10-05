import streamlit as st

st.set_page_config(page_title="課程回饋表單", page_icon="🛸")

# 科幻特效：網格背景、霓虹標題、發光表單外框與按鈕
# 顏色一律用 light-dark(白天色, 夜間色)，會跟著 Streamlit 的主題自動切換
st.html(
    """
<style>
[data-testid="stAppViewContainer"] {
    --neon: light-dark(#0077b6, #00e5ff);
    background:
        radial-gradient(circle at 50% 0%, light-dark(rgba(0, 119, 182, 0.12), rgba(0, 229, 255, 0.18)), transparent 60%),
        linear-gradient(light-dark(rgba(0, 119, 182, 0.08), rgba(0, 229, 255, 0.06)) 1px, transparent 1px),
        linear-gradient(90deg, light-dark(rgba(0, 119, 182, 0.08), rgba(0, 229, 255, 0.06)) 1px, transparent 1px),
        light-dark(#eef4fa, #05070f);
    background-size: 100% 100%, 40px 40px, 40px 40px;
}
h1 {
    letter-spacing: 0.08em;
    text-shadow: 0 0 8px light-dark(rgba(0, 119, 182, 0.35), #00e5ff),
                 0 0 24px light-dark(transparent, rgba(0, 229, 255, 0.6));
}
[data-testid="stForm"] {
    background: light-dark(rgba(255, 255, 255, 0.85), rgba(11, 20, 36, 0.75));
    border: 1px solid color-mix(in srgb, var(--neon) 50%, transparent);
}
[data-testid="stFormSubmitButton"] button {
    border: 1px solid var(--neon);
    color: var(--neon);
    letter-spacing: 0.3em;
}
[data-testid="stFormSubmitButton"] button:hover {
    background: color-mix(in srgb, var(--neon) 12%, transparent);
}

/* 滿意度按鈕：HUD 風格細框，依序為 夯、頂級、人上人、NPC、拉完了 */
/* 白天用較深的顏色，才能在淺色底上維持高對比 */
[data-testid="stForm"] [data-testid="stButtonGroup"] button:nth-of-type(1) { --tier: light-dark(#d90429, #ff2e63); }
[data-testid="stForm"] [data-testid="stButtonGroup"] button:nth-of-type(2) { --tier: light-dark(#c25e00, #ff9f1c); }
[data-testid="stForm"] [data-testid="stButtonGroup"] button:nth-of-type(3) { --tier: light-dark(#8f6b00, #ffe600); }
[data-testid="stForm"] [data-testid="stButtonGroup"] button:nth-of-type(4) { --tier: light-dark(#7a6a42, #f2e6c4); }
[data-testid="stForm"] [data-testid="stButtonGroup"] button:nth-of-type(5) { --tier: light-dark(#5b6b7d, #8a9bb0); }
[data-testid="stForm"] [data-testid="stButtonGroup"] button {
    background: light-dark(rgba(255, 255, 255, 0.9), rgba(5, 7, 15, 0.85)) !important;
    border: 1.5px solid var(--tier) !important;
    border-radius: 3px !important;
    color: var(--tier) !important;
    font-weight: 700;
    letter-spacing: 0.15em;
    padding: 0.4rem 1.2rem;
    text-shadow: 0 0 6px light-dark(transparent, var(--tier));
    transition: transform 0.15s, opacity 0.15s, background 0.15s;
}
[data-testid="stForm"] [data-testid="stButtonGroup"] button p {
    color: inherit !important;
}
[data-testid="stForm"] [data-testid="stButtonGroup"] button:hover {
    background: color-mix(in srgb, var(--tier) 15%, light-dark(#ffffff, #05070f)) !important;
}
/* 已選的那一個：填滿該等級顏色並放大；有選擇時其餘的變暗 */
[data-testid="stForm"] [data-testid="stButtonGroup"] button[kind="pillsActive"] {
    background: var(--tier) !important;
    color: light-dark(#ffffff, #05070f) !important;
    text-shadow: none;
    transform: scale(1.08);
}
[data-testid="stForm"] [data-testid="stButtonGroup"]:has(button[kind="pillsActive"]) button[kind="pills"] {
    opacity: 0.4;
}
</style>
"""
)

st.caption("◢ COURSE FEEDBACK TERMINAL ◣")
st.title("課程回饋表單")
st.caption("SYSTEM ONLINE — 右上角 ⋮ → Settings 可切換白天／夜間模式")

# 頁面說明文字
st.markdown(
    "感謝你撥空填寫本課程的回饋表單！你的意見將作為調整課程內容與教學方式的參考。\n\n"
    "請先在左側 **Sidebar** 選擇科系，再填寫下方欄位後按下送出，其中 **姓名為必填**。"
)

# 科系選擇放在 Sidebar（不在表單內，送出時直接讀取目前選擇的值）
with st.sidebar:
    st.header("◢ 基本資料")
    department = st.selectbox(
        ":material/school: 科系", ["資訊工程系", "電子工程系", "其他"]
    )

# 用 st.form 包起來，所有欄位會在按下送出時才一起送出
with st.form("feedback_form"):
    name = st.text_input(":material/person: 姓名（必填）")
    # 用 pills 讓使用者直接點文字選擇，顏色由上方 CSS 依順序設定
    satisfaction = st.pills(
        ":material/star: 課程滿意度",
        ["夯", "頂級", "人上人", "NPC", "拉完了"],
    )
    feedback = st.text_area(":material/chat: 意見回饋")
    submitted = st.form_submit_button(
        "送出", icon=":material/rocket_launch:", width="stretch"
    )

if submitted:
    # 姓名只有空白也視為未填寫
    if not name.strip():
        st.warning("請先填寫姓名再送出！", icon=":material/warning:")
    else:
        st.success("感謝您的回饋！", icon=":material/check_circle:")
        # 顯示這次送出的姓名、科系與滿意度
        with st.container(border=True):
            col_name, col_department, col_satisfaction = st.columns(3)
            col_name.metric("姓名", name.strip())
            col_department.metric("科系", department)
            col_satisfaction.metric("滿意度", satisfaction or "未選擇")
