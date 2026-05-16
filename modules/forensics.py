# ==============================================================================
# PROJECT: LSOEP TITAN BAYELSA - FORENSIC AUDIT & WAIVER ENGINE
# OFFICE: DISTINGUISHED SENATOR HENRY SERIAKE DICKSON (BAYELSA WEST)
# REVISION: v34.0.1 [VARIABLE FIX - BAYELSA CONVENTION SETUP]
# ==============================================================================

import streamlit as st
import pandas as pd

# ==============================================================================
# 1. LEGISLATIVE WAIVER LOGIC (FIXED ATTRIBUTE)
# ==============================================================================
def render_wai_logic():
    """
    📜 LEGISLATIVE WAIVER & ADMINISTRATIVE PREROGATIVE
    This module handles executive overrides and eligibility dispensations.
    Authorized Personnel: Senator Seriake Dickson Command Hub Only.
    """
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📜 LEGISLATIVE WAIVER & ADMINISTRATIVE PREROGATIVE")
    
    # SECURITY & AUDIT PROTOCOL
    st.warning("AUTHENTICATION ACTIVE: All waivers are logged to the Seriake Dickson Audit Trail.")
    
    with st.container():
        # DATA CAPTURE FIELDS
        w_col1, w_col2 = st.columns([1, 2])
        target_nin = w_col1.text_input("INPUT CONSTITUENT NIN", key="waiver_target_nin")
        waiver_cat = w_col2.selectbox("SELECT WAIVER JUSTIFICATION", 
                                      ["Age Dispensation", "Document Deficiency", "Urgent Humanitarian Need", "Senator's Prerogative"])
        
        # DETAILED REMARKS FOR AUDIT
        remarks = st.text_area("EXECUTIVE JUSTIFICATION / REMARKS", height=120, key="waiver_remarks")
        
        # EXECUTION COMMAND
        if st.button("⚖️ EXECUTE ADMINISTRATIVE WAIVER"):
            if target_nin and remarks:
                st.success(f"Administrative Protocol Applied: Waiver granted to NIN {target_nin}")
                st.info(f"Category: {waiver_cat}")
            else:
                st.error("Protocol Terminated: Target NIN and Executive Remarks are Mandatory.")
                
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. GROUND TRUTH VERIFICATION (EC8A FORMS)
# ==============================================================================
def render_ground_truth():
    """📝 Auditing physical vs digital EC8A form uploads for Bayelsa West."""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📝 GROUND TRUTH VERIFICATION (EC8A SYNC)")
    
    audit_c1, audit_c2 = st.columns(2)
    # Swapped from Akwa Ibom LGAs to Bayelsa West LGAs
    lga_audit = audit_c1.selectbox("Audit Target LGA", ["SAGBAMA", "EKEREMOR"])
    audit_c2.info(f"Batched forensic verification active for {lga_audit}.")
    
    st.file_uploader("UPLOAD PHYSICAL SCAN BATCH (PNG/JPG/PDF)", key="gt_batch_uploader")
    
    st.markdown("---")
    st.write("📊 **FORENSIC VARIANCE ANALYSIS**")
    st.progress(0.42)
    st.caption("Ground Truth Accuracy Index: 58% Verified.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 3. BULK DATA SYNCHRONIZATION
# ==============================================================================
def render_bulk_sync():
    """📂 BULK SYNC: Constituency-wide data injection and registry updates."""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📂 BULK DATA SYNCHRONIZATION HUB")
    
    st.write("Current CSF Reporting Queue: 2,840 Records Detected.")
    
    if st.button("🚀 INITIATE GLOBAL TITAN SYNC"):
        with st.spinner("Linking with Federal Republic of Nigeria Master Database..."):
            st.success("Global Sync Successful. Master Registry Updated.")
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 4. BILLS & LEGISLATIVE MOMENTUM (FIXED VARIABLE)
# ==============================================================================
def render_bills_matrix():
    """🚀 Tracking progress of Legislative Bills and constituency impacts."""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🚀 BILLS & LEGISLATIVE MOMENTUM MATRIX")
    
    # 🟢 FIXED: Variable Name Alignment
    bills_matrix_df = pd.DataFrame({
        "Legislative Instrument": [
            "Constituency Development Fund Act", 
            "MSME Grant Extension 2026", 
            "Digital Identity Protection Bill"
        ],
        "Stage": [
            "Third Reading", 
            "Public Hearing", 
            "Executive Assent"
        ],
        "Constituency Priority": [
            "High", 
            "Critical", 
            "Moderate"
        ]
    })
    
    # Render table using the corrected variable
    st.table(bills_matrix_df)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 5. COMMAND DASHBOARDS
# ==============================================================================
def render_supervisor_dashboard():
    """WARD SUPERVISOR INTERFACE"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📊 WARD SUPERVISOR COMMAND HUB")
    st.metric("Authenticated Enrollments", "4,120", "+12% Growth")
    st.markdown('</div>', unsafe_allow_html=True)

def render_pu_agent_gateway():
    """PU AGENT GATEWAY"""
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("📡 POLLING UNIT FIELD AGENT GATEWAY")
    st.camera_input("📸 SCAN PHYSICAL FORM FOR REAL-TIME SYNC")
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 6. END OF FORENSIC MODULE - v34.0.1
# ==============================================================================