# ==============================================================================
# PROJECT: LSOEP TITAN BAYELSA - BRANDING ENGINE
# REVISION: v34.0.5 [HIGH-CONTRAST ROYAL PRESTIGE FULL SPECIFICATION]
# ==============================================================================

import streamlit as st
import base64
import os

def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    except Exception: 
        return ""
    return ""

def apply_regal_styles():
    st.markdown("""
        <style>
        /* Global App Canvas: Deep Velvet Midnight Blue Gradient with Crisp Contrast */
        .stApp { 
            background: linear-gradient(135deg, #020813 0%, #051329 50%, #0a2246 100%) !important; 
        }
        
        /* Form Inputs & Select Boxes: Hardened Crisp Contrast Overrides */
        div[data-baseweb="select"], .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #0b1e36 !important;
            color: #FFFFFF !important;
            border: 2px solid #FFD700 !important;
            border-radius: 10px !important;
            font-weight: 500 !important;
        }
        
        /* Form Container Box Styling */
        div[data-testid="stForm"] {
            background: rgba(11, 30, 54, 0.65) !important;
            border: 2px solid #00E5FF !important;
            border-radius: 15px !important;
            padding: 25px !important;
            box-shadow: 0 4px 20px rgba(0, 229, 255, 0.15) !important;
        }
        
        /* Main Workspace Labels and Text Fixes */
        .stMarkdown p, label[data-testid="stWidgetLabel"] p {
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            letter-spacing: 0.5px;
        }
        
        /* Executive Header Container with Dynamic Polished Gold Pulse */
        @keyframes gold-glow {
            0% { border-color: #FFD700; box-shadow: 0 0 15px rgba(255, 215, 0, 0.4); }
            50% { border-color: #FFF59D; box-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }
            100% { border-color: #FFD700; box-shadow: 0 0 15px rgba(255, 215, 0, 0.4); }
        }
        
        .header-container { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            padding: 30px 50px; 
            background: linear-gradient(180deg, #061a33 0%, #020b17 100%);
            border-radius: 24px; 
            border: 4px solid #FFD700; 
            animation: gold-glow 4s infinite ease-in-out; 
            margin-bottom: 25px;
        }

        /* Tactical Marquee Sub-System Data Stream */
        @keyframes scroll-left {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        .marquee-container {
            background: #FFD700;
            border-radius: 8px;
            padding: 10px 0; 
            margin: 15px 0 25px 0; 
            overflow: hidden; 
            white-space: nowrap;
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
        }
        .marquee-text {
            display: inline-block; 
            font-size: 1.4rem; 
            font-weight: 900; 
            color: #020813;
            animation: scroll-left 20s linear infinite; 
            letter-spacing: 4px; 
            text-transform: uppercase;
        }

        /* Typography Elements Override */
        .gold-title-main { 
            color: #FFD700 !important; 
            font-size: 3rem; 
            font-weight: 900;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.9); 
            text-transform: uppercase; 
            font-family: 'Helvetica Neue', sans-serif;
            margin: 0 0 5px 0;
            letter-spacing: 1px;
        }
        
        .sub-header-white { 
            color: #FFFFFF !important; 
            font-size: 1.3rem; 
            font-weight: 800; 
            letter-spacing: 4px; 
            text-transform: uppercase; 
            margin: 0 0 8px 0;
        }
        
        .white-registry-header {
            background: linear-gradient(90deg, #00E5FF 0%, #0083B0 100%);
            color: #020813 !important;
            padding: 12px 20px;
            font-size: 1.6rem;
            font-weight: 900;
            border-radius: 10px;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(0, 229, 255, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)

def render_marquee():
    st.markdown('<div class="marquee-container"><div class="marquee-text">⚡ NDC NIGERIAN DEMOCRATIC CONGRESS (NDC) IS HERE TO LEAD..... NDC NIGERIAN DEMOCRATIC CONGRESS (NDC) IS HERE TO LEAD..... ⚡</div></div>', unsafe_allow_html=True)

def render_header():
    mace = get_base64_image("assets/mace.png")
    senator = get_base64_image("assets/senator.png")
    
    mace_src = mace if mace != "" else "https://upload.wikimedia.org/wikipedia/commons/e/e4/National_Assembly_of_Nigeria_Seal.svg"
    senator_src = senator if senator != "" else "https://raw.githubusercontent.com/streamlit/explore-co2/main/assets/icon.png"
    
    st.markdown(f'''
        <div class="header-container">
            <img src="{mace_src}" style="width:95px; filter: drop-shadow(0px 0px 8px rgba(255,215,0,0.5));"> 
            <div style="flex-grow: 1; text-align: center; padding: 0 20px;">
                <h1 class="gold-title-main">SENATOR HENRY SERIAKE DICKSON</h1>
                <p class="sub-header-white">NATIONAL ASSEMBLY SENATORIAL COMMAND HUB</p>
                <div style="display:inline-block; background:rgba(0, 229, 255, 0.15); border: 1.5px solid #00E5FF; padding: 6px 20px; border-radius: 30px;">
                    <p style="color:#00E5FF; font-size:1.1rem; font-weight:900; margin:0; letter-spacing: 2px; text-transform:uppercase;">BAYELSA WEST SENATORIAL DISTRICT</p>
                </div>
            </div>
            <img src="{senator_src}" style="width:230px; height:auto; border-radius:16px; border:4px solid #FFD700; box-shadow: 0 0 20px rgba(255,215,0,0.4); object-fit: cover;"> 
        </div>
    ''', unsafe_allow_html=True)