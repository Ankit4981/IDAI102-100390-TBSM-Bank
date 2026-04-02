"""
TBSM Bank · ATM Operational Intelligence  v6
★ Animated Circuit-Board Background  ★ Premium Redesigned Sidebar
★ Deep-Space Nebula App Theme         ★ Neon-Cyber Dark Palette
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from scipy import stats

# ──────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="TBSM Bank · ATM Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────────────────────────
CREDENTIALS = {
    "admin":   {"password": "1234",       "role": "Administrator", "name": "Admin User"},
    "analyst": {"password": "analyst123", "role": "Data Analyst",  "name": "Priya Sharma"},
    "manager": {"password": "mgr123",     "role": "Branch Manager","name": "Rahul Verma"},
}

DAY_ORDER = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

PLOT_BG  = "#06090F"
GRID_CLR = "#111B2E"
TEXT_CLR = "#94A3B8"
C_VIOLET = "#8B5CF6"
C_INDIGO = "#6366F1"
C_CYAN   = "#22D3EE"
C_TEAL   = "#2DD4BF"
C_GREEN  = "#34D399"
C_AMBER  = "#FBBF24"
C_ORANGE = "#FB923C"
C_ROSE   = "#FB7185"
C_PINK   = "#F472B6"
C_SKY    = "#38BDF8"
C_TXT1   = "#F0F4FF"

PALETTE_DARK = [C_CYAN, C_VIOLET, C_AMBER, C_ROSE, C_GREEN, C_PINK, C_SKY]
CL_COLORS  = {"High Demand": C_ROSE, "Medium Demand": C_AMBER, "Low Demand": C_CYAN}
LOC_COLORS = {"Urban": C_INDIGO, "Suburban": C_TEAL, "Rural": C_AMBER}
WX_COLORS  = {"Sunny": C_AMBER, "Cloudy": C_SKY, "Rainy": C_CYAN, "Stormy": C_VIOLET}

# ──────────────────────────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────────────────────────
_DEFAULTS = {
    "authenticated": False, "username": "", "role": "", "login_error": False,
    "current_page": "🏠  Home",
    "cleaning_done": {"convert": True, "encode": True, "normalize": False, "errors": True},
    "strategy_applied": False, "simulation_run": False, "sim_pct": 20, "investigated": [],
}
for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ══════════════════════════════════════════════════════════════════
# ████████████  GLOBAL CSS — v6 FULL REDESIGN  ████████████
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

/* ════════════════════════════════════════════
   ROOT VARIABLES
════════════════════════════════════════════ */
:root {
    --bg:        #03050A;
    --bg2:       #060912;
    --surf:      #0C1425;
    --surf2:     #101B33;
    --surf3:     #152040;

    --c1: #6366F1; --c2: #22D3EE; --cv: #8B5CF6; --cr: #FB7185;
    --cg: #34D399; --ca: #FBBF24; --co: #FB923C; --ct: #2DD4BF;
    --cs: #38BDF8; --cp: #F472B6;

    --t1: #F0F4FF; --t2: #CBD5E1; --t3: #94A3B8; --t4: #64748B;

    --bdr:  rgba(255,255,255,0.06);
    --bdr-c:rgba(34,211,238,0.18);
    --bdr-v:rgba(139,92,246,0.18);

    --gm: linear-gradient(135deg,#6366F1,#8B5CF6,#22D3EE);
    --gf: linear-gradient(135deg,#FB7185,#F472B6);
    --go: linear-gradient(135deg,#22D3EE,#2DD4BF);
    --gg: linear-gradient(135deg,#FBBF24,#FB923C);
    --gn: linear-gradient(135deg,#34D399,#22D3EE);

    --nc: 0 0 22px rgba(34,211,238,.5), 0 0 65px rgba(34,211,238,.18);
    --nv: 0 0 22px rgba(139,92,246,.5), 0 0 65px rgba(139,92,246,.18);
    --nr: 0 0 22px rgba(251,113,133,.5), 0 0 65px rgba(251,113,133,.18);
    --ng: 0 0 22px rgba(52,211,153,.5),  0 0 65px rgba(52,211,153,.18);
}

/* ════════════════════════════════════════════
   BASE RESET
════════════════════════════════════════════ */
* { box-sizing: border-box; }
html,body,[class*="css"] { font-family:'Syne',sans-serif !important; }
#MainMenu,footer { visibility:hidden; }
header[data-testid="stHeader"] { background:transparent !important; }

::-webkit-scrollbar { width:4px; height:4px; }
::-webkit-scrollbar-track { background:#040609; }
::-webkit-scrollbar-thumb {
    background:linear-gradient(180deg,#8B5CF6,#22D3EE);
    border-radius:4px;
}

/* ════════════════════════════════════════════
   ██  ANIMATED BACKGROUND — Deep Space Nebula  ██
════════════════════════════════════════════ */
.stApp {
    background: #03050A !important;
    color: var(--t1) !important;
    position: relative !important;
}

/* Main background canvas — pseudo-element approach via body injection */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;

    /* Layered radial nebula clouds */
    background:
        /* Top-left violet nebula */
        radial-gradient(ellipse 55% 45% at 8% 12%,
            rgba(99,102,241,0.22) 0%,
            rgba(99,102,241,0.08) 40%,
            transparent 70%),
        /* Right cyan nebula */
        radial-gradient(ellipse 45% 55% at 92% 20%,
            rgba(34,211,238,0.18) 0%,
            rgba(34,211,238,0.06) 45%,
            transparent 70%),
        /* Center-bottom violet-rose blend */
        radial-gradient(ellipse 60% 40% at 50% 88%,
            rgba(139,92,246,0.16) 0%,
            rgba(251,113,133,0.06) 50%,
            transparent 75%),
        /* Mid-left teal accent */
        radial-gradient(ellipse 35% 50% at 18% 62%,
            rgba(45,212,191,0.10) 0%,
            transparent 65%),
        /* Far right warm */
        radial-gradient(ellipse 40% 35% at 85% 75%,
            rgba(251,191,36,0.07) 0%,
            transparent 60%),
        /* Deep base */
        linear-gradient(160deg, #040710 0%, #03050A 35%, #050912 65%, #030508 100%);

    animation: nebula_drift 28s ease-in-out infinite alternate;
}

@keyframes nebula_drift {
    0%   { filter: hue-rotate(0deg) brightness(1);   }
    33%  { filter: hue-rotate(8deg)  brightness(1.04); }
    66%  { filter: hue-rotate(-5deg) brightness(0.97); }
    100% { filter: hue-rotate(12deg) brightness(1.02); }
}

/* Circuit-grid overlay */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background-image:
        /* Horizontal lines */
        linear-gradient(rgba(34,211,238,0.028) 1px, transparent 1px),
        /* Vertical lines */
        linear-gradient(90deg, rgba(34,211,238,0.028) 1px, transparent 1px),
        /* Larger grid */
        linear-gradient(rgba(99,102,241,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,102,241,0.015) 1px, transparent 1px);
    background-size: 40px 40px, 40px 40px, 160px 160px, 160px 160px;
    animation: grid_scroll 80s linear infinite;
}

@keyframes grid_scroll {
    0%   { background-position: 0 0, 0 0, 0 0, 0 0; }
    100% { background-position: 40px 40px, 40px 40px, 160px 160px, 160px 160px; }
}

/* Ensure all stApp children sit above backgrounds */
.stApp > * { position: relative; z-index: 1; }
[data-testid="stSidebar"],
[data-testid="stMain"],
.stMain,
[data-testid="block-container"] { position: relative; z-index: 1; }

/* Floating ambient orbs — injected via HTML below */
@keyframes orb_float_a {
    0%,100% { transform:translate(0,0) scale(1); opacity:.55; }
    30%     { transform:translate(22px,-28px) scale(1.06); opacity:.75; }
    70%     { transform:translate(-18px,16px) scale(.94); opacity:.45; }
}
@keyframes orb_float_b {
    0%,100% { transform:translate(0,0) scale(1); opacity:.4; }
    40%     { transform:translate(-30px,22px) scale(1.1); opacity:.6; }
    80%     { transform:translate(25px,-20px) scale(.9); opacity:.3; }
}
@keyframes orb_float_c {
    0%,100% { transform:translate(0,0) scale(1); opacity:.3; }
    50%     { transform:translate(18px,24px) scale(1.08); opacity:.5; }
}

/* ════════════════════════════════════════════
   ██  PREMIUM SIDEBAR v6  ██
════════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: transparent !important;
    min-width: 262px !important;
    max-width: 278px !important;
    position: relative !important;
    border-right: none !important;
    box-shadow: none !important;
    z-index: 10 !important;
}

/* Sidebar glass-panel background */
[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg,
        rgba(5,8,18,0.97) 0%,
        rgba(6,10,22,0.96) 30%,
        rgba(5,9,20,0.97) 65%,
        rgba(4,7,16,0.98) 100%);
    backdrop-filter: blur(28px) saturate(1.4);
    -webkit-backdrop-filter: blur(28px) saturate(1.4);
    z-index: -1;
    border-right: 1px solid rgba(34,211,238,0.1);
}

/* Right-edge glow line with scanning animation */
[data-testid="stSidebar"]::after {
    content: '';
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 2px;
    z-index: 20;
    background: linear-gradient(180deg,
        transparent 0%,
        rgba(34,211,238,0.0) 5%,
        rgba(34,211,238,0.9) 30%,
        rgba(139,92,246,1.0) 55%,
        rgba(34,211,238,0.9) 80%,
        rgba(34,211,238,0.0) 95%,
        transparent 100%);
    box-shadow: 0 0 12px rgba(34,211,238,0.6), 0 0 30px rgba(139,92,246,0.3);
    animation: sb_edge_scan 4.5s ease-in-out infinite;
}

@keyframes sb_edge_scan {
    0%,100% { opacity:.35; box-shadow:0 0 8px rgba(34,211,238,.4); }
    50%     { opacity:1;   box-shadow:0 0 16px rgba(34,211,238,.8), 0 0 40px rgba(139,92,246,.4); }
}

[data-testid="stSidebar"] * { color: var(--t2) !important; }
[data-testid="stSidebar"] > div:first-child { padding:0 !important; }
[data-testid="stSidebarResizeHandle"] { display:none !important; }
[data-testid="stSidebar"] ::-webkit-scrollbar { display:none !important; }

/* Kill all default spacing */
[data-testid="stSidebar"] .stButton,
[data-testid="stSidebar"] .element-container,
[data-testid="stSidebar"] [data-testid="stElementContainer"],
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"],
[data-testid="stSidebar"] .stMarkdown {
    margin:0 !important; padding:0 !important;
}
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap:0 !important; padding:0 !important; }

/* Nav buttons base */
[data-testid="stSidebar"] .stButton > button {
    width:100% !important; background:transparent !important;
    border:none !important; border-left:2px solid transparent !important;
    border-radius:0 !important; text-align:left !important;
    padding:10px 18px !important; font-family:'Syne',sans-serif !important;
    font-size:0.83rem !important; font-weight:600 !important;
    color:rgba(148,163,184,0.45) !important; letter-spacing:0.3px !important;
    box-shadow:none !important; transition:all .22s ease !important;
    min-height:0 !important; height:auto !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background:linear-gradient(90deg,rgba(34,211,238,0.09) 0%,rgba(99,102,241,0.04) 60%,transparent 100%) !important;
    color:#E2E8F0 !important; border-left-color:rgba(34,211,238,0.5) !important;
    transform:translateX(4px) !important;
    box-shadow:inset 0 0 18px rgba(34,211,238,0.04) !important;
}

/* Active nav — full neon treatment */
[data-testid="stSidebar"] .nav-active .stButton > button {
    background:linear-gradient(90deg,
        rgba(34,211,238,0.16) 0%,
        rgba(99,102,241,0.09) 55%,
        transparent 100%) !important;
    color:#F8FAFF !important;
    border-left:2px solid var(--c2) !important;
    font-weight:700 !important;
    box-shadow:
        inset 0 0 30px rgba(34,211,238,0.07),
        -3px 0 24px rgba(34,211,238,0.35) !important;
    text-shadow:0 0 14px rgba(34,211,238,0.45) !important;
    letter-spacing:0.4px !important;
}

/* Sign out button */
[data-testid="stSidebar"] .sb-signout .stButton > button {
    background:rgba(251,113,133,0.07) !important;
    border:1px solid rgba(251,113,133,0.22) !important;
    border-radius:11px !important; color:#fb7185 !important;
    font-weight:700 !important; justify-content:center !important;
    padding:9px 14px !important; font-size:0.8rem !important;
    box-shadow:0 0 22px rgba(251,113,133,0.09) !important;
    transition:all .25s !important;
}
[data-testid="stSidebar"] .sb-signout .stButton > button:hover {
    background:rgba(251,113,133,0.13) !important;
    box-shadow:0 0 32px rgba(251,113,133,0.22), inset 0 0 18px rgba(251,113,133,0.07) !important;
    transform:none !important;
}

/* ════════════════════════════════════════════
   INPUTS
════════════════════════════════════════════ */
.stTextInput > div > div > input {
    background:rgba(11,17,35,0.9) !important;
    border:1.5px solid rgba(255,255,255,0.07) !important;
    border-radius:11px !important; color:var(--t1) !important;
    font-family:'Syne',sans-serif !important; font-size:.93rem !important;
    padding:13px 16px !important; transition:all .3s !important;
    backdrop-filter:blur(10px) !important;
}
.stTextInput > div > div > input:focus {
    border-color:var(--c2) !important;
    box-shadow:0 0 0 3px rgba(34,211,238,.12), var(--nc) !important;
    background:rgba(14,22,44,0.95) !important;
}
.stTextInput > label {
    font-size:.65rem !important; font-weight:700 !important;
    letter-spacing:2.2px !important; text-transform:uppercase !important;
    color:var(--t4) !important;
}

/* ════════════════════════════════════════════
   BUTTONS
════════════════════════════════════════════ */
.stButton > button {
    background:var(--gm) !important; color:#fff !important;
    font-family:'Rajdhani',sans-serif !important; font-weight:700 !important;
    border:none !important; border-radius:11px !important;
    padding:12px 28px !important; font-size:1rem !important;
    width:100% !important; letter-spacing:1px !important;
    transition:all .3s cubic-bezier(.34,1.56,.64,1) !important;
    box-shadow:0 4px 24px rgba(99,102,241,.4) !important;
}
.stButton > button:hover {
    transform:translateY(-3px) scale(1.02) !important;
    box-shadow:0 12px 40px rgba(99,102,241,.6), var(--nv) !important;
}
.stButton > button:disabled { opacity:.35 !important; transform:none !important; box-shadow:none !important; }

/* ════════════════════════════════════════════
   SELECTBOX / MULTISELECT
════════════════════════════════════════════ */
.stSelectbox > div > div, .stMultiSelect > div > div {
    background:rgba(11,17,35,0.9) !important;
    border:1.5px solid rgba(255,255,255,0.07) !important;
    border-radius:11px !important; color:var(--t1) !important;
}

/* ════════════════════════════════════════════
   TABS
════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background:rgba(8,12,24,0.85) !important;
    border-radius:14px !important; padding:5px !important;
    gap:4px !important; border:1px solid rgba(255,255,255,0.05) !important;
    backdrop-filter:blur(12px) !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius:10px !important; color:var(--t4) !important;
    font-family:'Rajdhani',sans-serif !important; font-size:.88rem !important;
    font-weight:600 !important; padding:9px 20px !important;
    transition:all .2s !important;
}
.stTabs [aria-selected="true"] {
    background:linear-gradient(135deg,rgba(34,211,238,.15),rgba(99,102,241,.09)) !important;
    color:var(--c2) !important;
    box-shadow:0 0 20px rgba(34,211,238,.2),inset 0 0 18px rgba(34,211,238,.05) !important;
    border:1px solid rgba(34,211,238,.18) !important;
}

/* ════════════════════════════════════════════
   DATAFRAME
════════════════════════════════════════════ */
.stDataFrame {
    border-radius:14px !important; overflow:hidden !important;
    border:1px solid rgba(34,211,238,.1) !important;
    box-shadow:0 0 28px rgba(34,211,238,.04) !important;
}
div[data-testid="stExpander"] {
    background:rgba(10,15,28,0.8) !important;
    border:1px solid var(--bdr) !important;
    border-radius:14px !important;
    backdrop-filter:blur(10px) !important;
}

/* ════════════════════════════════════════════
   TOPBAR
════════════════════════════════════════════ */
.topbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:18px 0 22px; margin-bottom:32px;
    border-bottom:1px solid rgba(255,255,255,0.05);
    position:relative;
}
.topbar::after {
    content:''; position:absolute; bottom:-1px; left:0; height:2px;
    background:linear-gradient(90deg,var(--c2),var(--cv),transparent);
    border-radius:2px; box-shadow:0 0 14px rgba(34,211,238,.55);
    animation:tb_w 3.5s ease-in-out infinite;
}
@keyframes tb_w {
    0%,100%{ width:80px; opacity:.7; }
    50%    { width:220px; opacity:1; }
}
.topbar-title {
    font-family:'Orbitron',sans-serif; font-size:1.05rem; font-weight:700;
    color:var(--t1); display:flex; align-items:center; gap:14px; letter-spacing:1.5px;
}
.tb-bar {
    width:3px; height:24px;
    background:linear-gradient(180deg,var(--c2),var(--cv));
    border-radius:2px; box-shadow:0 0 12px rgba(34,211,238,.7);
    animation:bar_p 2s ease-in-out infinite;
}
@keyframes bar_p {
    0%,100%{ box-shadow:0 0 8px rgba(34,211,238,.5); }
    50%    { box-shadow:0 0 22px rgba(34,211,238,.9),0 0 40px rgba(139,92,246,.3); }
}
.topbar-right { display:flex; align-items:center; gap:10px; }
.tb-badge {
    display:flex; align-items:center; gap:8px;
    background:rgba(8,13,28,0.92); border:1px solid rgba(255,255,255,0.07);
    border-radius:12px; padding:8px 14px;
    font-size:.76rem; font-weight:600; color:var(--t2);
    backdrop-filter:blur(12px);
    box-shadow:0 4px 18px rgba(0,0,0,.35);
}
.tb-avatar {
    width:30px; height:30px; border-radius:8px; background:var(--gm);
    display:inline-flex; align-items:center; justify-content:center;
    font-size:.72rem; font-weight:800; color:#fff;
    box-shadow:0 0 12px rgba(99,102,241,.5);
}
.live-dot {
    width:7px; height:7px; border-radius:50%;
    background:var(--cg);
    box-shadow:0 0 8px var(--cg),0 0 18px rgba(52,211,153,.4);
    animation:pd 2s infinite; display:inline-block;
}
@keyframes pd {
    0%,100%{ box-shadow:0 0 0 0 rgba(52,211,153,.6); }
    50%    { box-shadow:0 0 0 5px rgba(52,211,153,0); }
}
.tb-alert {
    display:flex; align-items:center; gap:6px;
    background:rgba(251,113,133,.08); border:1px solid rgba(251,113,133,.24);
    border-radius:12px; padding:8px 14px;
    font-size:.76rem; font-weight:700; color:var(--cr);
    box-shadow:0 0 22px rgba(251,113,133,.1);
}

/* ════════════════════════════════════════════
   KPI CARDS — glassmorphism + glow
════════════════════════════════════════════ */
.kpi-card {
    background:linear-gradient(135deg,rgba(10,15,28,0.85) 0%,rgba(8,12,24,0.9) 100%);
    border:1px solid var(--bdr); border-radius:20px; padding:22px;
    position:relative; overflow:hidden;
    transition:all .35s cubic-bezier(.4,0,.2,1);
    backdrop-filter:blur(16px) !important;
    box-shadow:0 4px 24px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
}
.kpi-card::before {
    content:''; position:absolute; left:0; top:0; bottom:0;
    width:3px; border-radius:20px 0 0 20px;
}
.kpi-card::after {
    content:''; position:absolute; top:-55px; right:-55px;
    width:130px; height:130px; border-radius:50%; opacity:.04; transition:all .4s;
}
.kpi-card.indigo::before{ background:var(--gm); box-shadow:0 0 16px rgba(99,102,241,.75); }
.kpi-card.teal::before  { background:var(--go); box-shadow:0 0 16px rgba(45,212,191,.75); }
.kpi-card.amber::before { background:var(--gg); box-shadow:0 0 16px rgba(251,191,36,.75); }
.kpi-card.rose::before  { background:var(--gf); box-shadow:0 0 16px rgba(251,113,133,.75); }
.kpi-card.green::before { background:var(--gn); box-shadow:0 0 16px rgba(52,211,153,.75); }
.kpi-card.violet::before{ background:var(--gm); box-shadow:0 0 16px rgba(139,92,246,.75); }
.kpi-card.indigo::after { background:#6366F1; }
.kpi-card.teal::after   { background:#2DD4BF; }
.kpi-card.amber::after  { background:#FBBF24; }
.kpi-card.rose::after   { background:#FB7185; }
.kpi-card.green::after  { background:#34D399; }
.kpi-card.violet::after { background:#8B5CF6; }
.kpi-card:hover {
    transform:translateY(-6px);
    border-color:rgba(255,255,255,.13);
    box-shadow:0 20px 55px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.06);
}
.kpi-card:hover::after { opacity:.1; width:160px; height:160px; }
.kpi-card.indigo:hover{ box-shadow:0 0 45px rgba(99,102,241,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-card.teal:hover  { box-shadow:0 0 45px rgba(45,212,191,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-card.amber:hover { box-shadow:0 0 45px rgba(251,191,36,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-card.rose:hover  { box-shadow:0 0 45px rgba(251,113,133,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-card.green:hover { box-shadow:0 0 45px rgba(52,211,153,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-card.violet:hover{ box-shadow:0 0 45px rgba(139,92,246,.22),0 20px 55px rgba(0,0,0,.45); }
.kpi-ico {
    width:46px; height:46px; border-radius:13px;
    display:flex; align-items:center; justify-content:center;
    font-size:1.3rem; margin-bottom:16px; transition:all .3s;
}
.kpi-card:hover .kpi-ico { transform:scale(1.12); }
.kpi-ico.indigo{ background:rgba(99,102,241,.14); border:1px solid rgba(99,102,241,.3); box-shadow:0 0 14px rgba(99,102,241,.2); }
.kpi-ico.teal  { background:rgba(45,212,191,.14); border:1px solid rgba(45,212,191,.3); box-shadow:0 0 14px rgba(45,212,191,.2); }
.kpi-ico.amber { background:rgba(251,191,36,.14);  border:1px solid rgba(251,191,36,.3);  box-shadow:0 0 14px rgba(251,191,36,.2); }
.kpi-ico.rose  { background:rgba(251,113,133,.14); border:1px solid rgba(251,113,133,.3); box-shadow:0 0 14px rgba(251,113,133,.2); }
.kpi-ico.green { background:rgba(52,211,153,.14);  border:1px solid rgba(52,211,153,.3);  box-shadow:0 0 14px rgba(52,211,153,.2); }
.kpi-ico.violet{ background:rgba(139,92,246,.14);  border:1px solid rgba(139,92,246,.3);  box-shadow:0 0 14px rgba(139,92,246,.2); }
.kpi-lbl  { font-size:.59rem; font-weight:700; letter-spacing:2.5px; text-transform:uppercase; color:var(--t4); margin-bottom:7px; }
.kpi-val  { font-family:'Orbitron',sans-serif; font-size:1.6rem; font-weight:800; color:var(--t1); line-height:1; text-shadow:0 0 24px rgba(255,255,255,.1); }
.kpi-sub  { font-size:.72rem; color:var(--t4); margin-top:7px; }
.kpi-up   { font-size:.72rem; font-weight:700; color:var(--cg); margin-top:6px; }
.kpi-dn   { font-size:.72rem; font-weight:700; color:var(--cr); margin-top:6px; }

/* ════════════════════════════════════════════
   BANNERS
════════════════════════════════════════════ */
.ok-banner {
    background:rgba(52,211,153,.08); border:1px solid rgba(52,211,153,.24);
    border-radius:14px; padding:15px 20px; font-size:.86rem;
    color:var(--cg); font-weight:600; margin-bottom:18px;
    display:flex; align-items:center; gap:10px;
    box-shadow:0 0 28px rgba(52,211,153,.07);
    backdrop-filter:blur(10px);
}
.warn-banner {
    background:rgba(251,191,36,.08); border:1px solid rgba(251,191,36,.24);
    border-radius:14px; padding:15px 20px; font-size:.86rem;
    color:var(--ca); font-weight:600; margin-bottom:18px;
    display:flex; align-items:center; gap:10px;
}

/* ════════════════════════════════════════════
   INSIGHT BOX
════════════════════════════════════════════ */
.insight-box {
    background:linear-gradient(135deg,rgba(34,211,238,.06),rgba(99,102,241,.03));
    border:1px solid rgba(34,211,238,.17); border-left:3px solid var(--c2);
    border-radius:0 13px 13px 0; padding:14px 18px;
    font-size:.84rem; color:var(--t2); margin-top:14px; line-height:1.72;
    box-shadow:0 0 26px rgba(34,211,238,.04);
    backdrop-filter:blur(8px);
}
.insight-box strong { color:var(--c2); }

/* ════════════════════════════════════════════
   SECTION HEADER
════════════════════════════════════════════ */
.sec-h {
    font-family:'Orbitron',sans-serif; font-size:1.35rem; font-weight:800;
    color:var(--t1); margin-bottom:5px; letter-spacing:1.5px;
    text-shadow:0 0 28px rgba(255,255,255,.07);
}
.sec-s { font-size:.86rem; color:var(--t4); margin-bottom:28px; letter-spacing:.3px; }

/* ════════════════════════════════════════════
   GLASS PANEL (generic dark card)
════════════════════════════════════════════ */
.glass-panel {
    background:linear-gradient(135deg,rgba(8,12,24,0.88),rgba(6,10,20,0.92));
    border:1px solid var(--bdr-c); border-radius:19px; padding:24px;
    backdrop-filter:blur(18px);
    box-shadow:0 0 42px rgba(34,211,238,.05), inset 0 1px 0 rgba(255,255,255,.04);
}
.gp-title {
    display:flex; align-items:center; gap:10px;
    font-family:'Orbitron',sans-serif; font-weight:700; font-size:.84rem;
    margin-bottom:22px; color:var(--t1); letter-spacing:.5px;
}
.gp-icon {
    width:34px; height:34px; border-radius:9px;
    background:rgba(34,211,238,.1); border:1px solid rgba(34,211,238,.22);
    display:flex; align-items:center; justify-content:center; font-size:.95rem;
    box-shadow:0 0 12px rgba(34,211,238,.15);
}
.gp-status {
    display:flex; justify-content:space-between;
    font-size:.59rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase;
    color:var(--t4); border-top:1px solid rgba(255,255,255,.05);
    margin-top:18px; padding-top:14px;
}
.live-label { color:var(--cg); text-shadow:0 0 8px rgba(52,211,153,.55); }

/* ════════════════════════════════════════════
   STEP CARDS
════════════════════════════════════════════ */
.step-card {
    background:rgba(10,15,28,0.82); border:1px solid var(--bdr);
    border-radius:16px; padding:20px 22px;
    display:flex; align-items:center; gap:16px;
    margin-bottom:11px; transition:all .25s;
    backdrop-filter:blur(12px);
    box-shadow:0 4px 18px rgba(0,0,0,.22);
}
.step-card.done-card {
    border-color:rgba(52,211,153,.24);
    background:linear-gradient(135deg,rgba(52,211,153,.04),rgba(8,12,24,0.9));
    box-shadow:0 0 22px rgba(52,211,153,.06);
}
.step-ico { width:46px; height:46px; border-radius:13px; display:flex; align-items:center; justify-content:center; font-size:1.3rem; flex-shrink:0; }
.step-ico.done   { background:rgba(52,211,153,.12); border:1px solid rgba(52,211,153,.25); box-shadow:0 0 14px rgba(52,211,153,.18); }
.step-ico.pend   { background:rgba(251,191,36,.12);  border:1px solid rgba(251,191,36,.25); }
.step-info { flex:1; }
.step-title { font-family:'Rajdhani',sans-serif; font-weight:700; font-size:1rem; color:var(--t1); margin-bottom:3px; }
.step-desc  { font-size:.8rem; color:var(--t3); }
.badge-done { background:rgba(52,211,153,.12); color:var(--cg); font-size:.59rem; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; border-radius:20px; padding:4px 12px; white-space:nowrap; border:1px solid rgba(52,211,153,.25); box-shadow:0 0 10px rgba(52,211,153,.14); }
.badge-pend { background:rgba(251,191,36,.12); color:var(--ca); font-size:.59rem; font-weight:800; letter-spacing:.8px; text-transform:uppercase; border-radius:20px; padding:4px 13px; white-space:nowrap; border:1px solid rgba(251,191,36,.24); }

/* ════════════════════════════════════════════
   ANOMALY CARDS
════════════════════════════════════════════ */
.anom-card {
    background:linear-gradient(135deg,rgba(10,15,28,0.88),rgba(8,12,24,0.92));
    border:1px solid var(--bdr); border-radius:16px;
    padding:20px 22px; margin-bottom:12px;
    transition:all .3s cubic-bezier(.4,0,.2,1);
    position:relative; overflow:hidden;
    backdrop-filter:blur(14px);
}
.anom-card::after {
    content:''; position:absolute; right:0; top:0; bottom:0;
    width:3px; background:var(--ca); border-radius:0 16px 16px 0;
    box-shadow:0 0 14px rgba(251,191,36,.5);
}
.anom-card:hover { box-shadow:0 8px 38px rgba(251,113,133,.12); transform:translateX(-3px) translateY(-2px); border-color:rgba(251,113,133,.2); }
.anom-card.high-risk::after { background:var(--cr); box-shadow:0 0 20px rgba(251,113,133,.6); }
.anom-card.investigated    { border-color:rgba(52,211,153,.25); background:rgba(52,211,153,.04); }
.anom-card.investigated::after { background:var(--cg); box-shadow:0 0 14px rgba(52,211,153,.5); }
.anom-hdr { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; }
.anom-row { display:flex; align-items:center; gap:12px; }
.anom-ico { width:42px; height:42px; border-radius:11px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; }
.anom-ico.warn  { background:rgba(251,191,36,.12); border:1px solid rgba(251,191,36,.2); }
.anom-ico.alert { background:rgba(251,113,133,.12); border:1px solid rgba(251,113,133,.2); }
.anom-ico.ok    { background:rgba(52,211,153,.12);  border:1px solid rgba(52,211,153,.2); }
.anom-date { font-size:.7rem; color:var(--c2); font-weight:700; margin-bottom:2px; letter-spacing:.5px; }
.anom-name { font-size:.94rem; font-weight:700; color:var(--t1); }
.anom-val  { font-family:'Orbitron',sans-serif; font-size:1.2rem; font-weight:700; color:var(--t1); text-align:right; }
.anom-lbl  { font-size:.62rem; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:var(--t4); text-align:right; }
.risk-pill { display:inline-flex; align-items:center; gap:4px; border-radius:20px; padding:3px 10px; font-size:.68rem; font-weight:800; letter-spacing:.5px; }
.risk-pill.high{ background:rgba(251,113,133,.12); color:var(--cr); border:1px solid rgba(251,113,133,.25); box-shadow:0 0 10px rgba(251,113,133,.15); }
.risk-pill.med { background:rgba(251,191,36,.12);  color:var(--ca); border:1px solid rgba(251,191,36,.25); }
.risk-pill.low { background:rgba(52,211,153,.12);  color:var(--cg); border:1px solid rgba(52,211,153,.25); }
.risk-pill.done{ background:rgba(52,211,153,.12);  color:var(--cg); border:1px solid rgba(52,211,153,.25); }
.anom-reason {
    background:rgba(4,6,14,0.85); border:1px solid rgba(255,255,255,.05);
    border-radius:9px; padding:9px 13px;
    font-size:.8rem; color:var(--t3); margin-top:9px; line-height:1.55;
}
.anom-reason strong { color:var(--c2); }

/* ════════════════════════════════════════════
   STORY CARDS
════════════════════════════════════════════ */
.story-card {
    background:linear-gradient(135deg,rgba(10,15,28,0.85),rgba(8,12,24,0.9));
    border:1px solid var(--bdr); border-radius:18px; padding:26px;
    margin-bottom:14px; transition:all .25s;
    backdrop-filter:blur(14px);
    box-shadow:0 4px 18px rgba(0,0,0,.2);
}
.story-card:hover {
    box-shadow:0 0 48px rgba(99,102,241,.12),0 10px 38px rgba(0,0,0,.28);
    border-color:rgba(99,102,241,.2); transform:translateX(3px);
}
.story-content { flex:1; }
.story-title { font-family:'Rajdhani',sans-serif; font-weight:700; font-size:1.05rem; color:var(--t1); margin-bottom:9px; }
.story-text  { font-size:.84rem; color:var(--t3); line-height:1.72; }
.story-tag   { display:inline-block; background:rgba(99,102,241,.12); color:var(--c1); border:1px solid rgba(99,102,241,.22); border-radius:7px; padding:4px 11px; font-size:.68rem; font-weight:700; margin-top:11px; }

/* ════════════════════════════════════════════
   BIZ CARDS
════════════════════════════════════════════ */
.biz-card {
    background:rgba(10,15,28,0.8); border:1px solid var(--bdr);
    border-radius:11px; padding:15px 18px;
    display:flex; align-items:flex-start; gap:12px;
    margin-bottom:10px; transition:all .2s;
    backdrop-filter:blur(10px);
}
.biz-card:hover { border-color:rgba(99,102,241,.22); box-shadow:0 4px 18px rgba(99,102,241,.08); transform:translateX(2px); }
.biz-num { width:29px; height:29px; background:var(--gm); color:#fff; border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron',sans-serif; font-size:.72rem; font-weight:700; flex-shrink:0; box-shadow:0 0 12px rgba(99,102,241,.3); }
.biz-text { font-size:.86rem; color:var(--t2); line-height:1.62; }

/* ════════════════════════════════════════════
   HERO INSIGHTS
════════════════════════════════════════════ */
.hero-insights {
    background:linear-gradient(150deg,rgba(6,10,20,.98) 0%,rgba(12,9,40,.95) 50%,rgba(8,26,44,.95) 100%);
    border:1px solid rgba(139,92,246,.2); border-radius:22px;
    padding:50px 46px; color:var(--t1); position:relative; overflow:hidden;
    backdrop-filter:blur(20px);
    box-shadow:0 0 60px rgba(139,92,246,.08);
}
.hero-insights::before {
    content:''; position:absolute; right:-80px; top:-80px; width:340px; height:340px;
    background:radial-gradient(circle,rgba(139,92,246,.17) 0%,transparent 70%);
    border-radius:50%; animation:h_orb 8s ease-in-out infinite;
}
.hero-insights::after {
    content:''; position:absolute; left:15%; bottom:-60px; width:250px; height:250px;
    background:radial-gradient(circle,rgba(34,211,238,.1) 0%,transparent 70%);
    border-radius:50%; animation:h_orb 10s ease-in-out infinite 2s;
}
@keyframes h_orb { 0%,100%{transform:translate(0,0) scale(1);} 50%{transform:translate(20px,-20px) scale(1.1);} }
.hero-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1);
    border-radius:20px; padding:5px 16px;
    font-size:.65rem; font-weight:700; letter-spacing:2px; text-transform:uppercase;
    color:var(--t3); margin-bottom:20px; position:relative; z-index:1;
}
.hero-title {
    font-family:'Orbitron',sans-serif; font-size:2.1rem; font-weight:900;
    line-height:1.15; margin-bottom:18px; position:relative; z-index:1; letter-spacing:1px;
}
.hero-title .hl  { color:var(--c2); text-shadow:0 0 30px rgba(34,211,238,.4); }
.hero-title .hl2 { color:var(--cv); text-shadow:0 0 30px rgba(139,92,246,.4); }
.hero-body { font-size:.9rem; color:var(--t3); line-height:1.85; position:relative; z-index:1; max-width:580px; margin-bottom:28px; }
.hero-body strong { color:var(--t1); }

/* ════════════════════════════════════════════
   SIM RESULT
════════════════════════════════════════════ */
.sim-result {
    background:linear-gradient(135deg,rgba(52,211,153,.06),rgba(34,211,238,.03));
    border:1px solid rgba(52,211,153,.22); border-radius:18px; padding:30px;
    text-align:center; margin-top:16px;
    box-shadow:0 0 48px rgba(52,211,153,.07);
    backdrop-filter:blur(14px);
}
.sim-val { font-family:'Orbitron',sans-serif; font-size:2.4rem; font-weight:900; color:var(--cg); text-shadow:0 0 38px rgba(52,211,153,.6),0 0 80px rgba(52,211,153,.2); }

/* ════════════════════════════════════════════
   FEATURE CARDS
════════════════════════════════════════════ */
.feat-card {
    border-radius:18px; padding:28px 24px; height:100%;
    border:1px solid rgba(255,255,255,.08);
    transition:all .35s cubic-bezier(.4,0,.2,1);
    position:relative; overflow:hidden;
    box-shadow:0 8px 32px rgba(0,0,0,.4);
}
.feat-card::before {
    content:''; position:absolute; inset:0;
    background:rgba(0,0,0,.15); border-radius:18px;
    opacity:0; transition:opacity .3s;
}
.feat-card:hover { transform:translateY(-7px) scale(1.01); box-shadow:0 22px 62px rgba(0,0,0,.5),0 0 42px rgba(255,255,255,.07); }
.feat-card:hover::before { opacity:1; }
.feat-icon  { font-size:2rem; margin-bottom:14px; }
.feat-title { font-family:'Rajdhani',sans-serif; font-weight:700; font-size:1.08rem; color:#fff; margin-bottom:10px; }
.feat-desc  { font-size:.83rem; color:rgba(255,255,255,.72); line-height:1.68; }

/* ════════════════════════════════════════════
   HEALTH CARD
════════════════════════════════════════════ */
.health-card {
    background:rgba(10,15,28,0.82); border:1px solid var(--bdr);
    border-radius:18px; padding:22px;
    backdrop-filter:blur(14px); box-shadow:0 4px 18px rgba(0,0,0,.2);
}
.h-lbl { font-size:.59rem; font-weight:700; letter-spacing:1.8px; text-transform:uppercase; color:var(--t4); margin-bottom:5px; }
.h-val { font-family:'Orbitron',sans-serif; font-size:1.8rem; font-weight:800; color:var(--t1); }
.h-ok  { display:flex; align-items:center; gap:6px; font-size:.86rem; font-weight:700; color:var(--cg); }
.h-div { height:1px; background:var(--bdr); margin:13px 0; }

/* ════════════════════════════════════════════
   DIVIDER
════════════════════════════════════════════ */
.divline { height:1px; background:linear-gradient(90deg,transparent,rgba(255,255,255,.06),transparent); margin:28px 0; }

/* ════════════════════════════════════════════
   LOGIN PAGE
════════════════════════════════════════════ */
@keyframes fl1{0%,100%{transform:translate(0,0)scale(1);opacity:.6;}33%{transform:translate(28px,-18px)scale(1.07);opacity:.8;}66%{transform:translate(-18px,13px)scale(.95);opacity:.5;}}
@keyframes fl2{0%,100%{transform:translate(0,0)scale(1);opacity:.4;}25%{transform:translate(-38px,23px)scale(1.1);opacity:.7;}75%{transform:translate(23px,-28px)scale(.9);opacity:.3;}}
@keyframes spin1{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}
@keyframes spin2{from{transform:rotate(0deg);}to{transform:rotate(-360deg);}}
@keyframes shimmer{0%{background-position:0% 50%;}50%{background-position:100% 50%;}100%{background-position:0% 50%;}}
@keyframes card-in{from{opacity:0;transform:translateY(28px)scale(.96);}to{opacity:1;transform:translateY(0)scale(1);}}
@keyframes logo-p{0%,100%{box-shadow:0 0 28px rgba(99,102,241,.5),0 0 55px rgba(34,211,238,.18);}50%{box-shadow:0 0 55px rgba(99,102,241,.8),0 0 110px rgba(34,211,238,.35);}}
@keyframes glow-t{0%,100%{text-shadow:0 0 18px rgba(34,211,238,.38);}50%{text-shadow:0 0 38px rgba(34,211,238,.85),0 0 75px rgba(34,211,238,.28);}}
@keyframes scanline{0%{transform:translateY(-100%);}100%{transform:translateY(100vh);}}
@keyframes prise{0%{transform:translateY(0)scale(1);opacity:.7;}100%{transform:translateY(-115px)scale(0);opacity:0;}}
@keyframes dstream{0%{transform:translateY(0);opacity:.55;}100%{transform:translateY(-190px);opacity:0;}}

.lg-bg{position:fixed;inset:0;background:radial-gradient(ellipse at 20% 20%,rgba(99,102,241,.17) 0%,transparent 50%),radial-gradient(ellipse at 80% 80%,rgba(34,211,238,.12) 0%,transparent 50%),#040608;z-index:0;overflow:hidden;}
.lg-bg::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(99,102,241,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(99,102,241,.035) 1px,transparent 1px);background-size:46px 46px;}
.lg-bg::after{content:'';position:absolute;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent,rgba(34,211,238,.38),transparent);animation:scanline 6s linear infinite;}
.lg-orb1{position:absolute;width:480px;height:480px;background:radial-gradient(circle,rgba(99,102,241,.24) 0%,transparent 65%);border-radius:50%;top:-75px;left:-95px;animation:fl1 12s ease-in-out infinite;filter:blur(2px);}
.lg-orb2{position:absolute;width:380px;height:380px;background:radial-gradient(circle,rgba(34,211,238,.18) 0%,transparent 65%);border-radius:50%;bottom:-55px;right:-75px;animation:fl2 15s ease-in-out infinite;filter:blur(2px);}
.lg-card{background:rgba(10,15,30,.9);border:1px solid rgba(255,255,255,.07);border-radius:26px;padding:46px 44px 40px;width:100%;max-width:460px;backdrop-filter:blur(28px);box-shadow:0 32px 75px rgba(0,0,0,.55),0 0 70px rgba(99,102,241,.12);animation:card-in .8s cubic-bezier(.34,1.56,.64,1) both;position:relative;overflow:hidden;}
.lg-card::before{content:'';position:absolute;inset:0;border-radius:26px;padding:1px;background:linear-gradient(90deg,rgba(99,102,241,.55),rgba(34,211,238,.55),rgba(139,92,246,.55),rgba(34,211,238,.55),rgba(99,102,241,.55));background-size:300% 100%;animation:shimmer 4s linear infinite;-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;}
.lg-logo-wrap{position:relative;width:78px;height:78px;margin:0 auto 20px;}
.lg-logo{width:78px;height:78px;background:linear-gradient(135deg,#6366F1,#8B5CF6,#22D3EE);border-radius:22px;display:flex;align-items:center;justify-content:center;font-size:2.1rem;animation:logo-p 3s ease-in-out infinite;position:relative;z-index:2;}
.ring1{position:absolute;inset:-11px;border:1.5px solid rgba(34,211,238,.33);border-top-color:var(--c2);border-radius:50%;animation:spin1 3s linear infinite;}
.ring2{position:absolute;inset:-21px;border:1px solid rgba(139,92,246,.23);border-right-color:var(--cv);border-radius:50%;animation:spin2 5s linear infinite;}
.lg-brand{font-family:'Orbitron',sans-serif;font-size:1.55rem;font-weight:900;color:var(--t1);letter-spacing:3px;text-align:center;margin-bottom:3px;animation:glow-t 4s ease-in-out infinite;}
.lg-brand span{color:var(--c2);}
.lg-tag{font-size:.66rem;color:var(--t4);letter-spacing:3px;text-transform:uppercase;text-align:center;margin-bottom:30px;}
.lg-title{font-family:'Rajdhani',sans-serif;font-size:1.42rem;font-weight:700;color:var(--t1);margin-bottom:4px;}
.lg-sub{font-size:.83rem;color:var(--t4);margin-bottom:26px;}
.lg-demo{background:rgba(99,102,241,.07);border:1px solid rgba(99,102,241,.17);border-radius:10px;padding:12px 14px;margin-top:18px;font-size:.77rem;color:var(--t3);text-align:center;}
.lg-demo strong{color:var(--c2);}
.lg-err{background:rgba(251,113,133,.09);border:1px solid rgba(251,113,133,.27);border-radius:10px;padding:10px 14px;font-size:.82rem;color:var(--cr);margin-bottom:14px;font-weight:600;}
.particle{position:absolute;border-radius:50%;background:var(--c2);opacity:0;pointer-events:none;animation:prise var(--dur,4s) var(--delay,0s) ease-out infinite;}
.dcol{position:absolute;font-family:'JetBrains Mono',monospace;font-size:.69rem;color:rgba(34,211,238,.1);user-select:none;pointer-events:none;animation:dstream var(--dur,8s) var(--delay,0s) linear infinite;letter-spacing:2px;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# Inject floating ambient orbs into the main app background
# (These are separate from the CSS pseudo-elements)
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div aria-hidden='true' style='position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;'>
    <!-- Large violet nebula orb top-left -->
    <div style='position:absolute;width:680px;height:680px;
                background:radial-gradient(circle,rgba(99,102,241,0.12) 0%,rgba(99,102,241,0.04) 45%,transparent 70%);
                border-radius:50%;top:-180px;left:-200px;
                animation:orb_float_a 22s ease-in-out infinite;
                filter:blur(1px);'></div>
    <!-- Medium cyan orb top-right -->
    <div style='position:absolute;width:520px;height:520px;
                background:radial-gradient(circle,rgba(34,211,238,0.1) 0%,rgba(34,211,238,0.03) 50%,transparent 70%);
                border-radius:50%;top:-100px;right:-140px;
                animation:orb_float_b 26s ease-in-out infinite 3s;
                filter:blur(1px);'></div>
    <!-- Small rose orb center-right -->
    <div style='position:absolute;width:320px;height:320px;
                background:radial-gradient(circle,rgba(251,113,133,0.07) 0%,transparent 70%);
                border-radius:50%;top:40%;right:5%;
                animation:orb_float_c 18s ease-in-out infinite 6s;
                filter:blur(2px);'></div>
    <!-- Teal orb bottom-left -->
    <div style='position:absolute;width:420px;height:420px;
                background:radial-gradient(circle,rgba(45,212,191,0.07) 0%,transparent 70%);
                border-radius:50%;bottom:-120px;left:10%;
                animation:orb_float_b 20s ease-in-out infinite 2s;
                filter:blur(2px);'></div>
    <!-- Amber micro orb bottom-right -->
    <div style='position:absolute;width:260px;height:260px;
                background:radial-gradient(circle,rgba(251,191,36,0.06) 0%,transparent 70%);
                border-radius:50%;bottom:8%;right:12%;
                animation:orb_float_a 24s ease-in-out infinite 9s;
                filter:blur(3px);'></div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# ████████  PLOT HELPERS  ████████
# ══════════════════════════════════════════════════════════════════
def dark_fig(w=9, h=4):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor(PLOT_BG)
    ax.set_facecolor(PLOT_BG)
    ax.tick_params(colors=TEXT_CLR, labelsize=9)
    ax.xaxis.label.set_color(TEXT_CLR)
    ax.yaxis.label.set_color(TEXT_CLR)
    ax.title.set_color("#F0F4FF")
    for s in ax.spines.values():
        s.set_edgecolor(GRID_CLR)
    ax.grid(True, color=GRID_CLR, linewidth=0.5, alpha=0.8)
    return fig, ax


def dark_figs(rows, cols, w=12, h=5):
    fig, axes = plt.subplots(rows, cols, figsize=(w, h))
    fig.patch.set_facecolor(PLOT_BG)
    for ax in (axes.flatten() if hasattr(axes, "flatten") else [axes]):
        ax.set_facecolor(PLOT_BG)
        ax.tick_params(colors=TEXT_CLR, labelsize=9)
        ax.xaxis.label.set_color(TEXT_CLR)
        ax.yaxis.label.set_color(TEXT_CLR)
        ax.title.set_color("#F0F4FF")
        for sp in ax.spines.values():
            sp.set_edgecolor(GRID_CLR)
        ax.grid(True, color=GRID_CLR, linewidth=0.5, alpha=0.8)
    return fig, axes


# ══════════════════════════════════════════════════════════════════
# ████████  UI HELPERS  ████████
# ══════════════════════════════════════════════════════════════════
def kpi_card(col, icon, color, label, value, sub, trend=None):
    tr = ""
    if trend is not None:
        cls = "kpi-up" if trend >= 0 else "kpi-dn"
        ar  = "↑" if trend >= 0 else "↓"
        tr  = f"<div class='{cls}'>{ar} {abs(trend):.1f}% vs last period</div>"
    with col:
        st.markdown(f"""
        <div class='kpi-card {color}'>
          <div class='kpi-ico {color}'>{icon}</div>
          <div class='kpi-lbl'>{label}</div>
          <div class='kpi-val'>{value}</div>
          <div class='kpi-sub'>{sub}</div>
          {tr}
        </div>""", unsafe_allow_html=True)


def sec(title, sub=""):
    st.markdown(f"<div class='sec-h'>{title}</div><div class='sec-s'>{sub}</div>", unsafe_allow_html=True)


def ins(text):
    st.markdown(f"<div class='insight-box'>💡 {text}</div>", unsafe_allow_html=True)


def div():
    st.markdown("<div class='divline'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# ████████  DATA  ████████
# ══════════════════════════════════════════════════════════════════
@st.cache_data(show_spinner=False)
def generate_dataset(n: int = 1200) -> pd.DataFrame:
    np.random.seed(42)
    date_range  = pd.date_range("2023-01-01", periods=365, freq="D")
    dates       = pd.Series(np.random.choice(date_range, size=n))
    day_of_week = [pd.Timestamp(d).day_name() for d in dates]
    location    = np.random.choice(["Urban","Suburban","Rural"], n, p=[.50,.35,.15])
    time_of_day = np.random.choice(["Morning","Afternoon","Evening","Night"], n, p=[.30,.35,.25,.10])
    weather     = np.random.choice(["Sunny","Cloudy","Rainy","Stormy"], n, p=[.45,.30,.20,.05])
    holiday     = np.random.choice([0,1], n, p=[.85,.15])
    event       = np.random.choice([0,1], n, p=[.90,.10])
    competitors = np.random.randint(0, 6, n)
    base_w      = np.where(location=="Urban", 50000, np.where(location=="Suburban", 30000, 15000))
    noise       = np.random.normal(0, 5000, n)
    withdrawals = np.clip(base_w + noise
        + holiday * np.random.uniform(5000,15000,n)
        + event   * np.random.uniform(3000,10000,n), 5000, None)
    anom_idx    = np.random.choice(n, size=int(0.03*n), replace=False)
    withdrawals[anom_idx] += np.random.uniform(50000, 120000, len(anom_idx))
    deposits  = np.clip(withdrawals * np.random.uniform(.3,.7,n) + np.random.normal(0,2000,n), 1000, None)
    prev_cash = np.clip(withdrawals * np.random.uniform(1.0,2.5,n) + np.random.normal(0,3000,n), 5000, None)
    next_day  = np.clip(withdrawals * np.random.uniform(.8,1.4,n) + np.random.normal(0,4000,n), 5000, None)
    atm_ids   = [f"ATM{str(i).zfill(3)}" for i in np.random.randint(1,101,n)]
    df = pd.DataFrame({
        "ATM_ID":atm_ids,"Date":pd.to_datetime(dates.values),
        "Day_of_Week":day_of_week,"Time_of_Day":time_of_day,
        "Total_Withdrawals":np.round(withdrawals,2),"Total_Deposits":np.round(deposits,2),
        "Previous_Day_Cash_Level":np.round(prev_cash,2),"Location_Type":location,
        "Holiday_Flag":holiday,"Special_Event_Flag":event,"Weather_Condition":weather,
        "Nearby_Competitor_ATMs":competitors,"Cash_Demand_Next_Day":np.round(next_day,2),
    })
    return df.sort_values("Date").reset_index(drop=True)


@st.cache_data(show_spinner=False)
def run_clustering(df: pd.DataFrame):
    le  = LabelEncoder()
    df2 = df.copy()
    df2["Loc_Enc"] = le.fit_transform(df2["Location_Type"])
    feats = ["Total_Withdrawals","Total_Deposits","Loc_Enc","Nearby_Competitor_ATMs"]
    X_sc  = StandardScaler().fit_transform(df2[feats].values)
    inertias = [KMeans(k,random_state=42,n_init=10).fit(X_sc).inertia_ for k in range(1,11)]
    km = KMeans(3, random_state=42, n_init=10)
    df2["Cluster_Raw"] = km.fit_predict(X_sc)
    means = df2.groupby("Cluster_Raw")["Total_Withdrawals"].mean().sort_values()
    df2["Cluster"] = df2["Cluster_Raw"].map({
        means.index[0]:"Low Demand", means.index[1]:"Medium Demand", means.index[2]:"High Demand",
    })
    return df2, inertias


@st.cache_data(show_spinner=False)
def run_anomaly(df: pd.DataFrame):
    col = "Total_Withdrawals"
    z   = np.abs(stats.zscore(df[col]))
    Q1, Q3 = df[col].quantile(.25), df[col].quantile(.75)
    IQR = Q3 - Q1
    df2 = df.copy()
    df2["Z_Score"]     = z
    df2["Anomaly_Z"]   = z > 3.0
    df2["Anomaly_IQR"] = (df[col] > Q3+1.5*IQR) | (df[col] < Q1-1.5*IQR)
    df2["Is_Anomaly"]  = df2["Anomaly_Z"] | df2["Anomaly_IQR"]
    return df2, Q1, Q3, IQR


# ══════════════════════════════════════════════════════════════════
# ████████  LOGIN  ████████
# ══════════════════════════════════════════════════════════════════
def show_login():
    st.markdown(
        "<style>[data-testid='stSidebar']{display:none!important}"
        "header{display:none!important}.stApp::before,.stApp::after{display:none!important}</style>",
        unsafe_allow_html=True)

    st.markdown("""
    <div class='lg-bg'>
        <div class='lg-orb1'></div><div class='lg-orb2'></div>
        <div class='dcol' style='left:5%;top:10%;--dur:7s;--delay:0s;'>01001101<br>10110010<br>01001010<br>11000101</div>
        <div class='dcol' style='left:85%;top:8%;--dur:8.5s;--delay:.5s;'>₹50,430<br>₹32,100<br>₹78,900<br>₹45,670</div>
        <div class='dcol' style='left:12%;top:55%;--dur:9s;--delay:1.5s;'>ATM-042<br>ATM-099<br>ATM-017<br>ATM-055</div>
        <div class='dcol' style='left:91%;top:55%;--dur:11s;--delay:2s;'>Z=3.21<br>Z=2.87<br>Z=4.05<br>Z=1.99</div>
    </div>""", unsafe_allow_html=True)

    _, c, _ = st.columns([1, 1.05, 1])
    with c:
        st.markdown("""
        <div style='margin-top:38px;text-align:center;'>
          <div class='lg-logo-wrap'><div class='lg-logo'>🏦</div><div class='ring1'></div><div class='ring2'></div></div>
          <div class='lg-brand'>TBSM <span>BANK</span></div>
          <div class='lg-tag'>ATM Operational Intelligence · v6</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div class='lg-card'>", unsafe_allow_html=True)
        st.markdown("""<div aria-hidden='true'>
          <div class='particle' style='width:3px;height:3px;left:10%;bottom:5%;--dur:3.5s;--delay:0s;'></div>
          <div class='particle' style='width:2px;height:2px;left:30%;bottom:8%;--dur:5s;--delay:1s;background:var(--cv);'></div>
          <div class='particle' style='width:4px;height:4px;left:65%;bottom:3%;--dur:4s;--delay:.5s;background:var(--cg);'></div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div class='lg-title'>Welcome Back</div><div class='lg-sub'>Sign in to access the intelligence dashboard</div>", unsafe_allow_html=True)
        if st.session_state.login_error:
            st.markdown("<div class='lg-err'>⚠️ Invalid credentials. Please try again.</div>", unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            u   = st.text_input("Operator ID", placeholder="e.g. admin")
            p   = st.text_input("Access Key",  type="password", placeholder="••••••••")
            sub = st.form_submit_button("SIGN IN  →")

        if sub:
            cred = CREDENTIALS.get(u)
            if cred and cred["password"] == p:
                st.session_state.update({"authenticated":True,"username":u,"role":cred["role"],"login_error":False})
                st.rerun()
            else:
                st.session_state.login_error = True; st.rerun()

        st.markdown("<div class='lg-demo'>Demo · <strong>admin / 1234</strong> &nbsp;|&nbsp; <strong>analyst / analyst123</strong></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;font-size:.67rem;color:var(--t4);margin-top:14px;letter-spacing:1.5px;text-transform:uppercase;'>© 2026 TBSM BANK · OPERATIONAL INTELLIGENCE</p>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# ████████  PREMIUM SIDEBAR v6  ████████
# ══════════════════════════════════════════════════════════════════
def render_sidebar(df_all, n_anom):
    user_info = CREDENTIALS[st.session_state.username]
    name      = user_info["name"]
    initials  = "".join(w[0].upper() for w in name.split()[:2])

    with st.sidebar:
        # ── BRAND HEADER ──────────────────────────────────────────
        st.markdown(f"""
        <div style='padding:22px 16px 16px;
                    background:linear-gradient(180deg,rgba(34,211,238,0.07) 0%,transparent 100%);
                    border-bottom:1px solid rgba(34,211,238,0.07);
                    position:relative;overflow:hidden;'>
            <!-- Decorative corner glow -->
            <div style='position:absolute;right:-15px;top:-15px;width:90px;height:90px;
                        background:radial-gradient(circle,rgba(34,211,238,0.14) 0%,transparent 70%);
                        border-radius:50%;'></div>
            <!-- Brand row -->
            <div style='display:flex;align-items:center;gap:12px;position:relative;z-index:1;'>
                <div style='position:relative;'>
                    <div style='width:42px;height:42px;flex-shrink:0;
                                background:linear-gradient(135deg,#4F46E5,#7C3AED,#06B6D4);
                                border-radius:12px;display:flex;align-items:center;
                                justify-content:center;font-size:1.15rem;
                                box-shadow:0 0 22px rgba(99,102,241,0.65),
                                           0 0 44px rgba(34,211,238,0.22),
                                           inset 0 1px 0 rgba(255,255,255,0.15);'>🏦</div>
                    <!-- Pulsing ring around logo -->
                    <div style='position:absolute;inset:-4px;border:1px solid rgba(34,211,238,0.3);
                                border-radius:16px;animation:bar_p 3s ease-in-out infinite;'></div>
                </div>
                <div>
                    <div style='font-family:Orbitron,sans-serif;font-size:.92rem;
                                font-weight:900;color:#fff;letter-spacing:2.5px;line-height:1;
                                text-shadow:0 0 16px rgba(34,211,238,0.32);'>
                        TBSM <span style='color:#22D3EE;'>BANK</span>
                    </div>
                    <div style='font-size:.44rem;color:rgba(34,211,238,0.35);
                                letter-spacing:3px;text-transform:uppercase;margin-top:5px;
                                font-family:JetBrains Mono,monospace;'>
                        ATM INTEL · v6.0
                    </div>
                </div>
            </div>
            <!-- Thin scan line below brand -->
            <div style='position:absolute;bottom:0;left:0;right:0;height:1px;
                        background:linear-gradient(90deg,transparent,rgba(34,211,238,0.25),transparent);'></div>
        </div>
        """, unsafe_allow_html=True)

        # ── USER CARD ─────────────────────────────────────────────
        role_colors = {
            "Administrator": ("#6366F1","#4338CA"),
            "Data Analyst":  ("#22D3EE","#0891B2"),
            "Branch Manager":("#8B5CF6","#6D28D9"),
        }
        rc1, rc2 = role_colors.get(user_info["role"], ("#6366F1","#4338CA"))
        st.markdown(f"""
        <div style='margin:10px 10px 0;padding:13px 14px;
                    background:linear-gradient(135deg,rgba(99,102,241,0.1),rgba(34,211,238,0.05));
                    border:1px solid rgba(99,102,241,0.2);border-radius:13px;
                    display:flex;align-items:center;gap:10px;
                    box-shadow:0 0 24px rgba(99,102,241,0.1),inset 0 1px 0 rgba(255,255,255,0.04);'>
            <!-- Avatar -->
            <div style='width:37px;height:37px;flex-shrink:0;border-radius:10px;
                        background:linear-gradient(135deg,{rc1},{rc2});
                        display:flex;align-items:center;justify-content:center;
                        font-family:Orbitron,sans-serif;font-weight:900;
                        font-size:.78rem;color:#fff;
                        box-shadow:0 0 16px rgba(99,102,241,0.55),inset 0 1px 0 rgba(255,255,255,0.2);'>
                {initials}
            </div>
            <!-- Info -->
            <div style='flex:1;min-width:0;'>
                <div style='font-size:.83rem;font-weight:700;color:#F4F7FF;
                            white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
                            font-family:Syne,sans-serif;'>
                    {name}
                </div>
                <div style='display:flex;align-items:center;gap:5px;margin-top:4px;'>
                    <div style='width:5px;height:5px;border-radius:50%;
                                background:#34D399;
                                box-shadow:0 0 7px #34D399,0 0 14px rgba(52,211,153,0.4);
                                flex-shrink:0;animation:pd 2s infinite;'></div>
                    <span style='font-size:.53rem;font-weight:700;letter-spacing:1.8px;
                                 text-transform:uppercase;color:rgba(34,211,238,0.6);
                                 font-family:JetBrains Mono,monospace;'>
                        {user_info["role"]}
                    </span>
                </div>
            </div>
            <!-- Status dot right -->
            <div style='font-size:.58rem;font-weight:700;color:rgba(34,211,238,0.28);
                        font-family:Orbitron,sans-serif;letter-spacing:.5px;'>●</div>
        </div>
        """, unsafe_allow_html=True)

        # ── NAV ───────────────────────────────────────────────────
        page = st.session_state.current_page

        NAV_GROUPS = [
            ("Overview", [
                ("🏠","Home",         "🏠  Home"),
                ("🎯","Project Scope","🎯  Project Scope"),
            ]),
            ("Data", [
                ("📤","Data Upload",  "📤  Data Upload"),
                ("🧹","Data Cleaning","🧹  Data Cleaning"),
                ("📊","Exploration",  "📊  Exploration"),
            ]),
            ("Analysis", [
                ("⚠️","Anomaly Detection","⚠️  Anomaly Detection"),
                ("🔮","Forecasting",      "🔮  Forecasting"),
                ("💡","Insights",         "💡  Insights"),
                ("📖","Storyboard",       "📖  Storyboard"),
            ]),
        ]

        for gi, (grp_name, items) in enumerate(NAV_GROUPS):
            # Section label with decorative lines
            st.markdown(f"""
            <div style='padding:{"15px" if gi>0 else "10px"} 14px 6px;
                        display:flex;align-items:center;gap:8px;'>
                <div style='height:1px;flex:1;
                            background:linear-gradient(90deg,transparent,rgba(34,211,238,0.12));'></div>
                <span style='font-size:.42rem;font-weight:700;letter-spacing:3px;
                             text-transform:uppercase;color:rgba(34,211,238,0.28);
                             font-family:JetBrains Mono,monospace;'>{grp_name}</span>
                <div style='height:1px;flex:1;
                            background:linear-gradient(90deg,rgba(34,211,238,0.12),transparent);'></div>
            </div>""", unsafe_allow_html=True)

            # Nav group box
            st.markdown("""
            <div style='margin:0 9px 5px;
                        background:rgba(255,255,255,0.015);
                        border:1px solid rgba(255,255,255,0.04);
                        border-radius:12px;overflow:hidden;'>""",
                unsafe_allow_html=True)

            for i, (emoji, label, page_key) in enumerate(items):
                is_active  = (page == page_key)
                active_cls = "nav-active" if is_active else ""
                if i > 0:
                    st.markdown("<div style='height:1px;background:rgba(255,255,255,0.03);margin:0 12px;'></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='{active_cls}' style='margin:0;padding:0;'>", unsafe_allow_html=True)
                if st.button(f"{emoji}  {label}", key=f"nav_{page_key}"):
                    st.session_state.current_page = page_key
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        # ── SYSTEM STATUS PANEL ───────────────────────────────────
        n_pending = n_anom - len(st.session_state.investigated)
        cleaning_pct = int(sum(st.session_state.cleaning_done.values()) / 4 * 100)

        st.markdown(f"""
        <div style='margin:12px 9px 0;
                    background:linear-gradient(135deg,rgba(6,10,22,0.95),rgba(5,8,18,0.9));
                    border:1px solid rgba(34,211,238,0.1);border-radius:14px;
                    padding:16px;
                    box-shadow:0 0 30px rgba(34,211,238,0.04),inset 0 1px 0 rgba(255,255,255,0.03);'>
            <!-- Panel title -->
            <div style='font-size:.42rem;font-weight:700;letter-spacing:3px;
                        text-transform:uppercase;color:rgba(34,211,238,0.32);
                        margin-bottom:13px;font-family:JetBrains Mono,monospace;
                        display:flex;align-items:center;gap:7px;'>
                <div style='width:4px;height:4px;border-radius:50%;
                            background:var(--cg);box-shadow:0 0 6px var(--cg);
                            animation:pd 2s infinite;'></div>
                System Status
            </div>
            <!-- Stats grid -->
            <div style='display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-bottom:8px;'>
                <!-- Records -->
                <div style='background:linear-gradient(135deg,rgba(34,211,238,0.07),rgba(34,211,238,0.02));
                            border:1px solid rgba(34,211,238,0.13);border-radius:10px;
                            padding:10px 12px;'>
                    <div style='font-size:.46rem;font-weight:700;letter-spacing:.8px;
                                text-transform:uppercase;color:rgba(34,211,238,0.42);
                                margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Records</div>
                    <div style='font-family:Orbitron,sans-serif;font-size:.92rem;
                                font-weight:800;color:#F0F4FF;line-height:1;'>
                        {len(df_all):,}
                    </div>
                </div>
                <!-- Alerts -->
                <div style='background:linear-gradient(135deg,rgba(251,113,133,0.07),rgba(251,113,133,0.02));
                            border:1px solid rgba(251,113,133,0.16);border-radius:10px;
                            padding:10px 12px;'>
                    <div style='font-size:.46rem;font-weight:700;letter-spacing:.8px;
                                text-transform:uppercase;color:rgba(251,113,133,0.42);
                                margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Alerts</div>
                    <div style='font-family:Orbitron,sans-serif;font-size:.92rem;
                                font-weight:800;color:#fb7185;line-height:1;
                                text-shadow:0 0 10px rgba(251,113,133,0.35);'>
                        {n_pending}
                    </div>
                </div>
            </div>
            <!-- Pipeline progress -->
            <div style='margin-bottom:9px;'>
                <div style='display:flex;justify-content:space-between;
                            font-size:.44rem;font-weight:700;letter-spacing:1px;
                            color:rgba(139,92,246,0.5);text-transform:uppercase;
                            margin-bottom:5px;font-family:JetBrains Mono,monospace;'>
                    <span>Pipeline</span><span style='color:{"rgba(52,211,153,0.7)" if cleaning_pct==100 else "rgba(251,191,36,0.7)"};'>{cleaning_pct}%</span>
                </div>
                <div style='background:rgba(255,255,255,0.06);border-radius:99px;height:5px;'>
                    <div style='background:{"linear-gradient(90deg,#22D3EE,#8B5CF6)" if cleaning_pct==100 else "linear-gradient(90deg,#6366F1,#8B5CF6)"};
                                border-radius:99px;height:5px;width:{cleaning_pct}%;
                                box-shadow:0 0 10px rgba(99,102,241,0.5);'></div>
                </div>
            </div>
            <!-- ATMs online -->
            <div style='background:linear-gradient(135deg,rgba(52,211,153,0.06),rgba(34,211,238,0.03));
                        border:1px solid rgba(52,211,153,0.13);
                        border-radius:9px;padding:8px 11px;
                        display:flex;align-items:center;justify-content:space-between;'>
                <div style='display:flex;align-items:center;gap:6px;'>
                    <div style='width:5px;height:5px;border-radius:50%;
                                background:#34D399;
                                box-shadow:0 0 8px #34D399,0 0 16px rgba(52,211,153,0.4);
                                animation:pd 2s infinite;flex-shrink:0;'></div>
                    <span style='font-size:.71rem;font-weight:600;color:rgba(52,211,153,0.8);
                                 font-family:Syne,sans-serif;'>100 ATMs Online</span>
                </div>
                <span style='font-family:JetBrains Mono,monospace;font-size:.52rem;
                             font-weight:700;color:rgba(52,211,153,0.3);letter-spacing:1px;'>LIVE</span>
            </div>
        </div>""", unsafe_allow_html=True)

        # ── DIVIDER ───────────────────────────────────────────────
        st.markdown("""
        <div style='height:1px;
                    background:linear-gradient(90deg,transparent,rgba(255,255,255,0.07),transparent);
                    margin:14px 9px 11px;'></div>""",
            unsafe_allow_html=True)

        # ── SIGN OUT ──────────────────────────────────────────────
        st.markdown("<div class='sb-signout' style='padding:0 9px 10px;'>", unsafe_allow_html=True)
        if st.button("🔓  Sign Out", key="logout_btn"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        # ── COPYRIGHT ─────────────────────────────────────────────
        st.markdown("""
        <div style='padding:3px 0 13px;font-size:.43rem;color:rgba(255,255,255,0.09);
                    letter-spacing:2.5px;text-transform:uppercase;text-align:center;
                    font-family:Orbitron,sans-serif;'>
            © 2026 TBSM BANK · v6.0
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# ████████  TOPBAR  ████████
# ══════════════════════════════════════════════════════════════════
def render_topbar(page_label, n_anom):
    name     = CREDENTIALS[st.session_state.username]["name"]
    initials = "".join(w[0].upper() for w in name.split()[:2])
    st.markdown(f"""
    <div class='topbar'>
        <div class='topbar-title'><div class='tb-bar'></div>{page_label}</div>
        <div class='topbar-right'>
            <div class='tb-alert'><span>⚠️</span><span>{n_anom} Alerts</span></div>
            <div class='tb-badge'>
                <div class='tb-avatar'>{initials}</div>
                <span>{name}</span>
                <div class='live-dot'></div>
                <span style='color:var(--cg);font-size:.7rem;font-weight:700;'>LIVE</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# ████████  PAGE FUNCTIONS  ████████
# ══════════════════════════════════════════════════════════════════

def page_home(df, n_anom):
    tw = df["Total_Withdrawals"].sum()
    td = df["Total_Deposits"].sum()

    # Hero
    st.markdown("""
    <div style='background:linear-gradient(150deg,rgba(5,9,20,0.92) 0%,rgba(10,8,38,0.88) 50%,rgba(7,18,38,0.92) 100%);
                border-radius:24px;padding:60px 56px;margin-bottom:32px;
                position:relative;overflow:hidden;
                border:1px solid rgba(99,102,241,0.17);
                backdrop-filter:blur(20px);
                box-shadow:0 0 80px rgba(99,102,241,0.09),inset 0 1px 0 rgba(255,255,255,0.04);'>
        <div style='position:absolute;right:-80px;top:-80px;width:360px;height:360px;
                    background:radial-gradient(circle,rgba(139,92,246,0.2) 0%,transparent 70%);
                    border-radius:50%;pointer-events:none;'></div>
        <div style='position:absolute;left:25%;bottom:-60px;width:250px;height:250px;
                    background:radial-gradient(circle,rgba(34,211,238,0.12) 0%,transparent 70%);
                    border-radius:50%;pointer-events:none;'></div>
        <div style='position:relative;z-index:1;text-align:center;'>
            <div style='display:inline-flex;align-items:center;gap:8px;
                        background:rgba(34,211,238,0.08);border:1px solid rgba(34,211,238,0.2);
                        border-radius:20px;padding:6px 18px;margin-bottom:22px;
                        font-size:.63rem;font-weight:700;letter-spacing:3px;
                        text-transform:uppercase;color:var(--c2);
                        box-shadow:0 0 18px rgba(34,211,238,0.09);'>
                <span style='width:6px;height:6px;border-radius:50%;background:var(--cg);
                             box-shadow:0 0 8px var(--cg);display:inline-block;animation:pd 2s infinite;'></span>
                LIVE DASHBOARD
            </div>
            <div style='font-family:Orbitron,sans-serif;font-size:3rem;font-weight:900;
                        color:#F0F4FF;line-height:1.02;margin-bottom:16px;letter-spacing:2px;'>
                TBSM <span style='color:#22D3EE;text-shadow:0 0 38px rgba(34,211,238,0.5);'>BANK</span><br>
                <span style='font-size:1.5rem;color:#8B5CF6;letter-spacing:4px;
                             text-shadow:0 0 28px rgba(139,92,246,0.5);'>ATM INTELLIGENCE</span>
            </div>
            <div style='font-size:.96rem;color:#94A3B8;max-width:540px;margin:0 auto;line-height:1.8;'>
                Optimise cash flow, detect anomalies, and unlock demand patterns
                across <strong style='color:#F0F4FF;'>100 ATMs</strong> — powered by real-time data science.
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)
    for col, grad, icon, title, desc in [
        (f1,"linear-gradient(135deg,#4338CA,#6D28D9,#7C3AED)","⚡",
         "Smart Demand Forecasting","Predict cash requirements using historical patterns, holidays, events & weather."),
        (f2,"linear-gradient(135deg,#0D9488,#0891B2,#06B6D4)","🛡️",
         "Real-Time Anomaly Detection","Identify suspicious withdrawal spikes and unusual activity across the full network."),
        (f3,"linear-gradient(135deg,#B45309,#D97706,#F59E0B)","📈",
         "Actionable Data Storytelling","Convert complex analytics into clear, executive-ready banking intelligence reports."),
    ]:
        with col:
            st.markdown(f"""
            <div class='feat-card' style='background:{grad};'>
                <div class='feat-icon'>{icon}</div>
                <div class='feat-title'>{title}</div>
                <div class='feat-desc'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    kpi_card(k1,"📈","indigo","TOTAL WITHDRAWALS",f"₹{tw/1e7:.1f} Cr","Across all ATMs",trend=4.2)
    kpi_card(k2,"🏦","teal",  "TOTAL DEPOSITS",   f"₹{td/1e7:.1f} Cr","Net deposits",   trend=2.1)
    kpi_card(k3,"⚠️","rose",  "ANOMALIES FOUND",  str(n_anom),         "Auto-detected",  trend=-1.3)
    kpi_card(k4,"🏧","violet","ACTIVE ATMs",       str(df["ATM_ID"].nunique()),"Machines monitored")

    st.markdown("<br>", unsafe_allow_html=True)
    daily = df.groupby("Date")["Total_Withdrawals"].sum().reset_index()
    daily["MA7"] = daily["Total_Withdrawals"].rolling(7, min_periods=1).mean()
    fig, ax = dark_fig(14, 3.5)
    ax.fill_between(daily["Date"], daily["Total_Withdrawals"], alpha=0.07, color=C_CYAN)
    ax.plot(daily["Date"], daily["Total_Withdrawals"], color=C_CYAN, linewidth=0.6, alpha=0.35)
    ax.plot(daily["Date"], daily["MA7"], color=C_AMBER, linewidth=2.5, label="7-Day Moving Average")
    for d in pd.date_range(daily["Date"].min(), daily["Date"].max(), freq="W-SAT"):
        ax.axvspan(d, d + pd.Timedelta(days=2), alpha=0.035, color=C_VIOLET)
    ax.set_title("Network-Wide Daily Withdrawals — Full Year 2023", fontweight="bold", pad=12, fontsize=12)
    ax.set_ylabel("₹ Withdrawals"); ax.legend(fontsize=9, framealpha=0)
    fig.tight_layout(); st.pyplot(fig); plt.close()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--t4);margin-bottom:14px;'>Quick Navigation</div>", unsafe_allow_html=True)
    q1, q2, q3, q4 = st.columns(4)
    for col, key, dest, icon, label in [
        (q1,"qb_exp","📊  Exploration",      "📊","Explore Data"),
        (q2,"qb_ano","⚠️  Anomaly Detection","⚠️","View Anomalies"),
        (q3,"qb_fc", "🔮  Forecasting",      "🔮","Forecast"),
        (q4,"qb_ins","💡  Insights",          "💡","Insights"),
    ]:
        with col:
            if st.button(f"{icon} {label}", key=key):
                st.session_state.current_page = dest; st.rerun()


def page_scope(df):
    sec("Project Scope", "Defining the boundaries and goals of the TBSM BANK analysis initiative.")
    c1, c2 = st.columns(2)
    for col, grad, icon, title, text in [
        (c1,"linear-gradient(135deg,#4338CA,#6D28D9)","🎯","Objective",
         "Develop a data-driven intelligence system that analyses ATM transaction patterns to optimise "
         "cash replenishment schedules, reduce operational costs, and ensure high availability for customers."),
        (c2,"linear-gradient(135deg,#0D9488,#0891B2)","👥","Stakeholders",
         "TBSM Bank Operations Managers, Cash-in-Transit (CIT) Providers, Branch Managers, and Customer "
         "Experience Teams who rely on ATM uptime and seamless cash availability."),
    ]:
        with col:
            st.markdown(f"""
            <div style='border-radius:18px;padding:30px 28px;height:100%;
                        background:rgba(10,15,28,0.82);border:1px solid var(--bdr);
                        backdrop-filter:blur(14px);box-shadow:0 4px 22px rgba(0,0,0,0.22);'>
                <div style='width:46px;height:46px;border-radius:13px;background:{grad};
                            display:flex;align-items:center;justify-content:center;
                            font-size:1.35rem;margin-bottom:16px;box-shadow:0 8px 22px rgba(0,0,0,0.35);'>{icon}</div>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:1.12rem;
                            color:var(--t1);margin-bottom:14px;'>{title}</div>
                <div style='font-size:.85rem;color:var(--t3);line-height:1.8;
                            border-left:2px solid rgba(99,102,241,0.35);padding-left:16px;'>{text}</div>
            </div>""", unsafe_allow_html=True)
    div()
    st.markdown("""
    <div style='background:rgba(10,15,28,0.82);border:1px solid var(--bdr);
                border-radius:18px;padding:28px 30px;backdrop-filter:blur(14px);
                box-shadow:0 4px 22px rgba(0,0,0,0.2);'>
        <div style='display:flex;align-items:center;gap:12px;margin-bottom:20px;'>
            <div style='width:40px;height:40px;background:rgba(99,102,241,0.15);
                        border:1px solid rgba(99,102,241,0.25);border-radius:11px;
                        display:flex;align-items:center;justify-content:center;font-size:1.1rem;
                        box-shadow:0 0 14px rgba(99,102,241,0.2);'>❓</div>
            <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:1.12rem;color:var(--t1);'>Key Business Questions</div>
        </div>""", unsafe_allow_html=True)
    for i, q in enumerate([
        "When and where is ATM cash demand highest throughout the week?",
        "How do holidays and special events impact withdrawal volumes?",
        "Which ATMs show anomalous withdrawal patterns requiring investigation?",
        "What is the optimal cash replenishment schedule per ATM cluster?",
        "How does nearby competitor density affect individual ATM demand?",
    ], 1):
        st.markdown(f"""
        <div class='biz-card'>
            <div class='biz-num'>{i}</div>
            <div class='biz-text'>{q}</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    div()
    s1, s2, s3 = st.columns(3)
    kpi_card(s1,"📅","indigo","TIME PERIOD","Jan – Dec 2023","Full calendar year")
    kpi_card(s2,"🏧","teal",  "ATM NETWORK","100 ATMs","Urban · Suburban · Rural")
    kpi_card(s3,"🗃️","amber", "DATASET SIZE","1,200 Records","Multi-feature transactions")


def page_upload(df_all):
    sec("Data Upload", "Preview and validate the ATM transaction dataset before analysis.")
    col_main, col_side = st.columns([1.8, 1])
    preview = df_all[["Date","ATM_ID","Location_Type","Total_Withdrawals","Total_Deposits","Holiday_Flag"]].head(15).copy()
    preview["Date"] = preview["Date"].dt.strftime("%Y-%m-%d")
    preview.columns = ["DATE","ATM ID","LOCATION","WITHDRAWALS","DEPOSITS","HOLIDAY"]
    with col_main:
        st.markdown("""
        <div style='background:rgba(10,15,28,0.82);border:1px solid var(--bdr);
                    border-radius:18px;padding:22px 24px;backdrop-filter:blur(14px);
                    box-shadow:0 4px 22px rgba(0,0,0,0.2);'>
            <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;'>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:1rem;color:var(--t1);'>⊞ Dataset Preview</div>
                <div style='background:rgba(99,102,241,0.12);color:var(--c1);font-size:.66rem;font-weight:700;
                            text-transform:uppercase;border:1px solid rgba(99,102,241,0.22);border-radius:20px;padding:4px 14px;'>
                    Showing 15 of 1,200 rows</div>
            </div>""", unsafe_allow_html=True)
        st.dataframe(preview, use_container_width=True, height=380)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button("⬇️  Export Sample CSV (100 rows)", data=df_all.head(100).to_csv(index=False),
                           file_name="tbsm_atm_sample.csv", mime="text/csv", key="download_csv")
    with col_side:
        st.markdown("""
        <div style='background:rgba(10,15,28,0.82);border:1px solid var(--bdr);
                    border-radius:18px;padding:20px 22px;margin-bottom:14px;
                    backdrop-filter:blur(14px);box-shadow:0 4px 18px rgba(0,0,0,0.2);'>
            <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:.95rem;color:var(--t1);margin-bottom:16px;'>Field Mapping</div>""",
            unsafe_allow_html=True)
        for fname, ftype, freq in [
            ("Date","DATE","REQUIRED"),("ATM_ID","TEXT","REQUIRED"),
            ("Location_Type","CATEGORY","REQUIRED"),("Total_Withdrawals","NUMERIC","REQUIRED"),
            ("Holiday_Flag","BOOLEAN","OPTIONAL"),("Weather_Condition","CATEGORY","OPTIONAL"),
        ]:
            req = freq == "REQUIRED"
            bc = "rgba(99,102,241,0.12)" if req else "rgba(255,255,255,0.04)"
            cc = "var(--c1)" if req else "var(--t4)"
            st.markdown(f"""
            <div style='display:flex;justify-content:space-between;align-items:center;
                        padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04);'>
                <div>
                    <div style='font-size:.84rem;font-weight:700;color:var(--t1);'>{fname}</div>
                    <div style='font-size:.6rem;font-weight:700;letter-spacing:1.2px;
                                text-transform:uppercase;color:var(--t4);margin-top:2px;'>{ftype}</div>
                </div>
                <div style='background:{bc};color:{cc};font-size:.58rem;font-weight:800;
                            letter-spacing:.8px;text-transform:uppercase;border-radius:20px;
                            padding:4px 11px;border:1px solid {bc};'>{freq}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        missing = int(df_all.isnull().sum().sum())
        st.markdown(f"""
        <div class='health-card'>
            <div style='display:flex;align-items:center;gap:10px;margin-bottom:18px;
                        font-family:Rajdhani,sans-serif;font-weight:700;font-size:1rem;color:var(--t1);'>
                <div style='width:36px;height:36px;background:var(--gm);border-radius:10px;
                            display:flex;align-items:center;justify-content:center;font-size:.95rem;
                            box-shadow:0 0 14px rgba(99,102,241,0.4);'>🎯</div>
                Data Health
            </div>
            <div style='margin-bottom:13px;'><div class='h-lbl'>Total Records</div><div class='h-val'>1,200</div></div>
            <div class='h-div'></div>
            <div style='margin-bottom:13px;'><div class='h-lbl'>Missing Values</div><div class='h-ok'>✅ {missing} detected</div></div>
            <div class='h-div'></div>
            <div style='margin-bottom:13px;'><div class='h-lbl'>Unique ATMs</div><div class='h-val' style='font-size:1.5rem;'>{df_all["ATM_ID"].nunique()}</div></div>
            <div class='h-div'></div>
            <div><div class='h-lbl'>Date Range</div><div style='font-size:.86rem;font-weight:700;color:var(--t1);'>Jan – Dec 2023</div></div>
        </div>""", unsafe_allow_html=True)


def page_cleaning():
    sec("Data Cleaning", "Validate, transform, and prepare the dataset for analysis.")
    STEPS = [
        ("convert","Convert Date","Standardise date formats and extract Day-of-Week / Month features."),
        ("encode","Label Encode","Transform categorical locations (Urban/Suburban/Rural) into numeric IDs."),
        ("normalize","Normalize Amounts","Scale withdrawal and deposit amounts to [0,1] range for ML models."),
        ("errors","Check Errors","Identify and fix logical inconsistencies and impossible values."),
    ]
    LOGS = {
        "convert":"Extracted Day-of-Week and Month from date strings.",
        "encode":"Encoded 3 unique locations into numeric codes.",
        "normalize":"Normalised withdrawals to [0, 1] range.",
        "errors":"Cleaned 0 incomplete records. Dataset fully populated.",
    }
    col_main, col_side = st.columns([1.6, 1])
    with col_main:
        all_done = all(st.session_state.cleaning_done.values())
        if all_done:
            st.markdown("<div class='ok-banner'>✅ All cleaning steps complete — dataset is analysis-ready!</div>", unsafe_allow_html=True)
        for key, title, desc in STEPS:
            done = st.session_state.cleaning_done.get(key, False)
            st.markdown(f"""
            <div class='step-card {"done-card" if done else ""}'>
                <div class='step-ico {"done" if done else "pend"}'>{"✅" if done else "⏳"}</div>
                <div class='step-info'><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div>
                <span class='{"badge-done" if done else "badge-pend"}'>{"COMPLETE" if done else "PENDING"}</span>
            </div>""", unsafe_allow_html=True)
            if not done:
                if st.button(f"▶  Run: {title}", key=f"run_{key}"):
                    st.session_state.cleaning_done[key] = True; st.rerun()
        if not all_done:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("⚡  Run All Steps at Once", key="run_all"):
                for k in st.session_state.cleaning_done: st.session_state.cleaning_done[k] = True
                st.rerun()
    with col_side:
        done_count = sum(st.session_state.cleaning_done.values())
        pct  = int(done_count / len(STEPS) * 100)
        bg   = "linear-gradient(90deg,#22D3EE,#6366F1,#8B5CF6)" if pct == 100 else "linear-gradient(90deg,#6366F1,#8B5CF6)"
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,rgba(6,10,22,0.95),rgba(5,8,18,0.9));
                    border:1px solid var(--bdr-c);border-radius:18px;padding:22px;
                    backdrop-filter:blur(16px);box-shadow:0 0 38px rgba(34,211,238,0.05);'>
            <div style='font-size:.59rem;font-weight:700;letter-spacing:2px;color:var(--c2);
                        text-transform:uppercase;margin-bottom:16px;font-family:JetBrains Mono,monospace;'>Processing Log</div>""",
            unsafe_allow_html=True)
        for k, log_text in LOGS.items():
            done  = st.session_state.cleaning_done.get(k, False)
            clr   = "var(--cg)" if done else "var(--t4)"
            sym   = "✓" if done else "○"
            st.markdown(f"<div style='font-size:.78rem;color:{clr};padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.04);display:flex;gap:9px;'><span style='flex-shrink:0;font-weight:800;'>{sym}</span><span>{log_text}</span></div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style='margin-top:20px;'>
                <div style='display:flex;justify-content:space-between;font-size:.59rem;font-weight:700;
                            letter-spacing:1.2px;color:var(--c2);text-transform:uppercase;margin-bottom:8px;
                            font-family:JetBrains Mono,monospace;'>
                    <span>Progress</span>
                    <span style='color:{"var(--cg)" if pct==100 else "var(--ca)"};'>{pct}%</span>
                </div>
                <div style='background:rgba(255,255,255,0.05);border-radius:99px;height:9px;'>
                    <div style='background:{bg};border-radius:99px;height:9px;width:{pct}%;
                                box-shadow:0 0 14px rgba(99,102,241,0.5);transition:width .6s ease;'></div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        st.markdown("""
        <div style='background:rgba(99,102,241,0.07);border:1px solid rgba(99,102,241,0.17);
                    border-radius:13px;padding:16px;margin-top:11px;backdrop-filter:blur(10px);'>
            <div style='font-size:.76rem;font-weight:700;color:var(--c2);margin-bottom:7px;'>ⓘ Why Clean?</div>
            <div style='font-size:.8rem;color:var(--t3);line-height:1.7;'>
                Cleaning prevents false anomalies caused by formatting errors — resulting in
                <strong style='color:var(--c2);'>40% more accurate</strong> demand forecasts.
            </div>
        </div>""", unsafe_allow_html=True)


def page_exploration(df):
    sec("Data Exploration", "Interactive analysis of ATM withdrawal patterns and demand trends.")
    with st.expander("🔍 Filters", expanded=True):
        fc1, fc2, fc3 = st.columns(3)
        with fc1: loc_sel = st.multiselect("📍 Location", ["Urban","Suburban","Rural"], default=["Urban","Suburban","Rural"])
        with fc2: day_sel = st.multiselect("📅 Day", DAY_ORDER, default=DAY_ORDER)
        with fc3: wx_sel  = st.multiselect("🌤️ Weather", ["Sunny","Cloudy","Rainy","Stormy"], default=["Sunny","Cloudy","Rainy","Stormy"])

    df_exp = df[df["Location_Type"].isin(loc_sel) & df["Day_of_Week"].isin(day_sel) & df["Weather_Condition"].isin(wx_sel)].copy()
    if df_exp.empty:
        st.markdown("<div class='warn-banner'>⚠️ No records match the selected filters.</div>", unsafe_allow_html=True); return

    k1, k2, k3, k4 = st.columns(4)
    peak_day = df_exp.groupby("Day_of_Week")["Total_Withdrawals"].mean().idxmax()
    kpi_card(k1,"📈","indigo","FILTERED TOTAL",  f"₹{df_exp['Total_Withdrawals'].sum()/1000:.0f}K", f"{len(df_exp):,} records")
    kpi_card(k2,"📊","teal",  "AVG DEMAND",      f"₹{df_exp['Total_Withdrawals'].mean()/1000:.0f}K","Per transaction")
    kpi_card(k3,"📅","amber", "PEAK DAY",        peak_day,"Highest avg demand")
    kpi_card(k4,"📍","violet","LOCATIONS ACTIVE",str(df_exp["Location_Type"].nunique()),"In filter")

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📍 By Location","📅 By Day & Time","🌤️ Weather Impact","🌡️ Correlations","📐 Distributions"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            loc_avg = df_exp.groupby("Location_Type")["Total_Withdrawals"].mean()
            fig, ax = dark_fig(6, 4)
            bars = ax.bar(loc_avg.index, loc_avg.values, color=[LOC_COLORS.get(l, C_INDIGO) for l in loc_avg.index], edgecolor=PLOT_BG, linewidth=1.5, zorder=3, width=0.5)
            for b, v in zip(bars, loc_avg.values):
                ax.text(b.get_x()+b.get_width()/2, b.get_height()+300, f"₹{v/1000:.0f}K", ha="center", va="bottom", fontsize=9, color=C_TXT1, fontweight="700")
            ax.set_title("Avg Withdrawals by Location", fontweight="bold", pad=12)
            ax.set_ylabel("₹ Withdrawals"); fig.tight_layout(); st.pyplot(fig); plt.close()
        with c2:
            sel_atm = st.selectbox("🔎 Drill down — ATM", sorted(df_exp["ATM_ID"].unique()))
            atm_d   = df_exp[df_exp["ATM_ID"]==sel_atm].sort_values("Date")
            if len(atm_d) > 1:
                fig, ax = dark_fig(6, 4)
                ax.fill_between(atm_d["Date"], atm_d["Total_Withdrawals"], alpha=0.10, color=C_TEAL)
                ax.plot(atm_d["Date"], atm_d["Total_Withdrawals"], color=C_CYAN, linewidth=1.5)
                an = atm_d[atm_d["Is_Anomaly"]]
                if not an.empty:
                    ax.scatter(an["Date"], an["Total_Withdrawals"], color=C_ROSE, s=70, zorder=5, label="⚠ Anomaly", edgecolors=PLOT_BG, linewidths=1)
                    ax.legend(fontsize=8, framealpha=0)
                ax.set_title(f"{sel_atm} — Withdrawal History", fontweight="bold")
                ax.set_xlabel("Date"); ax.set_ylabel("₹ Withdrawals")
                fig.tight_layout(); st.pyplot(fig); plt.close()

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            dow = df_exp.groupby("Day_of_Week")["Total_Withdrawals"].mean().reindex(DAY_ORDER)
            fig, ax = dark_fig(6, 4)
            bars = ax.bar(range(7), dow.values, color=[C_VIOLET if d in ["Saturday","Sunday"] else C_INDIGO for d in DAY_ORDER], edgecolor=PLOT_BG, linewidth=1.0, zorder=3, width=0.6)
            ax.set_xticks(range(7)); ax.set_xticklabels([d[:3] for d in DAY_ORDER], color=TEXT_CLR)
            ax.set_title("Avg Withdrawals by Day of Week", fontweight="bold"); ax.set_ylabel("₹ Withdrawals")
            fig.tight_layout(); st.pyplot(fig); plt.close()
            ins("<strong>Weekend peak:</strong> Saturday & Sunday show highest demand — pre-load cash on Friday evenings.")
        with c2:
            tod   = df_exp.groupby("Time_of_Day")["Total_Withdrawals"].mean().reindex(["Morning","Afternoon","Evening","Night"])
            fig, ax = dark_fig(6, 4)
            bars = ax.bar(tod.index, tod.values, color=[C_AMBER,C_ORANGE,C_ROSE,C_VIOLET], edgecolor=PLOT_BG, linewidth=1.0, zorder=3, width=0.5)
            for b, v in zip(bars, tod.values):
                ax.text(b.get_x()+b.get_width()/2, b.get_height()+300, f"₹{v/1000:.0f}K", ha="center", va="bottom", fontsize=9, color=C_TXT1, fontweight="700")
            ax.set_title("Avg Withdrawals by Time of Day", fontweight="bold"); ax.set_ylabel("₹ Withdrawals")
            fig.tight_layout(); st.pyplot(fig); plt.close()
            ins("<strong>Afternoon/Evening peaks</strong> — schedule refills before 2 PM daily.")

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            w_order = ["Sunny","Cloudy","Rainy","Stormy"]
            w_avg   = df_exp.groupby("Weather_Condition")["Total_Withdrawals"].mean().reindex(w_order).dropna()
            fig, ax = dark_fig(6, 4)
            bars = ax.bar(w_avg.index, w_avg.values, color=[WX_COLORS.get(w,C_CYAN) for w in w_avg.index], edgecolor=PLOT_BG, linewidth=1.0, zorder=3, width=0.5)
            for b, v in zip(bars, w_avg.values):
                ax.text(b.get_x()+b.get_width()/2, b.get_height()+300, f"₹{v/1000:.0f}K", ha="center", va="bottom", fontsize=9, color=C_TXT1, fontweight="700")
            ax.set_title("Avg Withdrawals by Weather", fontweight="bold"); ax.set_ylabel("₹ Withdrawals")
            fig.tight_layout(); st.pyplot(fig); plt.close()
        with c2:
            fig, ax = dark_fig(6, 4)
            for i, w in enumerate(w_order):
                sub = df_exp[df_exp["Weather_Condition"]==w]["Total_Withdrawals"]
                if sub.empty: continue
                clr = WX_COLORS.get(w, C_CYAN)
                parts = ax.violinplot(sub, positions=[i], showmedians=True, showextrema=False)
                for pc in parts["bodies"]: pc.set_facecolor(clr); pc.set_alpha(0.55)
                parts["cmedians"].set_color(clr); parts["cmedians"].set_linewidth(2)
            ax.set_xticks(range(len(w_order))); ax.set_xticklabels(w_order, color=TEXT_CLR)
            ax.set_title("Withdrawal Distribution by Weather", fontweight="bold"); ax.set_ylabel("₹ Withdrawals")
            fig.tight_layout(); st.pyplot(fig); plt.close()

    with tab4:
        num_cols = ["Total_Withdrawals","Total_Deposits","Previous_Day_Cash_Level",
                    "Holiday_Flag","Special_Event_Flag","Nearby_Competitor_ATMs","Cash_Demand_Next_Day"]
        corr = df_exp[num_cols].corr()
        fig, ax = plt.subplots(figsize=(9, 6))
        fig.patch.set_facecolor(PLOT_BG); ax.set_facecolor(PLOT_BG)
        cmap = LinearSegmentedColormap.from_list("tbsm", ["#060912","#22D3EE","#6366F1","#8B5CF6"])
        sns.heatmap(corr, ax=ax, annot=True, fmt=".2f", cmap=cmap,
                    mask=np.triu(np.ones_like(corr, dtype=bool)),
                    linewidths=1, linecolor=PLOT_BG, square=True,
                    annot_kws={"size":9,"color":"#F0F4FF"}, cbar_kws={"shrink":.75})
        ax.tick_params(colors=TEXT_CLR, rotation=30, labelsize=8)
        ax.set_title("Correlation Matrix – Numerical Features", fontweight="bold", color="#F0F4FF")
        fig.tight_layout(); st.pyplot(fig); plt.close()
        ins("<strong>Total_Withdrawals → Cash_Demand_Next_Day</strong> has the strongest correlation (~0.85) — the primary predictor.")

    with tab5:
        c1, c2 = st.columns(2)
        with c1:
            fig, ax = dark_fig(6, 4)
            ax.hist(df_exp["Total_Withdrawals"], bins=45, color=C_INDIGO, edgecolor=PLOT_BG, linewidth=0.4, alpha=0.85)
            m_ = df_exp["Total_Withdrawals"].mean(); md_ = df_exp["Total_Withdrawals"].median()
            ax.axvline(m_,  color=C_ROSE,  linestyle="--", linewidth=2, label=f"Mean ₹{m_:,.0f}")
            ax.axvline(md_, color=C_AMBER, linestyle="--", linewidth=2, label=f"Median ₹{md_:,.0f}")
            ax.legend(fontsize=8, framealpha=0); ax.set_title("Withdrawal Distribution", fontweight="bold")
            ax.set_xlabel("₹ Withdrawals"); ax.set_ylabel("Frequency")
            fig.tight_layout(); st.pyplot(fig); plt.close()
        with c2:
            daily = df_exp.groupby("Date")["Total_Withdrawals"].sum().reset_index()
            daily["MA7"] = daily["Total_Withdrawals"].rolling(7, min_periods=1).mean()
            fig, ax = dark_fig(6, 4)
            ax.fill_between(daily["Date"], daily["Total_Withdrawals"], alpha=0.07, color=C_CYAN)
            ax.plot(daily["Date"], daily["Total_Withdrawals"], color=C_CYAN, linewidth=0.7, alpha=0.55)
            ax.plot(daily["Date"], daily["MA7"], color=C_AMBER, linewidth=2.2, label="7-Day MA")
            ax.legend(fontsize=8, framealpha=0); ax.set_title("Daily Trend + 7-Day Moving Average", fontweight="bold")
            ax.set_xlabel("Date"); ax.set_ylabel("₹ Withdrawals")
            fig.tight_layout(); st.pyplot(fig); plt.close()


def page_anomaly(df, Q1, Q3, IQR):
    sec("Anomaly Detection", "AI-powered identification of unusual withdrawal patterns across the ATM network.")
    anomaly_df  = df[df["Is_Anomaly"]].nlargest(12, "Total_Withdrawals").copy()
    normal_df   = df[~df["Is_Anomaly"]]
    upper_bound = Q3 + 1.5 * IQR
    n_inv       = len(st.session_state.investigated)

    col_main, col_side = st.columns([1.5, 1])
    with col_main:
        n_found = len(anomaly_df)
        inv_pct = int(n_inv / n_found * 100) if n_found else 0
        st.markdown(f"""
        <div style='background:linear-gradient(135deg,rgba(251,113,133,0.05),rgba(8,12,24,0.92));
                    border:1px solid rgba(251,113,133,0.18);border-radius:18px;
                    padding:20px 24px;margin-bottom:20px;
                    display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;
                    backdrop-filter:blur(14px);box-shadow:0 0 38px rgba(251,113,133,0.06);'>
            <div>
                <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:1rem;color:var(--t1);margin-bottom:10px;'>🔍 Anomaly Triage</div>
                <div style='display:flex;gap:8px;align-items:center;flex-wrap:wrap;'>
                    <span class='risk-pill high'>{n_found} DETECTED</span>
                    <span class='risk-pill low'>{n_inv} INVESTIGATED</span>
                    <span class='risk-pill med'>{n_found - n_inv} PENDING</span>
                </div>
            </div>
            <div style='text-align:right;'>
                <div style='font-size:.6rem;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;
                            color:var(--t4);margin-bottom:6px;font-family:JetBrains Mono,monospace;'>Investigation Progress</div>
                <div style='width:180px;height:8px;background:rgba(251,113,133,0.12);border-radius:99px;'>
                    <div style='width:{inv_pct}%;height:8px;
                                background:linear-gradient(90deg,var(--cg),var(--c2));
                                border-radius:99px;box-shadow:0 0 10px rgba(52,211,153,0.4);'></div>
                </div>
                <div style='font-size:.76rem;font-weight:700;color:var(--cg);margin-top:5px;'>{inv_pct}% resolved</div>
            </div>
        </div>""", unsafe_allow_html=True)

        max_z = df["Z_Score"].max()
        for idx, (_, row) in enumerate(anomaly_df.iterrows()):
            row_id     = f"{row['ATM_ID']}_{row['Date'].strftime('%Y%m%d')}"
            is_inv     = row_id in st.session_state.investigated
            risk_score = min(int((row["Z_Score"] / max_z) * 100), 99)
            if is_inv:
                risk_cls, risk_label = "done","✓ INVESTIGATED"; card_extra="investigated"; icon_cls="ok"; icon_sym="✅"
            elif risk_score >= 70:
                risk_cls, risk_label = "high",f"🔴 HIGH {risk_score}%"; card_extra="high-risk"; icon_cls="alert"; icon_sym="🚨"
            elif risk_score >= 40:
                risk_cls, risk_label = "med",f"🟡 MED {risk_score}%"; card_extra=""; icon_cls="warn"; icon_sym="⚠️"
            else:
                risk_cls, risk_label = "low",f"🟢 LOW {risk_score}%"; card_extra=""; icon_cls="warn"; icon_sym="📊"
            iqr_tag = "&nbsp;·&nbsp;<span style='color:var(--co);'>IQR breach</span>" if row["Anomaly_IQR"] else ""
            st.markdown(f"""
            <div class='anom-card {card_extra}'>
                <div class='anom-hdr'>
                    <div class='anom-row'>
                        <div class='anom-ico {icon_cls}'>{icon_sym}</div>
                        <div>
                            <div style='display:flex;align-items:center;gap:8px;margin-bottom:3px;'>
                                <span class='anom-date'>{row["Date"].strftime("%Y-%m-%d")}</span>
                                <span class='risk-pill {risk_cls}'>{risk_label}</span>
                            </div>
                            <div class='anom-name'>{row["Location_Type"]} — {row["ATM_ID"]}</div>
                        </div>
                    </div>
                    <div>
                        <div class='anom-val'>₹{row["Total_Withdrawals"]:,.0f}</div>
                        <div class='anom-lbl'>Withdrawal</div>
                    </div>
                </div>
                <div class='anom-reason'>
                    <strong>Z-score:</strong> {row["Z_Score"]:.2f}{iqr_tag}
                    &nbsp;·&nbsp; Holiday: {"Yes 🎉" if row["Holiday_Flag"] else "No"}
                    &nbsp;·&nbsp; Event: {"Yes ⭐" if row["Special_Event_Flag"] else "No"}
                </div>
            </div>""", unsafe_allow_html=True)
            if not is_inv:
                if st.button(f"🔎  Investigate {row['ATM_ID']}", key=f"inv_{idx}_{row_id}"):
                    st.session_state.investigated.append(row_id); st.rerun()
            else:
                st.button("✓ Investigated", key=f"inv_{idx}_{row_id}", disabled=True)

    with col_side:
        hol_rate  = df[df["Holiday_Flag"]==1]["Is_Anomaly"].mean() * 100
        norm_rate = df[df["Holiday_Flag"]==0]["Is_Anomaly"].mean() * 100
        st.markdown(f"""
        <div class='glass-panel'>
            <div class='gp-title'><div class='gp-icon'>🔍</div>Detection Logic</div>
            <div style='margin-bottom:15px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Z-Score Method</div>
                <div style='font-size:.81rem;color:var(--t3);line-height:1.65;'>Withdrawals with |z| &gt; 3.0 are flagged — more than 3σ from mean.</div>
            </div>
            <div style='margin-bottom:15px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>IQR Method</div>
                <div style='font-size:.81rem;color:var(--t3);line-height:1.65;'>Records exceeding Q3 + 1.5×IQR (upper: ₹{upper_bound:,.0f}) flagged.</div>
            </div>
            <div style='margin-bottom:15px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Holiday Correlation</div>
                <div style='font-size:.81rem;color:var(--t3);line-height:1.65;'>
                    Holiday: <span style='color:var(--ca);font-weight:700;'>{hol_rate:.1f}%</span> vs
                    <span style='color:var(--cg);font-weight:700;'>{norm_rate:.1f}%</span> normal.
                </div>
            </div>
            <div class='gp-status'><span>SYSTEM STATUS</span><span class='live-label'>● LIVE</span></div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        k1, k2 = st.columns(2)
        with k1: st.markdown(f"<div class='kpi-card green' style='text-align:center;'><div class='kpi-lbl'>NORMAL</div><div class='kpi-val' style='color:var(--cg);font-size:1.8rem;'>{len(normal_df):,}</div></div>", unsafe_allow_html=True)
        with k2: st.markdown(f"<div class='kpi-card rose' style='text-align:center;'><div class='kpi-lbl'>ANOMALIES</div><div class='kpi-val' style='color:var(--cr);font-size:1.8rem;'>{df['Is_Anomaly'].sum()}</div></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        fig, ax = dark_fig(5, 3.5)
        n_, _, _ = ax.hist(df["Z_Score"], bins=55, color=C_INDIGO, edgecolor=PLOT_BG, linewidth=0.3, alpha=0.85)
        ax.hist(df[df["Z_Score"]>3]["Z_Score"], bins=30, color=C_ROSE, edgecolor=PLOT_BG, linewidth=0.3, alpha=0.9)
        ax.axvline(3.0, color=C_AMBER, linestyle="--", linewidth=2, label="z=3.0")
        ax.fill_betweenx([0, n_.max()*1.1], 3.0, df["Z_Score"].max(), alpha=0.07, color=C_ROSE)
        ax.set_ylim(0, n_.max()*1.15)
        ax.set_xlabel("Z-Score"); ax.set_ylabel("Frequency"); ax.set_title("Z-Score Distribution", fontweight="bold")
        ax.legend(fontsize=8, framealpha=0); fig.tight_layout(); st.pyplot(fig); plt.close()

        anom_tl = df[df["Is_Anomaly"]].groupby("Date").size().reset_index(name="n")
        if not anom_tl.empty:
            fig, ax = dark_fig(5, 2.5)
            ax.bar(anom_tl["Date"], anom_tl["n"], color=C_ROSE, edgecolor=PLOT_BG, linewidth=0.3, alpha=0.85, width=3)
            ax.set_title("Anomaly Timeline", fontweight="bold"); ax.set_ylabel("Count")
            fig.tight_layout(); st.pyplot(fig); plt.close()

        if st.session_state.investigated:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("↺  Reset Investigations", key="reset_inv"):
                st.session_state.investigated = []; st.rerun()


def page_forecasting(df):
    sec("Forecasting", "Predict next-day ATM cash demand using historical patterns.")
    col_main, col_side = st.columns([1.8, 1])
    with col_main:
        loc_sel = st.selectbox("📍 Select Location Type", ["Urban","Suburban","Rural"])
        df_loc  = df[df["Location_Type"]==loc_sel]
        daily   = df_loc.groupby("Date")["Total_Withdrawals"].sum().reset_index().sort_values("Date")
        daily["MA7"]  = daily["Total_Withdrawals"].rolling(7,  min_periods=1).mean()
        daily["MA30"] = daily["Total_Withdrawals"].rolling(30, min_periods=1).mean()
        last_val     = daily["MA7"].iloc[-1]
        trend_slope  = (daily["MA7"].iloc[-1] - daily["MA7"].iloc[-8]) / 7 if len(daily) >= 8 else 0
        future_dates = pd.date_range(daily["Date"].iloc[-1] + pd.Timedelta(days=1), periods=14, freq="D")
        future_vals  = [last_val + trend_slope * i for i in range(1, 15)]
        upper_band   = [v * 1.07 for v in future_vals]
        lower_band   = [v * 0.93 for v in future_vals]

        fig, ax = dark_fig(11, 4.8)
        ax.fill_between(daily["Date"], daily["Total_Withdrawals"], alpha=0.06, color=C_CYAN)
        ax.plot(daily["Date"], daily["Total_Withdrawals"], color=C_CYAN, linewidth=0.7, alpha=0.5, label="Actual")
        ax.plot(daily["Date"], daily["MA7"],  color=C_TEAL,  linewidth=2.0, label="7-Day MA")
        ax.plot(daily["Date"], daily["MA30"], color=C_INDIGO, linewidth=1.6, linestyle="--", label="30-Day MA")
        ax.fill_between(future_dates, lower_band, upper_band, alpha=0.15, color=C_AMBER)
        ax.plot(future_dates, future_vals, color=C_AMBER, linewidth=2.4, linestyle="--", label="14-Day Forecast")
        ax.axvline(daily["Date"].iloc[-1], color=C_ROSE, linewidth=1.2, linestyle=":", alpha=0.7)
        ax.text(daily["Date"].iloc[-1], ax.get_ylim()[1]*0.95, " ← History | Forecast →", color=C_ROSE, fontsize=8, va="top")
        ax.legend(fontsize=8, framealpha=0); ax.set_title(f"{loc_sel} ATM Network — 14-Day Cash Demand Forecast", fontweight="bold", pad=12)
        ax.set_xlabel("Date"); ax.set_ylabel("₹ Withdrawals")
        fig.tight_layout(); st.pyplot(fig); plt.close()
        ins(f"Forecast horizon: 14 days · trend: <strong>{round(trend_slope/last_val*100,1):+.1f}%/day</strong>. Shaded = ±7% confidence band.")

        div()
        heat_df = df.copy()
        heat_df["Month"]   = heat_df["Date"].dt.month_name().str[:3]
        heat_df["DayOfWk"] = heat_df["Day_of_Week"].map({d:i for i,d in enumerate(DAY_ORDER)})
        pivot = heat_df.groupby(["Month","DayOfWk"])["Total_Withdrawals"].mean().unstack(fill_value=0)
        pivot.columns = [DAY_ORDER[i] for i in pivot.columns]
        m_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        pivot = pivot.reindex([m for m in m_order if m in pivot.index])
        cmap_h = LinearSegmentedColormap.from_list("heat",[PLOT_BG,"#1E1B4B",C_INDIGO,C_CYAN,C_AMBER])
        fig, ax = plt.subplots(figsize=(11, 5))
        fig.patch.set_facecolor(PLOT_BG); ax.set_facecolor(PLOT_BG)
        sns.heatmap(pivot, ax=ax, cmap=cmap_h, annot=True, fmt=".0f", linewidths=0.8, linecolor=PLOT_BG, annot_kws={"size":7.5,"color":"#F0F4FF"})
        ax.set_title("Avg Withdrawals by Month × Day of Week", fontweight="bold", color="#F0F4FF")
        ax.tick_params(colors=TEXT_CLR, labelsize=8); fig.tight_layout(); st.pyplot(fig); plt.close()

    with col_side:
        next_val = future_vals[0]; week_total = sum(future_vals[:7])
        st.markdown(f"""
        <div class='glass-panel' style='margin-bottom:16px;'>
            <div class='gp-title'><div class='gp-icon'>🔮</div>Forecast Summary</div>
            <div style='margin-bottom:14px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Next Day Forecast</div>
                <div style='font-family:Orbitron,sans-serif;font-size:1.9rem;font-weight:800;color:var(--t1);text-shadow:0 0 18px rgba(255,255,255,0.1);'>₹{next_val/1000:.1f}K</div>
            </div>
            <div style='border-top:1px solid rgba(255,255,255,0.05);padding-top:14px;margin-top:4px;margin-bottom:14px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>7-Day Total</div>
                <div style='font-family:Orbitron,sans-serif;font-size:1.45rem;font-weight:800;color:var(--c2);text-shadow:0 0 14px rgba(34,211,238,0.4);'>₹{week_total/1e6:.2f}M</div>
            </div>
            <div style='border-top:1px solid rgba(255,255,255,0.05);padding-top:14px;margin-top:4px;'>
                <div style='font-size:.59rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--c2);margin-bottom:5px;font-family:JetBrains Mono,monospace;'>Method</div>
                <div style='font-size:.81rem;color:var(--t3);line-height:1.65;'>7-Day MA + linear trend · ±7% confidence band</div>
            </div>
            <div class='gp-status'><span>FORECAST STATUS</span><span class='live-label'>● ACTIVE</span></div>
        </div>""", unsafe_allow_html=True)

        top5 = (df[df["Location_Type"]==loc_sel].groupby("ATM_ID")["Total_Withdrawals"].mean().nlargest(5).reset_index())
        st.markdown("""<div style='background:rgba(10,15,28,0.82);border:1px solid var(--bdr);border-radius:18px;padding:20px;backdrop-filter:blur(14px);box-shadow:0 4px 18px rgba(0,0,0,0.2);'>
        <div style='font-family:Rajdhani,sans-serif;font-weight:700;font-size:.96rem;color:var(--t1);margin-bottom:14px;'>🏆 Top 5 ATMs by Avg Demand</div>""",
            unsafe_allow_html=True)
        rank_clrs = [C_AMBER, C_ORANGE, C_INDIGO, C_TEAL, C_VIOLET]
        for rank, (_, row) in enumerate(top5.iterrows()):
            clr = rank_clrs[rank % len(rank_clrs)]
            st.markdown(f"""
            <div style='display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04);'>
                <div style='display:flex;align-items:center;gap:9px;'>
                    <div style='width:24px;height:24px;border-radius:7px;background:{clr};display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:800;color:#000;'>{rank+1}</div>
                    <div style='font-size:.84rem;font-weight:700;color:var(--t1);'>{row["ATM_ID"]}</div>
                </div>
                <div style='font-size:.84rem;color:var(--c2);font-weight:700;'>₹{row["Total_Withdrawals"]/1000:.1f}K</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


def page_insights(df, df_all):
    sec("Insights", "Data-driven recommendations for ATM cash management and optimisation.")
    urban_avg  = df[df["Location_Type"]=="Urban"]["Total_Withdrawals"].mean()
    suburb_avg = df[df["Location_Type"]=="Suburban"]["Total_Withdrawals"].mean()
    rural_avg  = df[df["Location_Type"]=="Rural"]["Total_Withdrawals"].mean()
    pct_hol    = (df[df["Holiday_Flag"]==1]["Total_Withdrawals"].mean() / df[df["Holiday_Flag"]==0]["Total_Withdrawals"].mean() - 1) * 100

    if st.session_state.strategy_applied:
        st.markdown("<div class='ok-banner'>✅ Strategy applied! Urban ATM cash loads increased by 20% for Friday evenings.</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='hero-insights'>
        <div class='hero-badge'>⭐ OPTIMISATION STRATEGY</div>
        <div class='hero-title'>TBSM Bank<br><span class='hl'>Replenishment</span> <span class='hl2'>Protocol 2026</span></div>
        <div class='hero-body'>
            Analysis recommends increasing cash supply by <strong>20% for Urban ATMs</strong> every Friday evening.
            Suburban: bi-weekly refills. Rural: festival/holiday periods only.
            Projected savings: <strong>₹12.4 Cr/year</strong> from reduced emergency refills.
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 1, 2])
    with b1:
        if st.button("⚡ Apply Strategy", key="apply_strategy"): st.session_state.strategy_applied = True; st.rerun()
    with b2:
        if st.button("📈 Simulate Impact", key="simulate"): st.session_state.simulation_run = True; st.rerun()
    with b3:
        report_df = pd.DataFrame({
            "Metric":["Urban Avg","Suburban Avg","Rural Avg","Holiday Lift","Anomalies","Urban Increase"],
            "Value": [f"₹{urban_avg:,.0f}",f"₹{suburb_avg:,.0f}",f"₹{rural_avg:,.0f}",f"+{pct_hol:.1f}%",str(df["Is_Anomaly"].sum()),"20%"],
        })
        st.download_button("📥 Export Insights Report", data=report_df.to_csv(index=False),
                           file_name="tbsm_insights_report.csv", mime="text/csv", key="export_insights")

    if st.session_state.simulation_run:
        sim_pct    = st.slider("📊 Urban cash increase (%)", 5, 40, st.session_state.sim_pct, 5, key="sim_slider")
        st.session_state.sim_pct = sim_pct
        savings    = urban_avg * (sim_pct/100) * 0.40 * 365
        reduction  = min(sim_pct * 1.5, 60)
        extra_cost = urban_avg * (sim_pct/100) * 0.08 * 365
        net        = savings - extra_cost
        st.markdown(f"""
        <div class='sim-result'>
            <div style='font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--cg);margin-bottom:10px;font-family:JetBrains Mono,monospace;'>
                📈 Simulation · {sim_pct}% Urban Increase
            </div>
            <div class='sim-val'>₹{net/1e7:.2f} Cr</div>
            <div style='font-size:.78rem;color:var(--t4);margin-top:6px;'>Net annual savings (savings minus carrying cost)</div>
            <div style='margin-top:18px;display:flex;gap:24px;justify-content:center;flex-wrap:wrap;'>
                {''.join([f"<div style='text-align:center;'><div style='font-size:.62rem;font-weight:700;color:{c};letter-spacing:1px;text-transform:uppercase;font-family:JetBrains Mono,monospace;'>{l}</div><div style='font-family:Orbitron,sans-serif;font-size:1.3rem;font-weight:800;color:{c};'>{v}</div></div>" for l,v,c in [("Cash-Out Reduction",f"{reduction:.0f}%",C_GREEN),("Gross Savings",f"₹{savings/1e7:.2f} Cr",C_GREEN),("Carry Cost",f"₹{extra_cost/1e7:.2f} Cr",C_AMBER)]])}
            </div>
        </div>""", unsafe_allow_html=True)

    div()
    k1, k2, k3, k4 = st.columns(4)
    kpi_card(k1,"🏙️","indigo","URBAN AVG",    f"₹{urban_avg/1000:.0f}K", "Per transaction",trend=4.2)
    kpi_card(k2,"🏘️","teal",  "SUBURBAN AVG", f"₹{suburb_avg/1000:.0f}K","Per transaction",trend=1.8)
    kpi_card(k3,"🌾","amber", "RURAL AVG",    f"₹{rural_avg/1000:.0f}K", "Per transaction",trend=-0.5)
    kpi_card(k4,"🎉","violet","HOLIDAY LIFT", f"+{pct_hol:.0f}%","vs. regular days")
    div()

    c1, c2 = st.columns(2)
    with c1:
        loc_avg = df.groupby("Location_Type")["Total_Withdrawals"].mean().sort_values()
        fig, ax = dark_fig(6, 4)
        hbars = ax.barh(loc_avg.index, loc_avg.values, color=[LOC_COLORS.get(l,C_INDIGO) for l in loc_avg.index], edgecolor=PLOT_BG, height=0.5, zorder=3)
        for b, v in zip(hbars, loc_avg.values):
            ax.text(v+400, b.get_y()+b.get_height()/2, f"₹{v:,.0f}", va="center", fontsize=9, color="#F0F4FF", fontweight="700")
        ax.set_title("Avg Withdrawals by Location", fontweight="bold"); ax.set_xlabel("₹ Withdrawals")
        fig.tight_layout(); st.pyplot(fig); plt.close()
    with c2:
        cl_df, _ = run_clustering(df_all)
        clust_cnt = cl_df["Cluster"].value_counts()
        fig, ax = dark_fig(6, 4)
        bars = ax.bar(clust_cnt.index, clust_cnt.values, color=[CL_COLORS.get(c,C_INDIGO) for c in clust_cnt.index], edgecolor=PLOT_BG, linewidth=1, width=0.5, zorder=3)
        for b, v in zip(bars, clust_cnt.values):
            ax.text(b.get_x()+b.get_width()/2, b.get_height()+4, str(v), ha="center", va="bottom", fontsize=9, color="#F0F4FF", fontweight="700")
        ax.set_title("K-Means Cluster Distribution (k=3)", fontweight="bold"); ax.set_ylabel("Records"); ax.tick_params(axis="x", rotation=10)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    div()
    sample = cl_df.sample(min(400, len(cl_df)), random_state=42)
    fig, ax = dark_fig(12, 4.5)
    for cluster, grp in sample.groupby("Cluster"):
        ax.scatter(grp["Total_Withdrawals"], grp["Total_Deposits"], c=CL_COLORS[cluster], label=cluster, alpha=0.60, s=28, edgecolors=PLOT_BG, linewidths=0.4)
    ax.set_xlabel("Total Withdrawals (₹)"); ax.set_ylabel("Total Deposits (₹)")
    ax.set_title("K-Means Clusters: Withdrawals vs Deposits", fontweight="bold")
    ax.legend(fontsize=9, framealpha=0.1, facecolor=PLOT_BG, labelcolor="#F0F4FF")
    fig.tight_layout(); st.pyplot(fig); plt.close()

    _, inertias = run_clustering(df_all)
    fig, ax = dark_fig(8, 3.5)
    ax.plot(range(1,11), inertias, color=C_CYAN, linewidth=2.5, marker="o", markersize=7, markerfacecolor=C_AMBER, markeredgecolor=PLOT_BG)
    ax.axvline(3, color=C_ROSE, linestyle="--", linewidth=1.8, label="Chosen k=3")
    ax.set_xlabel("Number of Clusters (k)"); ax.set_ylabel("Inertia"); ax.set_title("Elbow Method for Optimal Cluster Count", fontweight="bold")
    ax.legend(fontsize=9, framealpha=0); fig.tight_layout(); st.pyplot(fig); plt.close()


def page_storyboard(df):
    sec("Storyboard", "The complete analytical journey from raw data to actionable banking decisions.")
    tag_grads = [
        "linear-gradient(135deg,#4338CA,#6D28D9)",
        "linear-gradient(135deg,#0D9488,#0891B2)",
        "linear-gradient(135deg,#B45309,#D97706)",
        "linear-gradient(135deg,#065F46,#0D9488)",
        "linear-gradient(135deg,#0369A1,#0284C7)",
        "linear-gradient(135deg,#9F1239,#DB2777)",
        "linear-gradient(135deg,#5B21B6,#DB2777)",
        "linear-gradient(135deg,#B45309,#4338CA)",
    ]
    story_steps = [
        ("Business Problem","TBSM Bank operates 100 ATMs across Urban, Suburban, and Rural locations. Frequent cash-outs during weekends and holidays cause customer dissatisfaction and operational losses.","💼 Problem Definition"),
        ("Data Collection & Upload","1,200 transaction records collected spanning January–December 2023. Each record captures ATM ID, date, location, withdrawal/deposit amounts, weather condition, holiday flags, and competitor proximity.","📤 Data Ingestion"),
        ("Data Cleaning & Preparation","Date features extracted (day of week, month). Categorical variables label-encoded. Missing values: 0 detected. Normalisation applied for clustering models. All 4 pipeline steps passed.","🧹 Data Prep"),
        ("Exploratory Analysis","Urban ATMs average ₹50K/day vs ₹15K for Rural. Weekends drive 18% higher demand. Afternoon/Evening slots account for 60% of all transactions. Holidays boost withdrawals by ~15%.","📊 EDA Findings"),
        ("Clustering (K-Means, k=3)","Three demand segments emerged: High Demand (Urban, event-prone), Medium Demand (Suburban, stable), Low Demand (Rural, infrequent). Elbow method confirmed k=3.","🔵 Clustering"),
        ("Anomaly Detection",f"Z-score (|z|>3) and IQR methods identified {df['Is_Anomaly'].sum()} anomalous records (≈{df['Is_Anomaly'].mean()*100:.1f}% of dataset). Holiday anomaly rate significantly elevated.","⚠️ Anomalies"),
        ("Forecasting","Rolling 7-day and 30-day MAs with linear trend extrapolation deliver 14-day ahead demand forecasts per location. Monthly heatmaps surface seasonal patterns.","🔮 Forecasting"),
        ("Actionable Recommendations","Pre-load Urban ATMs every Friday evening (+20% cash). Alert threshold: ₹80K+ single transaction. Rural ATM refills bi-monthly except during festival periods.","💡 Recommendations"),
    ]
    for i, ((title, body, tag), grad) in enumerate(zip(story_steps, tag_grads), 1):
        st.markdown(f"""
        <div class='story-card'>
            <div style='display:flex;align-items:flex-start;gap:18px;'>
                <div style='width:40px;height:40px;flex-shrink:0;margin-top:2px;background:{grad};border-radius:50%;
                            display:flex;align-items:center;justify-content:center;
                            font-family:Orbitron,sans-serif;font-weight:900;font-size:.88rem;color:#fff;
                            box-shadow:0 6px 18px rgba(0,0,0,0.4);'>{i}</div>
                <div class='story-content'>
                    <div class='story-title'>{title}</div>
                    <div class='story-text'>{body}</div>
                    <div class='story-tag'>{tag}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    n_anom = df["Is_Anomaly"].sum()
    st.markdown(f"""
    <div style='background:linear-gradient(150deg,rgba(4,8,18,.97) 0%,rgba(7,7,28,.94) 50%,rgba(3,12,10,.97) 100%);
                border-radius:22px;padding:42px 46px;color:var(--t1);margin-top:8px;
                border:1px solid rgba(52,211,153,0.17);position:relative;overflow:hidden;
                backdrop-filter:blur(20px);box-shadow:0 0 55px rgba(52,211,153,0.06);'>
        <div style='position:absolute;right:-50px;top:-50px;width:220px;height:220px;
                    background:radial-gradient(circle,rgba(52,211,153,0.14) 0%,transparent 70%);border-radius:50%;'></div>
        <div style='font-family:Orbitron,sans-serif;font-size:1.5rem;font-weight:900;margin-bottom:12px;letter-spacing:1px;'>🎉 Project Complete</div>
        <div style='font-size:.88rem;color:var(--t3);line-height:1.85;margin-bottom:26px;'>
            This pipeline transformed <strong style='color:var(--t1);'>1,200 raw ATM records</strong>
            into a structured intelligence system — predicting cash demand, detecting anomalous withdrawals, and delivering optimised replenishment schedules.
        </div>
        <div style='display:flex;gap:14px;flex-wrap:wrap;'>
            {''.join([f"<div style='background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:16px 22px;text-align:center;'><div style='font-family:Orbitron,sans-serif;font-size:1.5rem;font-weight:900;color:{c};text-shadow:0 0 18px {c}44;'>{v}</div><div style='font-size:.59rem;color:{sc};letter-spacing:1.5px;text-transform:uppercase;margin-top:5px;font-family:JetBrains Mono,monospace;'>{l}</div></div>" for v,l,c,sc in [("1,200","RECORDS","#34D399","#6EE7B7"),(str(n_anom),"ANOMALIES","#22D3EE","#67E3FF"),("3","CLUSTERS","#8B5CF6","#C4B5FD"),("100","ATMs","#FB7185","#FCA5A5"),("8","STEPS","#FBBF24","#FDE68A")]])}
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    story_df = pd.DataFrame(story_steps, columns=["Title","Body","Tag"])
    st.download_button("⬇️  Export Full Storyboard as CSV", data=story_df.to_csv(index=False),
                       file_name="tbsm_storyboard.csv", mime="text/csv", key="export_storyboard")


# ══════════════════════════════════════════════════════════════════
# ████████  MAIN DASHBOARD  ████████
# ══════════════════════════════════════════════════════════════════
def show_dashboard():
    with st.spinner("Initialising ATM Intelligence System…"):
        df_raw          = generate_dataset(1200)
        df_cl, inertias = run_clustering(df_raw)
        df_all, Q1, Q3, IQR = run_anomaly(df_cl)

    n_anom = int(df_all["Is_Anomaly"].sum())

    render_sidebar(df_all, n_anom)

    page       = st.session_state.get("current_page", "🏠  Home")
    page_label = page.split("  ", 1)[-1] if "  " in page else page[2:]
    render_topbar(page_label, n_anom)

    df = df_all.copy()
    if   page == "🏠  Home":              page_home(df, n_anom)
    elif page == "🎯  Project Scope":     page_scope(df)
    elif page == "📤  Data Upload":       page_upload(df_all)
    elif page == "🧹  Data Cleaning":     page_cleaning()
    elif page == "📊  Exploration":       page_exploration(df)
    elif page == "⚠️  Anomaly Detection": page_anomaly(df, Q1, Q3, IQR)
    elif page == "🔮  Forecasting":       page_forecasting(df)
    elif page == "💡  Insights":          page_insights(df, df_all)
    elif page == "📖  Storyboard":        page_storyboard(df)


# ══════════════════════════════════════════════════════════════════
# ████████  ROUTER  ████████
# ══════════════════════════════════════════════════════════════════
if not st.session_state.authenticated:
    show_login()
else:
    show_dashboard()