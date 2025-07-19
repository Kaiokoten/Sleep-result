import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="수면 설문 결과 분석", page_icon="📊", layout="wide")

st.title("🧠 수면과 스트레스 설문 결과 대시보드")
st.markdown("이 페이지는 187명을 대상으로 한 설문 결과를 시각화하여 수면과 정신 건강의 관계를 분석합니다.")

# Загрузка данных
df = pd.read_csv("responses.csv")

# ----- AGE PIE CHART -----
st.subheader("🧓 연령대 분포")
age_count = df["age"].value_counts()
fig_age = px.pie(
    names=age_count.index,
    values=age_count.values,
    title="연령대 비율",
    color_discrete_sequence=px.colors.qualitative.Dark24  # насыщенная и разнообразная палитра
)
st.plotly_chart(fig_age, use_container_width=True)

# ----- WEEKDAY SLEEP PIE -----
st.subheader("🛏️ 평일 수면 시간 분포")
sleep_count = df["weekday_sleep"].value_counts()
fig_sleep = px.pie(
    names=sleep_count.index,
    values=sleep_count.values,
    title="평일 평균 수면 시간",
    color_discrete_sequence=px.colors.sequential.Viridis_r  # плавный градиент, приятный глазу
)
st.plotly_chart(fig_sleep, use_container_width=True)

# ----- INSOMNIA PIE CHART -----
st.subheader("😵 불면증 유무")
fig_insomnia = px.pie(
    names=df["insomnia"].value_counts().index,
    values=df["insomnia"].value_counts().values,
    title="불면증 경험 여부",
    color_discrete_sequence=px.colors.qualitative.Set2  # мягкие пастельные оттенки
)
st.plotly_chart(fig_insomnia, use_container_width=True)

