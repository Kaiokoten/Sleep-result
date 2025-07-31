import streamlit as st
import pandas as pd
import plotly.express as px
data = {
    "weekday_sleep": ["5시간 이하", "6시간", "7시간", "8시간 이상"] * 40,
    "stress_level": [5, 4, 2, 1] * 40,
    "tired_morning": [7, 6, 3, 2] * 40,
    "insomnia": ["예", "예", "아니오", "아니오"] * 40
}

st.set_page_config(
    page_title="🛌 수면 & 스트레스 설문 분석",
    page_icon="🧠",
    layout="wide"
)

st.title("🛌 수면과 스트레스 설문 결과 분석 대시보드")
st.markdown("""
이 대시보드는 187명의 설문 결과를 바탕으로 수면 습관과 정신 건강 간의 관계를 시각적으로 분석합니다.  
그래프에 마우스를 올리면 자세한 수치를 확인할 수 있습니다.
""")

# 데이터 불러오기
df = pd.read_csv("responses.csv")

# --- 연령대 분포 Pie Chart ---
st.markdown("## 👥 연령대 분포")
age_counts = df['age'].value_counts().sort_index()
fig_age = px.pie(
    names=age_counts.index,
    values=age_counts.values,
    title="연령대별 비율",
    color_discrete_sequence=px.colors.qualitative.Dark24,
    hole=0.4,
)
fig_age.update_traces(textposition='inside', textinfo='percent+label')
fig_age.update_layout(
    legend_title_text='연령대',
    margin=dict(t=50, b=20, l=20, r=20),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)
st.plotly_chart(fig_age, use_container_width=True)

st.markdown("---")

# --- 평일 수면 시간 Pie Chart ---
st.markdown("## 🛏️ 평일 수면 시간 분포")
sleep_counts = df['weekday_sleep'].value_counts()
fig_sleep = px.pie(
    names=sleep_counts.index,
    values=sleep_counts.values,
    title="평일 평균 수면 시간 분포",
    color_discrete_sequence=px.colors.sequential.Viridis_r,
    hole=0.3,
)
fig_sleep.update_traces(textposition='inside', textinfo='percent+label')
fig_sleep.update_layout(
    legend_title_text='수면 시간',
    margin=dict(t=50, b=20, l=20, r=20),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)
st.plotly_chart(fig_sleep, use_container_width=True)

st.markdown("---")

# --- 불면증 경험 Pie Chart ---
st.markdown("## 😵 불면증 경험 여부")
insomnia_counts = df['insomnia'].value_counts()
fig_insomnia = px.pie(
    names=insomnia_counts.index,
    values=insomnia_counts.values,
    title="불면증 경험 비율",
    color_discrete_sequence=px.colors.qualitative.Set2,
    hole=0.4,
)
fig_insomnia.update_traces(textposition='inside', textinfo='percent+label')
fig_insomnia.update_layout(
    legend_title_text='불면증 경험',
    margin=dict(t=50, b=20, l=20, r=20),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)
st.plotly_chart(fig_insomnia, use_container_width=True)

st.markdown("---")

# --- 스트레스 수준 분포 Bar Chart ---
st.markdown("## ⚡ 스트레스 수준 분포")
fig_stress = px.histogram(
    df,
    x='stress_level',
    nbins=10,
    title="스트레스 수준 빈도",
    labels={'stress_level': '스트레스 수준 (1-10)'},
    color_discrete_sequence=['#FF6F61'],
)
fig_stress.update_layout(
    margin=dict(t=50, b=20, l=40, r=20),
    xaxis=dict(dtick=1),
    yaxis_title='응답 수',
)
fig_stress.update_traces(texttemplate='%{y}', textposition='outside')
st.plotly_chart(fig_stress, use_container_width=True)

st.markdown("---")

# --- 운동 여부에 따른 평균 스트레스 Bar Chart ---
st.markdown("## 💪 운동 여부에 따른 평균 스트레스 수준")
stress_by_activity = df.groupby('physical_activity')['stress_level'].mean().reset_index()
fig_activity = px.bar(
    stress_by_activity,
    x='physical_activity',
    y='stress_level',
    title='운동 여부별 평균 스트레스 수준',
    labels={'physical_activity': '운동 여부', 'stress_level': '평균 스트레스'},
    color='stress_level',
    color_continuous_scale='RdYlGn_r',
    text=stress_by_activity['stress_level'].round(2),
)
fig_activity.update_traces(textposition='outside')
fig_activity.update_layout(
    margin=dict(t=50, b=20, l=40, r=20),
    yaxis_range=[0, 10],
    coloraxis_showscale=False
)
st.plotly_chart(fig_activity, use_container_width=True)

st.markdown("---")

