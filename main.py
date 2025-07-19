# sleep_analysis_dashboard.py

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
    color_discrete_sequence=px.colors.sequential.RdBu
)
st.plotly_chart(fig_age, use_container_width=True)

# ----- WEEKDAY SLEEP PIE -----
st.subheader("🛏️ 평일 수면 시간 분포")
sleep_count = df["weekday_sleep"].value_counts()
fig_sleep = px.pie(
    names=sleep_count.index,
    values=sleep_count.values,
    title="평일 평균 수면 시간",
    color_discrete_sequence=px.colors.sequential.Purples
)
st.plotly_chart(fig_sleep, use_container_width=True)

# ----- STRESS BAR CHART -----
st.subheader("⚡ 스트레스 수준 분포")
fig_stress = px.histogram(
    df,
    x="stress_level",
    nbins=10,
    title="스트레스 수준 빈도수",
    labels={"stress_level": "스트레스 수준"},
    color_discrete_sequence=["#FF6961"]
)
st.plotly_chart(fig_stress, use_container_width=True)

# ----- INSOMNIA PIE CHART -----
st.subheader("😵 불면증 유무")
fig_insomnia = px.pie(
    names=df["insomnia"].value_counts().index,
    values=df["insomnia"].value_counts().values,
    title="불면증 경험 여부",
    color_discrete_sequence=px.colors.sequential.Blues
)
st.plotly_chart(fig_insomnia, use_container_width=True)

# ----- PHYSICAL ACTIVITY & STRESS -----
st.subheader("💪 운동 여부와 스트레스 평균 비교")
stress_by_activity = df.groupby("physical_activity")["stress_level"].mean().reset_index()
fig_activity = px.bar(
    stress_by_activity,
    x="physical_activity",
    y="stress_level",
    title="운동 여부에 따른 평균 스트레스 수준",
    labels={"physical_activity": "운동 여부", "stress_level": "평균 스트레스"},
    color="stress_level",
    color_continuous_scale="RdBu"
)
st.plotly_chart(fig_activity, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("이 대시보드는 실제 연구 데이터를 바탕으로 만들어졌으며, Streamlit과 Plotly를 활용해 작성되었습니다.")
