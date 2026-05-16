import streamlit as st
import pandas as pd
import plotly.express as px

def render_activity_monitor():
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📅 STRATEGIC MONITORING ENGINE")
    interval = st.radio("Monitoring Interval", ["DAILY", "WEEKLY", "MONTHLY"], horizontal=True)
    df = pd.DataFrame({"T": [1,2,3,4,5], "V": [10, 30, 45, 90, 142]})
    fig = px.area(df, x="T", y="V", title=f"{interval} DATA REACH VELOCITY")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#D4AF37")
    fig.update_traces(line_color='#D4AF37', fillcolor='rgba(212,175,55,0.2)')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)