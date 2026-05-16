# ==============================================================================
# PROJECT: LSOEP TITAN BAYELSA - INTELLIGENCE & ANALYTICS ENGINE
# OFFICE: DISTINGUISHED SENATOR HENRY SERIAKE DICKSON (BAYELSA WEST)
# REVISION: v34.0.2 [CUN MATRIX RESTORATION - BAYELSA GEOGRAPHY SYNC]
# ==============================================================================

import streamlit as st
import pandas as pd
import time

# ==============================================================================
# 0. GEOGRAPHICAL JURISDICTION ARCHITECTURE (EXPLICIT BAYELSA WEST WARD MAPPING)
# ==============================================================================
GEOGRAPHY = {
    "SAGBAMA LGA": [
        "SAGBAMA", 
        "AGBERE", 
        "ANGALABIRI", 
        "OFONI", 
        "ADAGBABIRI", 
        "ODONI", 
        "TROFANI", 
        "EBEDEBIRI", 
        "OSSUAMA", 
        "ASAMABIRI", 
        "AGOROGBENE", 
        "ISENYI", 
        "TORU-BENI", 
        "TUNGBO"
    ],
    "EKEREMOR LGA": [
        "EKEREMOR", 
        "EDUMANE", 
        "AMATOLO", 
        "OYAKIRI", 
        "TARAKIRI", 
        "OPOROMA", 
        "OGBUSA", 
        "ALEIBIRI", 
        "LALAGBENE", 
        "EGBEMO-ANGALABIRI", 
        "AGGE", 
        "ANGALAWEI-GBENE"
    ]
}

# ==============================================================================
# 1. ANALYTICS & EQUITY FUNCTIONS (RESTORED ATTRIBUTES)
# ==============================================================================

def render_registry():
    """📊 MASTER REGISTRY VIEW"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📊 MASTER CONSTITUENT REGISTRY")
    df = st.session_state.global_registry.copy()
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_cun_matrix():
    """📈 CONSTITUENT URGENCY NETWORK (CUN) MATRIX"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📈 CONSTITUENT URGENCY NETWORK (CUN) MATRIX")
    st.info("Prioritizing resource distribution based on local hardship indices.")
    cun_data = pd.DataFrame({
        "LGA": list(GEOGRAPHY.keys()),
        "Urgency Score": [84, 76],  # Recalibrated index score fields for 2 LGAs
        "Last Palliative Sync": ["2026-05-15"] * 2
    })
    st.line_chart(cun_data.set_index("LGA")["Urgency Score"])
    st.dataframe(cun_data, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_equity_log():
    """⚖️ RESOURCE EQUITY LOG"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("⚖️ RESOURCE EQUITY DISTRIBUTION LOG")
    st.write("Tracking the geopolitical balance of empowerments across Bayelsa West LGAs.")
    equity_data = pd.DataFrame({
        "Sector": ["Education", "Agric", "ICT", "Health"],
        "Allocation %": [35, 25, 20, 20]
    })
    st.bar_chart(equity_data.set_index("Sector"))
    st.markdown('</div>', unsafe_allow_html=True)

def render_cv_audit():
    """🎓 EXECUTIVE CV AUDIT VAULT"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🎓 EXECUTIVE CV AUDIT & ARTISAN SKILL MATRIX")
    vault_data = pd.DataFrame([
        {"Name": "Tari Ebiere", "Skill": "Mechanical Engineering", "Level": "PhD", "Status": "VERIFIED"},
        {"Name": "Kemela Okponan", "Skill": "Electrical Technician", "Level": "HND", "Status": "PENDING"}
    ])
    st.dataframe(vault_data, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. PUBLIC GATEWAY: EMPOWERMENT & TOWN HALL (AUTO-SYNC READY)
# ==============================================================================

def render_public_gateway():
    """Renders the Full Enrollment Registry with Auto-Ward Refresh."""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>🏛️ CONSTITUENT EMPOWERMENT/PALLIATIVE ENROLLMENT REGISTRY</h2>", unsafe_allow_html=True)
    
    master_lga = st.selectbox("STEP 1: SELECT YOUR LGA", list(GEOGRAPHY.keys()), key="sync_lga_v29")

    with st.form("titan_v29_restoration"):
        # A. PERSONAL IDENTITY
        st.subheader("👤 PERSONAL IDENTITY REGISTRY")
        pi1, pi2 = st.columns(2)
        with pi1:
            st.text_input("Full Name")
            st.selectbox("Gender", ["Select Gender", "Male", "Female", "Other"])
            st.text_input("NIN (11 Digits)")
            st.file_uploader("Upload NIN Slip")
        with pi2:
            st.selectbox("Ward Jurisdiction", GEOGRAPHY[master_lga], key="sync_ward_id")
            st.text_input("VIN (Voters Card)")
            st.text_input("Phone Number")
            st.selectbox("Disability Status", ["None", "Physical", "Visual"])

        st.divider()

        # B. CV/ARTISAN VAULT
        st.subheader("🎓 CV AND ARTISAN REGISTRATION VAULT")
        va1, va2 = st.columns(2)
        with va1:
            st.selectbox("Education Level", ["PhD", "Masters", "B.Sc/B.A", "HND", "ND", "SSCE"])
            st.multiselect("Artisan Skills", ["Mechanical", "Electrical", "Welding", "Tailoring", "ICT", "OTHERS"])
            st.file_uploader("Upload CV")
        with va2:
            st.text_input("Trade Name")
            st.text_input("Years of Experience")
            st.file_uploader("Upload Certification")

        st.divider()

        # C. BIOMETRIC PHOTO CAPTURE
        st.subheader("📸 BIOMETRIC PHOTO CAPTURE")
        st.markdown("""<style>[data-testid="stCameraInput"] { width: 40% !important; margin: 0 auto; border: 3px solid #D4AF37; border-radius: 15px; }</style>""", unsafe_allow_html=True)
        st.camera_input("IDENTITY SYNC", key="v29_cam_trigger")

        st.divider()

        # D. LEADER VOUCHING
        st.subheader("🏛️ Leader Vouching Verification")
        lv1, lv2 = st.columns(2)
        with lv1:
            st.text_input("Leader LGA/Ward")
            st.text_input("Village Name")
            st.text_input("Leader Full Name")
        with lv2:
            st.text_input("PORTFOLIO IN THE COMMUNITY")
            st.text_input("Leader NIN")
            st.file_uploader("Leader NIN UPLOAD")
        st.text_area("REMARKS Note")

        st.divider()

        # E. TOWN HALL (DEEP BLUE SPLASH)
        st.markdown('<div class="townhall-blue-splash">', unsafe_allow_html=True)
        st.subheader("🗣️ COMMUNITY TOWN HALL VOICE")
        th1, th2 = st.columns(2)
        with th1:
            th_lga = st.selectbox("LGA of Complaint", list(GEOGRAPHY.keys()), key="th_lga_v29")
            st.text_input("Complainant Phone Number")
        with th2:
            th_ward = st.selectbox("Ward of Complaint", GEOGRAPHY[th_lga], key="th_ward_v29")
            st.multiselect("Infrastructure Gaps", ["Security", "Roads", "Education", "Electricity", "OTHERS"])
        st.text_area("Suggestion Context", height=100)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.form_submit_button("LOCK & SUBMIT TO TITAN HUB"):
            st.balloons()
            time.sleep(0.5)
            st.balloons()
            st.success("THANK YOU FOR YOUR TIME! Submission synchronized.")
            st.markdown("<h3 style='text-align: center; color: #D4AF37;'>YOUR VOICE HAS BEEN HEARD.</h3>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)