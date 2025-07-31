import streamlit as st
import pandas as pd
import plotly.express as px

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

# 수면 시간별 평균 스트레스 수준
st.markdown("## 😣 수면 시간에 따른 평균 스트레스 수준")
sleep_stress = df.groupby('weekday_sleep')['stress_level'].mean().reset_index()
fig_sleep_stress = px.bar(
    sleep_stress,
    x='weekday_sleep',
    y='stress_level',
    title='수면 시간별 평균 스트레스 수준',
    labels={'weekday_sleep': '평일 수면 시간', 'stress_level': '평균 스트레스'},
    color='stress_level',
    color_continuous_scale='RdBu_r',
    text=sleep_stress['stress_level'].round(2)
)
fig_sleep_stress.update_traces(textposition='outside')
fig_sleep_stress.update_layout(margin=dict(t=50, b=20, l=40, r=20))
st.plotly_chart(fig_sleep_stress, use_container_width=True)

# 수면 시간별 아침 피로감 평균
st.markdown("## 😴 수면 시간에 따른 아침 피로감 평균")
sleep_tired = df.groupby('weekday_sleep')['tired_morning'].mean().reset_index()
fig_sleep_tired = px.bar(
    sleep_tired,
    x='weekday_sleep',
    y='tired_morning',
    title='수면 시간별 아침 피로감 수준',
    labels={'weekday_sleep': '평일 수면 시간', 'tired_morning': '평균 피로감'},
    color='tired_morning',
    color_continuous_scale='Tealgrn',
    text=sleep_tired['tired_morning'].round(2)
)
fig_sleep_tired.update_traces(textposition='outside')
fig_sleep_tired.update_layout(margin=dict(t=50, b=20, l=40, r=20))
st.plotly_chart(fig_sleep_tired, use_container_width=True)

# 수면 시간별 스트레스와 피로감 평균 비교
st.markdown("## 📊 수면 시간별 스트레스와 피로감 비교")
sleep_summary = df.groupby('weekday_sleep')[['stress_level', 'tired_morning']].mean().reset_index()
fig_sleep_compare = px.bar(
    sleep_summary.melt(id_vars='weekday_sleep', var_name='항목', value_name='수치'),
    x='weekday_sleep',
    y='수치',
    color='항목',
    barmode='group',
    title='수면 시간에 따른 평균 스트레스 및 피로감',
    labels={'weekday_sleep': '수면 시간', '수치': '평균 수치'}
)
fig_sleep_compare.update_layout(margin=dict(t=50, b=20, l=40, r=20))
st.plotly_chart(fig_sleep_compare, use_container_width=True)
