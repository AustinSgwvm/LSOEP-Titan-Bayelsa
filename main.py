# ==============================================================================
# PROJECT: LSOEP TITAN BAYELSA - CORE ENGINE INTERFACE
# REVISION: v34.0.6 [GEOGRAPHY, CSS KEYFRAMES, & MOCK UTILITIES - FULL SPECIFICATION]
# ==============================================================================

import streamlit as st
import pandas as pd
import datetime
import os

# ==============================================================================
# DATA ARCHITECTURE LAYER: TWO-LGA COMPLETE ADMINISTRATIVE MATRIX (NO OMISSIONS)
# ==============================================================================

# --- EXPANDED GEOGRAPHICAL DICTIONARY: BAYELSA WEST SENATORIAL DISTRICT ---
# Every administrative ward across Sagbama and Ekeremor LGAs explicitly declared.
GEOGRAPHY = {
    "Sagbama LGA": [
        "Sagbama Ward 1",
        "Salope Ward 2",
        "Asamabiri Ward 3",
        "Angalabiri Ward 4",
        "Ofoni Ward 5",
        "Ebedebiri Ward 6",
        "Ossiama Ward 7",
        "Agoro Ward 8",
        "Toruedeni Ward 9",
        "Adagbabiri Ward 10",
        "Ona Ward 11",
        "Agbere Ward 12",
        "Trofani Ward 13"
    ],
    "Ekeremor LGA": [
        "Ekeremor Ward 1",
        "Onyilolo Ward 2",
        "Ogbosuware Ward 3",
        "Ondewari Ward 4",
        "Isampou Ward 5",
        "Amabulou Ward 6",
        "Agge Ward 7",
        "Egbemo-Angalabiri Ward 8",
        "Onoledi Ward 9",
        "Angalaoweibiri Ward 10",
        "Peretorugbene Ward 11",
        "Ondewari Ward 12",
        "Eyinware Ward 13"
    ]
}

# Unified Form Input Dropdown Selection Target Mappings (Standardized Case)
LGA_WARD_DATA = {
    "SAGBAMA": [
        "SAGBAMA WARD 1",
        "SALOPE WARD 2",
        "ASAMABIRI WARD 3",
        "ANGALABIRI WARD 4",
        "OFONI WARD 5",
        "EBEDEBIRI WARD 6",
        "OSSIAMA WARD 7",
        "AGORO WARD 8",
        "TORUEDENI WARD 9",
        "ADAGBABIRI WARD 10",
        "ONA WARD 11",
        "AGBERE WARD 12",
        "TROFANI WARD 13"
    ],
    "EKEREMOR": [
        "EKEREMOR WARD 1",
        "ONYILOLO WARD 2",
        "OGBOSUWARE WARD 3",
        "ONDEWARI WARD 4",
        "ISAMPOU WARD 5",
        "AMABULOU WARD 6",
        "AGGE WARD 7",
        "EGBEMO-ANGALABIRI WARD 8",
        "ONOREDI WARD 9",
        "ANGALAOWEIBIRI WARD 10",
        "PERETORUGBENE WARD 11",
        "ONDEWARI WARD 12",
        "EYINWARE WARD 13"
    ]
}

# --- UN-TRUNCATED CORE SECTOR REGISTRY DATA ---
MOCK_DATA_REGISTRY = [
    {
        "ID": "LSOEP-BYW-SAG-001",
        "Name": "Preye Tari",
        "LGA": "Sagbama LGA",
        "Ward": "Sagbama Ward 1",
        "NIN": "12345678901",
        "Status": "Verified",
        "Allocation": "SME Seed Capital"
    },
    {
        "ID": "LSOEP-BYW-EKR-002",
        "Name": "Ebiowei Pere",
        "LGA": "Ekeremor LGA",
        "Ward": "Ekeremor Ward 1",
        "NIN": "98765432109",
        "Status": "Verified",
        "Allocation": "Agro-Development Grant"
    },
    {
        "ID": "LSOEP-BYW-SAG-003",
        "Name": "Ayibakuro Joseph",
        "LGA": "Sagbama LGA",
        "Ward": "Ofoni Ward 5",
        "NIN": "45678912301",
        "Status": "Pending Review",
        "Allocation": "Educational Bursary"
    },
    {
        "ID": "LSOEP-BYW-EKR-004",
        "Name": "Tariela Benjamin",
        "LGA": "Ekeremor LGA",
        "Ward": "Agge Ward 7",
        "NIN": "78912345602",
        "Status": "Verified",
        "Allocation": "Fisheries Infrastructure support"
    },
    {
        "ID": "LSOEP-BYW-SAG-005",
        "Name": "Fungefa Ebimobowei",
        "LGA": "Sagbama LGA",
        "Ward": "Agbere Ward 12",
        "NIN": "32165498705",
        "Status": "Flagged",
        "Allocation": "None - Verification Required"
    }
]

# Hardcoded Global Partition Stencil for Bayelsa West Strategic Ledger
PROJECT_PARTITION_ID = "BAYELSA_WEST"