# --- 아침 피로감 분포 Pie Chart ---
st.markdown("## 😴 아침 피로감 정도")
tired_counts = df['tired_morning'].value_counts()
fig_tired = px.pie(
    names=tired_counts.index,
    values=tired_counts.values,
    title='아침에 느끼는 피로감 비율',
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    hole=0.4,
)
fig_tired.update_traces(textposition='inside', textinfo='percent+label')
fig_tired.update_layout(
    legend_title_text='피로감 정도',
    margin=dict(t=50, b=20, l=20, r=20),
    uniformtext_minsize=14,
    uniformtext_mode='hide'
)
st.plotly_chart(fig_tired, use_container_width=True)

st.markdown("---")

st.markdown("### 📢 본 대시보드는 Streamlit과 Plotly 라이브러리를 활용하여 제작되었습니다.")

import plotly.express as px
import pandas as pd
import streamlit as st

# 💡 Пример данных — можешь подгрузить свои или заменить CSV
data = {
    "weekday_sleep": ["5시간 이하", "6시간", "7시간", "8시간 이상"] * 40,
    "stress_level": [5, 4, 2, 1] * 40,
    "tired_morning": [7, 6, 3, 2] * 40,
}
df = pd.DataFrame(data)

st.title("🛌 수면 시간과 스트레스/피로감 관계 분석")

# 1️⃣ 스트레스 수준 vs 수면 시간
st.markdown("## 1. 수면 시간에 따른 스트레스 수준")
stress_sleep = df.groupby("weekday_sleep")["stress_level"].mean().reset_index()
fig_stress = px.bar(
    stress_sleep,
    x="weekday_sleep",
    y="stress_level",
    title="수면 시간에 따른 평균 스트레스 수준",
    labels={"weekday_sleep": "수면 시간", "stress_level": "스트레스 수준"},
    color="stress_level",
    color_continuous_scale="Reds",
    text=stress_sleep["stress_level"].round(2)
)
fig_stress.update_traces(textposition="outside")
st.plotly_chart(fig_stress, use_container_width=True)

# 2️⃣ 피로감 vs 수면 시간
st.markdown("## 2. 수면 시간에 따른 아침 피로감")
tired_sleep = df.groupby("weekday_sleep")["tired_morning"].mean().reset_index()
fig_tired = px.bar(
    tired_sleep,
    x="weekday_sleep",
    y="tired_morning",
    title="수면 시간에 따른 평균 아침 피로감",
    labels={"weekday_sleep": "수면 시간", "tired_morning": "피로감"},
    color="tired_morning",
    color_continuous_scale="Blues",
    text=tired_sleep["tired_morning"].round(2)
)
fig_tired.update_traces(textposition="outside")
st.plotly_chart(fig_tired, use_container_width=True)

# 3️⃣ 스트레스와 피로감의 상관관계 (산점도)
st.markdown("## 3. 스트레스와 아침 피로감의 관계")
fig_scatter = px.scatter(
    df,
    x="stress_level",
    y="tired_morning",
    color="weekday_sleep",
    title="스트레스 수준과 아침 피로감의 상관관계",
    labels={"stress_level": "스트레스 수준", "tired_morning": "아침 피로감"},
    size_max=15,
)
fig_scatter.update_layout(margin=dict(t=50, b=30))
st.plotly_chart(fig_scatter, use_container_width=True)

# --- 수면 시간에 따른 불면증 경험 비율 Bar Chart ---
st.markdown("## 😵 수면 시간에 따른 불면증 경험 비율")

# 데이터 준비
insomnia_by_sleep = df.groupby(['weekday_sleep', 'insomnia']).size().reset_index(name='count')
total_by_sleep = df['weekday_sleep'].value_counts().reset_index()
total_by_sleep.columns = ['weekday_sleep', 'total']
insomnia_by_sleep = pd.merge(insomnia_by_sleep, total_by_sleep, on='weekday_sleep')
insomnia_by_sleep['percent'] = (insomnia_by_sleep['count'] / insomnia_by_sleep['total'] * 100).round(1)
data = {
    "weekday_sleep": ["5시간 이하", "6시간", "7시간", "8시간 이상"] * 40,
    "stress_level": [5, 4, 2, 1] * 40,
    "tired_morning": [7, 6, 3, 2] * 40,
    "insomnia": ["예", "예", "아니오", "아니오"] * 40
}

# 시각화
fig_insomnia_bar = px.bar(
    insomnia_by_sleep,
    x='weekday_sleep',
    y='percent',
    color='insomnia',
    barmode='group',
    text='percent',
    labels={
        'weekday_sleep': '평일 평균 수면 시간',
        'percent': '비율 (%)',
        'insomnia': '불면증 경험 여부'
    },
    title="수면 시간에 따른 불면증 경험 여부",
    color_discrete_sequence=px.colors.qualitative.Set2,
)
fig_insomnia_bar.update_layout(
    margin=dict(t=50, b=20, l=40, r=20),
    yaxis_range=[0, 100]
)
fig_insomnia_bar.update_traces(textposition='outside')
st.plotly_chart(fig_insomnia_bar, use_container_width=True)

