# ==============================================================================
# PROJECT: LSOEP TITAN BAYELSA - WAR ROOM & RADAR ENGINE
# OFFICE: DISTINGUISHED SENATOR HENRY SERIAKE DICKSON (BAYELSA WEST)
# REVISION: v34.0.3 [RICH RESTORATION - BAYELSA COMMAND LOCK]
# ==============================================================================

import streamlit as st
import pandas as pd
import plotly.express as px

def render_election_matrix():
    """🗳️ LIVE DIGITAL GRAPHICAL MATRIX FOR 5-TIER ELECTIONS"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🗳️ LIVE DIGITAL GRAPHICAL MATRIX")
    
    # DYNAMIC COLORED BOX MATRIX
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="election-card pres-bg"><h3>PRESIDENTIAL</h3><h1>4,210</h1></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="election-card gov-bg"><h3>GOVERNORSHIP</h3><h1>3,980</h1></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="election-card sen-bg"><h3>SENATORIAL</h3><h1>5,920</h1></div>', unsafe_allow_html=True)
    
    c4, c5 = st.columns(2)
    with c4:
        st.markdown('<div class="election-card house-bg"><h3>FEDERAL HOUSE</h3><h1>2,150</h1></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="election-card house-bg"><h3>STATE HOUSE</h3><h1>1,890</h1></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_radar():
    """🛡️ DOUBLE-DIPPING DETECTION RADAR WITH BLINKING RED ALERT"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🛡️ 🛡️ DOUBLE-DIPPING DETECTION RADAR")
    
    # 🔴 RESTORED: BLINKING RED ALERT INJECTOR (SERIAKE DICKSON HUB AUDIT)
    st.markdown('''
        <div class="radar-blink-alert">
            ⚠️ RED ALERT: 4 DUPLICATE NIN ATTEMPTS DETECTED - IMMEDIATE ADJUDICATION REQUIRED
        </div>
    ''', unsafe_allow_html=True)
    
    # Calibrated target identity search token for Bayelsa West data streams
    st.info("Adjudicating Identity: NIN-MOCK-BYW-0")
    
    # ADJUDICATION CONTROL MATRIX
    adj_col1, adj_col2, adj_col3 = st.columns(3)
    if adj_col1.button("✅ APPROVE IDENTITY"): 
        st.success("Authorization Protocol Success.")
    if adj_col2.button("📦 ARCHIVE ATTEMPT"): 
        st.warning("Identity Moved to Cold Storage Vault.")
    if adj_col3.button("🗑️ DELETE ENTRY"): 
        st.error("Purged from Titan Cloud Matrix.")
    
    # TARGET DATA DISPLAY
    try:
        target_data = st.session_state.global_registry[st.session_state.global_registry["NIN"] == "NIN-MOCK-BYW-0"]
        st.table(target_data)
    except Exception:
        st.caption("Active data lane monitoring enabled. Awaiting collision logs.")
        
    st.markdown('</div>', unsafe_allow_html=True)

def render_vantedge():
    """💎 THE VANTEDGE ENGINE: 2027 CAMPAIGN BRAIN (RESTORED - 2 LGA PARTICLES)"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("💎 THE VANTEDGE ENGINE: 2027 CAMPAIGN BRAIN")
    
    # Recalibrated to track performance trends exclusively for Sagbama and Ekeremor
    van_df = pd.DataFrame({
        "LGA": ["SAGBAMA", "EKEREMOR"],
        "Saturation": [84, 76]
    })
    st.plotly_chart(px.line(van_df, x="LGA", y="Saturation", title="Campaign Saturation Index"), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)