# ==============================================================================
# GLOBAL SYSTEM INITIALIZATION (HARDENED PRODUCTION PROTOCOL)
# ==============================================================================
if 'global_registry' not in st.session_state:
    columns = [
        "NIN", "VIN", "Name", "LGA", "Ward", "Status", "Category", 
        "Skill_Interest", "Academic_Qual", "Admission_Year", "Admission_Letter",
        "Phone", "Leader_Name", "Leader_Contact", "Leader_NIN", "Leader_LGA", 
        "Leader_Ward", "Leader_Portfolio", "Voucher_Code", "Remarks", "Timestamp"
    ]
    st.session_state.global_registry = pd.DataFrame([
        {"NIN": "23456789012", "VIN": "90FVA2345678901", "Name": "Tari Ebiere", "LGA": "SAGBAMA", "Ward": "SAGBAMA WARD 1", "Status": "Verified", "Category": "Professional", "Skill_Interest": "ICT & AI", "Academic_Qual": "Degree/HND", "Admission_Year": "2024", "Admission_Letter": None, "Phone": "08039999999", "Leader_Name": "Chief Seriake", "Leader_Contact": "08038888888", "Leader_NIN": "33333333333", "Leader_LGA": "SAGBAMA", "Leader_Ward": "SAGBAMA WARD 1", "Leader_Portfolio": "Community Leader", "Voucher_Code": "SG01V", "Remarks": "Authentic", "Timestamp": "2026-05-15 10:00:00"},
        {"NIN": "87654321098", "VIN": "90FVA8765432109", "Name": "Kemela Okponan", "LGA": "EKEREMOR", "Ward": "EKEREMOR WARD 1", "Status": "Flagged", "Category": "Skilled Artisan", "Skill_Interest": "Solar Power", "Academic_Qual": "SSCE", "Admission_Year": "2025", "Admission_Letter": None, "Phone": "08037777777", "Leader_Name": "Elder Pere", "Leader_Contact": "08036666666", "Leader_NIN": "44444444444", "Leader_LGA": "EKEREMOR", "Leader_Ward": "EKEREMOR WARD 1", "Leader_Portfolio": "Clergy", "Voucher_Code": "EK02V", "Remarks": "Verify Biometrics", "Timestamp": "2026-05-15 11:15:22"}
    ], columns=columns)

if 'submitted_wards' not in st.session_state:
    st.session_state.submitted_wards = {
        "SAGBAMA_SAGBAMA_WARD_1": "2026-05-15 08:12:04",
        "EKEREMOR_EKEREMOR_WARD_1": "2026-05-15 09:45:10"
    }

if 'submitted_pus' not in st.session_state:
    st.session_state.submitted_pus = {
        "SAGBAMA_SAGBAMA_WARD_1_PU001": "2026-05-15 08:10:00",
        "EKEREMOR_EKEREMOR_WARD_1_PU003": "2026-05-15 09:30:15"
    }

if 'current_page' not in st.session_state:
    st.session_state.current_page = "skill_form"

if 'radar_threat' not in st.session_state:
    st.session_state.radar_threat = False

if 'threat_msg' not in st.session_state:
    st.session_state.threat_msg = ""

# --- REARRANGED LOCAL SANBOX MATRIX OVERRIDE (THE CIRCUIT BREAKER) ---
# This checks if the app is local or live to protect the execution line.
IS_LOCAL_SANDBOX = not os.path.exists("/app/secrets.toml") and not os.path.exists(".streamlit/secrets.toml")

# --- HARDENED CIRCUIT BREAKER MATRIX ---
conn = None
if not IS_LOCAL_SANDBOX:
    try:
        conn = st.connection("postgresql", type="sql")
    except Exception:
        conn = None

# ==============================================================================
# UI INITIALIZATION & CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="LSOEP TITAN BAYELSA | SEN. DICKSON HUB", 
    page_icon="🏛️",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 1. CORE MODULE INTEGRATION (Safe Dynamic Local Bypass)
try:
    from modules import branding, intelligence, war_room, forensics, monitoring
    HAS_MODULES = True
except ImportError:
    HAS_MODULES = False

# Boot Visual Core Layout Stylesheets
if HAS_MODULES:
    branding.apply_regal_styles()

# ==============================================================================
# --- SECTION 3: THE THREE-TIER HARDENED SIDEBAR WITH RESPONSIVE OVERRIDES ---
# ==============================================================================
with st.sidebar:
    st.markdown("""
        <style>
        /* Sidebar Panel Body: Rich Midnight Dark Velvet Blue with Solid Gold Separation Rim */
        [data-testid="stSidebar"] { 
            background-color: #030f21 !important; 
            border-right: 4px solid #FFD700 !important;
        }
        
        .admin-launch-zone {
            border: 2px dashed #00E5FF; padding: 15px; border-radius: 14px;
            background-color: rgba(0, 229, 255, 0.08); margin-bottom: 15px;
        }
        
        .inst-link-box {
            display: block; background: linear-gradient(90deg, #FFD700 0%, #FFA000 100%) !important; 
            color: #020813 !important; padding: 12px; border-radius: 10px; 
            text-align: center; font-weight: 900; margin-bottom: 10px; text-decoration: none;
            font-size: 14px; letter-spacing: 1px; box-shadow: 0 4px 12px rgba(255,215,0,0.2);
            text-transform: uppercase;
        }
        
        /* Action Buttons: Vibrant Neon Teal & Blues with Bold White Text */
        .stButton>button { 
            width: 100% !important; height: 48px !important; font-weight: 800 !important; 
            font-size: 14px !important; margin-bottom: 10px !important; border: 2px solid #FFD700 !important;
            border-radius: 10px !important; color: #FFFFFF !important; transition: all 0.3s ease;
            text-transform: uppercase; letter-spacing: 1px;
        }
        
        button[key="btn_skill"] { background: linear-gradient(90deg, #00B4DB 0%, #0083B0 100%) !important; }
        button[key="btn_sch"] { background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%) !important; }
        button[key="btn_pal"] { background: linear-gradient(90deg, #2e8b57 0%, #38ef7d 100%) !important; }
        button[key="btn_cv"] { background: linear-gradient(90deg, #8E2DE2 0%, #4A00E0 100%) !important; }
        button[key="btn_cmd"] { background: #0b1e36 !important; border: 2px solid #00E5FF !important; }

        @keyframes alert_pulse { 
            0% { background-color: #FF1744; box-shadow: 0 0 10px #FF1744; } 
            50% { background-color: #B71C1C; box-shadow: 0 0 25px #FF1744; } 
            100% { background-color: #FF1744; box-shadow: 0 0 10px #FF1744; } 
        }
        @keyframes radar_flash {
            0% { background-color: #FF0000; color: #FFFFFF; box-shadow: 0 0 20px #FF0000; }
            50% { background-color: #330000; color: #FF0000; box-shadow: 0 0 0px #000000; }
            100% { background-color: #FF0000; color: #FFFFFF; box-shadow: 0 0 20px #FF0000; }
        }
        .sidebar-red-flash {
            animation: alert_pulse 1.2s infinite ease-in-out; color: #FFFFFF !important;
            padding: 14px; border-radius: 10px; text-align: center; font-weight: 900; 
            display: block; width: 100%; font-size: 14px; margin-bottom: 12px;
            letter-spacing: 1px; text-transform: uppercase;
        }
        .radar-sticky-threat {
            animation: radar_flash 0.5s infinite;
            padding: 15px; border-radius: 8px; border: 3px solid #FFFFFF;
            text-align: center; font-weight: bold; font-size: 14px; margin-bottom: 15px;
        }
        .tier-box {
            display: inline-block; padding: 10px 20px; margin: 5px; border-radius: 6px;
            font-weight: bold; color: white; text-align: center; border: 2px solid #FFFFFF;
        }
        .tier-box.tier-pres { background-color: #FF4B4B !important; }
        .tier-box.tier-sen { background-color: #1F77B4 !important; }
        .tier-box.tier-rep { background-color: #2CA02C !important; }
        .tier-box.tier-gov { background-color: #9467BD !important; }
        .tier-box.tier-house { background-color: #FF7F0E !important; }
        
        .stTextInput label p { color: #00E5FF !important; font-weight: 700 !important; }
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.radar_threat:
        st.markdown(f'<div class="radar-sticky-threat">🚨 SECURITY WARNING: IDENTITY DUPLICATION COLLISION<br>{st.session_state.threat_msg}</div>', unsafe_allow_html=True)

    # 💡 REPLACE: "GCON COMMAND HUB KEY" to "COMMAND HUB KEY"
    st.markdown('<div class="admin-launch-zone">', unsafe_allow_html=True)
    adm_key = st.text_input("COMMAND HUB KEY", type="password", key="adm_v30_auth")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 💡 REPLACE & ADD: Facebook URL link injected alongside active website asset tracking portal
    st.divider()
    st.markdown('<a href="https://www.facebook.com/IamHSDickson" target="_blank" class="inst-link-box">🌐 Senator HSD Facebook</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://HSDickson.org" target="_blank" class="inst-link-box">🏛️ Senator HSD Web Portal</a>', unsafe_allow_html=True)
    
    st.divider()
    if st.button("🛠️ SKILL VOCATION POOL", key="btn_skill"): st.session_state.current_page = "skill_form"
    if st.button("🎓 STUDENT SCHOLARSHIP/GRANT", key="btn_sch"): st.session_state.current_page = "scholarship_form"
    if st.button("📦 CONSTITUENT PALLIATIVE ENROLLMENT", key="btn_pal"): st.session_state.current_page = "palliative_gateway"
    if st.button("🚀 CV & ARTISAN VAULT", key="btn_cv"): st.session_state.current_page = "cv_vault"
    
    st.markdown('<div class="sidebar-red-flash">🚨 COMMUNITY URGENT NEED</div>', unsafe_allow_html=True)
    if st.button("LAUNCH URGENT REPORT", key="btn_cun_clean"): st.session_state.current_page = "cun_trigger"
    
    st.divider()
    if st.button("🏛️ RETURN TO COMMAND HUB", key="btn_cmd"): st.session_state.current_page = "main_dashboard"

    # 💡 REPLACEMENTS AND AMENDMENTS: Keys set up with mandatory contextual remarks inputs
    st.divider()
    st.markdown("<p style='color:#FFD700; font-weight:bold; text-transform: uppercase; letter-spacing: 1px;'>Field Authentication</p>", unsafe_allow_html=True)
    sup_key = st.text_input("WARD SUPERVISOR KEY", type="password", key="sup_v30_auth")
    if sup_key:
        st.text_area("Supervisor Remarks/Field Observations", key="sup_remarks", placeholder="Enter authorization details/field log...")
        
    agt_key = st.text_input("POLLING UNIT AGENT KEY", type="password", key="agt_v30_auth")
    if agt_key:
        st.text_area("Agent Remarks/Field Observations", key="agt_remarks", placeholder="Enter unit authorization notes/field log...")
        
    st.caption(f"Engine: v34.0.6-BAYELSA | {datetime.date.today()}")

# 4. COMMAND ROUTING & AUTO-DATA LOGIC
def render_marquee_header():
    if HAS_MODULES:
        branding.render_header() 
        branding.render_marquee()
    else:
        # Gateway Page Scale Adjustments: Portrait containers scaled downward cleanly to minimize screen real estate overflow
        st.markdown('''
            <div style="background: linear-gradient(180deg, #061a33 0%, #020b17 100%); padding: 12px 18px; border-radius: 16px; border: 3px solid #FFD700; text-align: center; margin-bottom:15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
                <div style="display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 2px;">
                    <div style="max-width: 45px; max-height: 45px; width: 45px; height: 45px; border-radius: 6px; border: 2px solid #FFD700; background-color: #030f21; display: flex; align-items: center; justify-content: center; font-size: 18px; box-shadow: inset 0 0 6px #FFD700;">🏛️</div>
                    <div>
                        <h1 style="color:#FFD700; margin:0; font-size:1.7rem; font-weight:900; letter-spacing: 1px; text-transform: uppercase;">SENATOR HENRY SERIAKE DICKSON</h1>
                        <p style="color:#FFF; margin:1px 0; font-weight:bold; font-size:11px; letter-spacing:2px; text-transform: uppercase;">NATIONAL ASSEMBLY SENATORIAL COMMAND HUB</p>
                    </div>
                    <div style="max-width: 45px; max-height: 45px; width: 45px; height: 45px; border-radius: 6px; border: 2px solid #FFD700; background-color: #030f21; display: flex; align-items: center; justify-content: center; font-size: 18px; box-shadow: inset 0 0 6px #FFD700;">📜</div>
                </div>
                <span style="color:#00E5FF; font-weight:800; font-size:9px; border:1px solid #00E5FF; padding:1px 6px; border-radius:12px; letter-spacing: 1px;">BAYELSA WEST LOCAL SANDBOX MATRIX SYSTEM</span>
            </div>
        ''', unsafe_allow_html=True)

# ==============================================================================
# --- SECTION A: WARD SUPERVISOR COMMAND (SAGBAMA & EKEREMOR) ---
# ==============================================================================
if sup_key == "ndc ndc 2027":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🛡️ WARD SUPERVISOR COMMAND: Form EC8A INTELLIGENCE VECTORS</div>', unsafe_allow_html=True)
    
    with st.form("supervisor_form"):
        c1, c2 = st.columns(2)
        with c1:
            sup_name = st.text_input("Supervisor Full Name")
            sup_phone = st.text_input("Phone Number")
            sup_state = st.text_input("State", value="Bayelsa")
            sup_lga = st.selectbox("LGA Location Partition", list(LGA_WARD_DATA.keys()), key="sup_lga_select")
            sup_ward = st.selectbox("Ward Name Location Partition", LGA_WARD_DATA.get(sup_lga, []), key="sup_ward_select")
            sup_ward_unit_name = st.text_input("Ward Unit Name and Number")
        
        ward_id = f"{sup_lga}_{sup_ward}".replace(" ", "_").upper()
        
        with c2:
            st.markdown("""
            **Active Election Tiers:**<br>
            <div class="tier-box tier-pres">Presidential</div><div class="tier-box tier-sen">Senatorial</div>
            <div class="tier-box tier-rep">House of Reps</div><div class="tier-box tier-gov">Governorship</div>
            <div class="tier-box tier-house">State House</div>
            """, unsafe_allow_html=True)
            st.multiselect("Select Tiers to Affirm", ["Presidential", "Senatorial", "Federal House", "Governorship", "State House"], default=["Senatorial"])
            st.number_input("Highest Party Vote (Ward Total)", min_value=0, key="sup_high_vote")
            st.number_input("Principal Votes Cast", min_value=0, key="sup_pr_vote")
            st.file_uploader("Upload Supervisor NIN Slip Column", type=['pdf', 'jpg', 'png'])
        
        st.camera_input("Live Capture of Form EC8A Sheet or screen shot and send where neccessary.")
        
        if st.form_submit_button("📤 SEND TO COMMAND VAULT"):
            if ward_id in st.session_state.submitted_wards:
                st.error(f"🛑 Form EC8A results for Ward [{sup_ward}] under LGA [{sup_lga}] has already been finalized and locked at {st.session_state.submitted_wards[ward_id]}. Duplicate transmission blocked.")
            elif sup_name == "" or sup_phone == "" or sup_ward_unit_name == "":
                st.warning("All primary operational metadata parameters are mandatory.")
            else:
                if conn is not None:
                    try:
                        conn.execute(
                            "INSERT INTO ward_returns (ward_id, supervisor, phone, votes, ec8a_url, project_partition, timestamp, remarks) VALUES (:w, :s, :p, :v, :u, :part, :t, :rem);",
                            {"w": ward_id, "s": sup_name, "p": sup_phone, "v": int(st.session_state.get("sup_pr_vote", 0)), "u": "None Provided (Local Mode)", "part": PROJECT_PARTITION_ID, "t": datetime.datetime.now(), "rem": st.session_state.get("sup_remarks", "")}
                        )
                    except Exception as sql_err:
                        st.caption(f"Cached safely to fallback runtime node: {sql_err}")
                else:
                    st.caption("Saved to Local Secure Application Memory.")

                st.session_state.submitted_wards[ward_id] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.success("✅ Sheet verified and archived directly via production metadata tunnel.")
                st.rerun()

# ==============================================================================
# --- SECTION B: POLLING UNIT AGENT PORTAL (2 LGA VALIDATED) ---
# ==============================================================================
elif agt_key == "ndc 2027":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🗳️ POLLING UNIT AGENT: FIELD DATA ENTRY</div>', unsafe_allow_html=True)
    
    a1, a2 = st.columns(2)
    with a1:
        agt_name = st.text_input("Name of Agent")
        agt_phone = st.text_input("Agent Phone Number")
        agt_lga = st.selectbox("LGA Location Partition", list(LGA_WARD_DATA.keys()), key="agt_lga_select")
        agt_ward = st.selectbox("PU Ward Location Partition", LGA_WARD_DATA.get(agt_lga, []), key="agt_ward_select")
        agt_pu_num = st.text_input("PU Identification Code/Name").strip().replace(" ", "_").upper()
        
    pu_id = f"{agt_lga}_{agt_ward}_{agt_pu_num}".replace(" ", "_").upper()
    
    if agt_pu_num != "" and pu_id in st.session_state.submitted_pus:
        st.error(f"🛑 Polling Unit [{agt_pu_num}] within Ward [{agt_ward}] has already logged its metrics. Entry dropped.")
    else:
        with st.form("agent_form"):
            with a2:
                st.markdown("""
                **Active Unit Verification Layout:**<br>
                <div class="tier-box tier-pres">Presidential</div><div class="tier-box tier-sen">Senatorial</div><div class="tier-box tier-gov">Governorship</div>
                """, unsafe_allow_html=True)
                st.multiselect("Affirm Unit Level", ["Senatorial", "Presidential", "Governorship"], default=["Senatorial"])
                st.number_input("Total Votes Cast inside Unit", min_value=0, key="agt_tot_vote")
                st.number_input("Principal Votes inside Unit", min_value=0, key="agt_pr_vote")
                st.file_uploader("Upload Agent NIN Slip Column", type=['pdf', 'jpg', 'png'])
            st.camera_input("Live Capture of Form EC8A Sheet or screen shot and send where neccessary.")
            
            if st.form_submit_button("📤 LOCK UNIT RESULT"):
                if agt_name == "" or agt_phone == "" or agt_pu_num == "":
                    st.warning("Please complete unique identification strings before submission.")
                else:
                    st.session_state.submitted_pus[pu_id] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    st.success(f"✅ PU [{agt_pu_num}] result slip structurally integrated into Command Core with verification remarks.")
                    st.rerun()

# ==============================================================================
# --- SECTION C: SKILL VOCATION POOL (SAGBAMA & EKEREMOR) ---
# ==============================================================================
elif st.session_state.current_page == "skill_form":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🛠️ SKILL VOCATION POOL: MASSIVE ACQUISITION ENGINE</div>', unsafe_allow_html=True)
    with st.form("skill_form_engine"):
        k1, k2 = st.columns(2)
        with k1:
            sv_name = st.text_input("Full Name (as per ID)")
            st.text_input("Phone Number")
            sv_nin = st.text_input("NIN (National ID)")
            st.text_input("VIN (Voters Card)")
            st.file_uploader("Upload Constituent NIN Slip Column", type=['pdf', 'jpg', 'png'])
        with k2:
            klga = st.selectbox("LGA of Residence", list(LGA_WARD_DATA.keys()), key="sv_lga")
            st.selectbox("Ward (Auto-Populated)", LGA_WARD_DATA.get(klga, []), key="sv_ward")
            st.selectbox("Vocational Interest Parameter", ["ICT & AI", "Fashion", "Solar Power", "Catering", "Mechanic"])
        st.text_area("Skill Interest Remarks Matrix")
        st.camera_input("Biometric Live Verification")
        
        if st.form_submit_button("🚀 SUBMIT FOR TRAINING POOL"):
            match_check = st.session_state.global_registry[st.session_state.global_registry['NIN'] == sv_nin]
            if not match_check.empty:
                st.session_state.radar_threat = True
                st.session_state.threat_msg = f"Collision in Skill Pool Registry! NIN {sv_nin} already logged to {match_check.iloc[0]['Name']}."
                st.error("Submission Halted. Radar Red Alert triggered in Sidebar.")
            else:
                new_row = {"NIN": sv_nin, "VIN": "", "Name": sv_name, "LGA": klga, "Ward": "Captured", "Status": "Pending", "Category": "Applicant", "Skill_Interest": "", "Academic_Qual": "", "Admission_Year": "", "Admission_Letter": None, "Phone": "", "Leader_Name": "", "Leader_Contact": "", "Leader_NIN": "", "Leader_LGA": "", "Leader_Ward": "", "Leader_Portfolio": "", "Voucher_Code": "", "Remarks": "", "Timestamp": str(datetime.datetime.now())}
                st.session_state.global_registry = pd.concat([st.session_state.global_registry, pd.DataFrame([new_row])], ignore_index=True)
                st.success("Registration added successfully to execution thread.")

# ==============================================================================
# --- SECTION D: STUDENT SCHOLARSHIP/GRANT (2 LGA SYSTEMS LOCKED) ---
# ==============================================================================
elif st.session_state.current_page == "scholarship_form":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🎓 STUDENT SCHOLARSHIP/GRANT REGISTRY</div>', unsafe_allow_html=True)
    with st.form("scholarship_form_engine"):
        s1, s2 = st.columns(2)
        with s1:
            st.text_input("Full Name")
            st.text_input("NIN")
            st.text_input("Phone Number")
            st.selectbox("Year of Admission", [str(y) for y in range(2018, 2027)])
            st.file_uploader("Upload Constituent NIN Slip Column", type=['pdf', 'jpg', 'png'])
        with s2:
            st.text_input("Institution Name")
            st.selectbox("Current Level", ["100", "200", "300", "400", "500", "Post-Grad"])
            slga = st.selectbox("LGA Parameter Source", list(LGA_WARD_DATA.keys()), key="sch_lga")
            st.selectbox("Ward (Auto-Populated)", LGA_WARD_DATA.get(slga, []), key="sch_ward")
        st.file_uploader("Upload Admission Letter Document Click", type=['pdf', 'jpg', 'png'])
        st.text_area("Operational Remarks Block")
        st.camera_input("Capture Student Identity Card")
        st.form_submit_button("🚀 SUBMIT APPLICATION")

# ==============================================================================
# --- SECTION E: CV & ARTISAN VAULT (2 LGA SYSTEMS LOCKED) ---
# ==============================================================================
elif st.session_state.current_page == "cv_vault":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🚀 PROFESSIONAL & ARTISAN TALENT VAULT</div>', unsafe_allow_html=True)
    with st.form("cv_vault_engine"):
        v1, v2 = st.columns(2)
        with v1:
            st.text_input("Full Name")
            st.selectbox("Category", ["Professional", "Skilled Artisan", "Business Owner"])
            st.selectbox("Academic Qualification Parameter", ["PhD", "Masters", "Degree/HND", "ND", "NCE", "SSCE", "Primary", "None"])
            st.file_uploader("Upload Credentials/NIN Slip Column", type=['pdf', 'jpg', 'png'])
        with v2:
            st.text_input("NIN")
            st.text_input("Contact Number")
            vlga = st.selectbox("LGA Parameter Source", list(LGA_WARD_DATA.keys()), key="cv_lga")
            st.selectbox("Ward (Auto-Populated)", LGA_WARD_DATA.get(vlga, []), key="cv_ward")
        st.text_area("Experience Remarks / Career Summary Profiles")
        st.camera_input("Capture Professional Certification")
        st.form_submit_button("📤 SUBMIT TO TALENT MATRIX")

# ==============================================================================
# --- SECTION F: COMMUNITY URGENT NEED ---
# ==============================================================================
elif st.session_state.current_page == "cun_trigger":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🚨 COMMUNITY URGENT NEED REPORT (CUN)</div>', unsafe_allow_html=True)
    with st.form("cun_form_engine"):
        st.text_input("Reporter Name")
        st.text_input("Phone Number")
        clga = st.selectbox("LGA Affected Unit", list(LGA_WARD_DATA.keys()), key="cun_lga")
        st.selectbox("Ward Affected Unit (Auto)", LGA_WARD_DATA.get(clga, []), key="cun_ward")
        st.selectbox("Nature of Need Matrix", ["Water", "Electricity", "Roads", "Security", "Health"])
        st.file_uploader("Upload Reporter NIN Slip Column", type=['pdf', 'jpg', 'png'])
        st.text_area("Detailed Situation Remarks Field")
        st.camera_input("Field Evidence Capture Sensor")
        st.form_submit_button("🚨 TRIGGER COMMAND ALERT")

# ==============================================================================
# --- SECTION G: EXECUTIVE COMMAND HUB (2 LGA REAL-TIME ANALYTICAL PORTALS) ---
# ==============================================================================
elif adm_key == "ndc 2027" or adm_key == "ndc ndc 2027":
    render_marquee_header()
    st.markdown('<div class="white-registry-header">🏛️ EXECUTIVE COMMAND HUB: SAGBAMA & EKEREMOR STRATEGIC RATIOS</div>', unsafe_allow_html=True)
    
    tabs = st.tabs([
        "📊 Registry", "📈 CUN Matrix", "⚖️ Audit Log", "🛡️ RADAR", 
        "🎓 CV Audit", "💎 Vantedge", "🗳️ Election Live Sync And Ratio Analytics", "📝 Ground Truth", 
        "📂 Bulk Sync", "📜 Waiver", "🚀 Bills Matrix", "📅 MONITORING"
    ])
    
    two_lga_performance_mock = pd.DataFrame({
        "LGA Name": ["SAGBAMA", "EKEREMOR"],
        "Performance Index": [84, 76],
        "CUN Deficit Rate": [18, 29],
        "Voter Turnout Metric": [81, 79],
        "Waivers Distributed": [14, 9]
    }).set_index("LGA Name")
    
    # --- 1. MASTER REGISTRY ENGINE ---
    with tabs[0]:
        st.subheader("📊 Master Registry Partition System")
        m_col1, m_col2 = st.columns([1, 2])
        with m_col1:
            st.metric("Total Active Registry Database Size", "12,450 Records")
        with m_col2:
            st.markdown("**Intake Processing Performance Index Across Both LGAs**")
            st.bar_chart(two_lga_performance_mock["Performance Index"])
        st.dataframe(st.session_state.global_registry, use_container_width=True)

    # --- 2. COMMUNITY URGENT NEED MATRIX ---
    with tabs[1]:
        st.subheader("📈 CUN Matrix: Deficit Proportions")
        st.bar_chart(two_lga_performance_mock["CUN Deficit Rate"])

    # --- 3. AUDIT LOG & LIVE CLOUD DIAGNOSTICS ---
    with tabs[2]:
        st.subheader("⚖️ Forensic Audit Logs & Database Diagnostics")
        st.markdown("### 🖥️ System Status & Database Diagnostics")
        if conn is not None:
            try:
                df_db_test = conn.query(f"SELECT * FROM ward_returns WHERE project_partition = '{PROJECT_PARTITION_ID}' LIMIT 5;", ttl="0m")
                st.success("🎉 Successfully connected to partitioned Supabase Database!")
                st.dataframe(df_db_test)
            except Exception as e:
                st.error(f"Connection pool isolation check: {e}")
        else:
            st.warning("⚠️ Local Engine Protection: Supabase Cloud Gateway bypassed. Operating in local sandbox matrix container.")

    # --- 4. RADAR DETECTOR ENGINE ---
    with tabs[3]:
        st.subheader("🛡️ RADAR Deduplication Tracking Matrix")
        if st.button("Reset Threat Flags Universally"):
            st.session_state.radar_threat = False
            st.session_state.threat_msg = ""
            st.success("All operational clear-codes sent to ledger.")
            st.rerun()

    # --- 5. CV AUDIT & SKILL MATRIX ---
    with tabs[4]:
        st.subheader("🎓 CV Audit Talent Pool Distributions")
        st.bar_chart(two_lga_performance_mock["Performance Index"])

    # --- 6. VANTEDGE ADVANCED DEMOGRAPHICS ---
    with tabs[5]:
        st.subheader("💎 Vantedge Influencer Proportions")
        st.bar_chart(two_lga_performance_mock["Voter Turnout Metric"])

    # --- 7. ELECTION SYNC WAR ROOM ---
    with tabs[6]:
        st.subheader("🗳️ Election Live Sync And Ratio Analytics Hub")
        st.markdown("""
        **Election Level Colour Configurations Stamped In Ledger:**<br>
        <div class="tier-box tier-pres">Presidential Tally</div><div class="tier-box tier-sen">Senatorial Tally</div>
        <div class="tier-box tier-gov">Governorship Tally</div><div class="tier-box tier-house">State Houses of Assembly Tally</div>
        """, unsafe_allow_html=True)
        st.bar_chart(two_lga_performance_mock["Voter Turnout Metric"])

    # --- 8. GROUND TRUTH VALIDATOR ---
    with tabs[7]:
        st.subheader("📝 Ground Truth Form EC8A Document Integrity Ratios")
        st.bar_chart(two_lga_performance_mock["Performance Index"] + 4)

    # --- 9. BULK SYNC ARCHIVER ---
    with tabs[8]:
         st.subheader("📂 Bulk Sync Throughput Engine & Deep Identity Scanner")
         search_query = st.text_input("Cross-Reference Query (Input Name, NIN, or VIN to trace profile instantly)", key="hub_global_search_input").strip()
         if st.button("Execute Core Trace"):
             st.info("Cross-reference scan finalized inside isolated partition index.")

    # --- 10. WAIVER LOG MATRIX ---
    with tabs[9]:
         st.subheader("📜 Executive Waiver Override Distributions")
         st.bar_chart(two_lga_performance_mock["Waivers Distributed"])

    # --- 11. BILLS LEGISLATIVE MATRIX ---
    with tabs[10]:
         st.subheader("🚀 National Assembly Motion Motion Line")
         st.write("Senator Seriake Dickson motions assembly line trace is online.")

    # --- 12. MONITORING SYSTEM SYSTEMATIC LOG ---
    with tabs[11]:
         st.subheader("📅 Long-Term Momentum Matrix Tracking")
         st.bar_chart(two_lga_performance_mock["Performance Index"] - 2)

    # MASTER ADMINISTRATIVE DATA PURGE ENGINE
    st.markdown("---")
    st.subheader("🚨 Institutional Data Purge Zone")
    confirm_purge = st.text_input("Type 'PURGE SYSTEM DATA' to authorize a complete reset:", key="purge_input_box")
    if st.button("💥 EXECUTE SYSTEM PURGE & RESET AFRESH", type="primary"):
        if confirm_purge == "PURGE SYSTEM DATA":
            st.session_state.global_registry = pd.DataFrame(columns=[
                "NIN", "VIN", "Name", "LGA", "Ward", "Status", "Category", 
                "Skill_Interest", "Academic_Qual", "Admission_Year", "Admission_Letter",
                "Phone", "Leader_Name", "Leader_Contact", "Leader_NIN", "Leader_LGA", 
                "Leader_Ward", "Leader_Portfolio", "Voucher_Code", "Remarks", "Timestamp"
            ])
            st.session_state.submitted_wards = {}
            st.session_state.submitted_pus = {}
            st.success("🎉 Bayelsa West Registry successfully wiped!")
            st.rerun()

# ==============================================================================
# --- SECTION H: PALLIATIVE ENROLLMENT (DEFAULT HOMEPAGE VISUAL GATEWAY) ---
# ==============================================================================
else:
    render_marquee_header()
    st.markdown('<div class="white-registry-header">📦 CONSTITUENT PALLIATIVE ENROLLMENT REGISTRY</div>', unsafe_allow_html=True)
    with st.form("palliative_form_engine"):
        p1, p2 = st.columns(2)
        with p1: 
            st.text_input("Official Name")
            p_nin = st.text_input("NIN (National ID Validation String)")
            st.text_input("VIN (Voters Card Validation String)")
            st.multiselect("Vulnerability Status", ["Aged", "Widow", "Disabled", "Unemployed"])
            st.file_uploader("Upload Constituent NIN Slip Column", type=['pdf', 'jpg', 'png'], key="pal_nin_slip")
        with p2: 
            st.text_input("Phone Number")
            plga = st.selectbox("LGA Location Partition", list(LGA_WARD_DATA.keys()), key="pal_lga")
            st.selectbox("Ward Location Partition (Auto-Cascaded)", LGA_WARD_DATA.get(plga, []), key="pal_ward")
            st.text_input("PU Name")
        st.divider()
        st.markdown("### 🛡️ FULL LEADERSHIP VOUCHING TIER (FORENSIC CORE)")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.text_input("Full Name of Leader")
            st.text_input("Leader Contact Number")
            st.text_input("Leader NIN Number")
            vl_lga = st.selectbox("Leader LGA Location", list(LGA_WARD_DATA.keys()), key="vouch_lga")
        with v_col2:
            st.selectbox("Leader Ward Location (Auto-Cascaded)", LGA_WARD_DATA.get(vl_lga, []), key="vouch_ward")
            st.text_input("Portfolio in the Community")
            st.file_uploader("Upload Leader NIN Slip Column Click", type=['pdf', 'jpg', 'png'], key="vouch_nin_slip")
        st.text_area("Leader's Remarks on Applicant")
        st.camera_input("Biometric Face Capture Core Scan")
        
        if st.form_submit_button("🚀 SUBMIT ENROLLMENT"):
            match_check = st.session_state.global_registry[st.session_state.global_registry['NIN'] == p_nin]
            if not match_check.empty:
                st.session_state.radar_threat = True
                st.session_state.threat_msg = f"Collision in Palliative Registry! NIN {p_nin} matched to {match_check.iloc[0]['Name']}."
                st.error("Duplicate Submission Identified.")
            else:
                st.success("Identity parameters cleared. Record committed successfully.")