# 👑 CELLREVIVE AI - THE MASTER METABOLIC OS & CELLULAR RESTORATION PLATFORM (v21.5 - Persistent Memory)
# ==============================================================================
# Production-Ready Sovereign System (2026 International & Egyptian Drug Authority Standards)
# Designed & Supervised by: Dr. Ehab Heshmat El-Znny
# ==============================================================================

import streamlit as st
import sqlite3
import math
import numpy as np
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 0️⃣ الإعدادات السيادية الفاخرة لواجهة المستخدم والتصميم الملكي
st.set_page_config(
    page_title="CellRevive AI - Dr. Ehab Heshmat El-Znny",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

try:
    from cryptography.fernet import Fernet
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet

# تطبيق التصاميم الملكية الفاخرة المقاومة للتداخل لعام 2026
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=600;800;900&display=swap');
    .stApp { background-color: #040d1a; color: #ffffff !important; font-family: 'Cairo', sans-serif !important; }
    [data-testid="stMainBlockContainer"], .stTabs, div, p, span, label, h1, h2, h3, h4, h5, h6 { direction: rtl !important; text-align: right !important; }
    .premium-card { background: linear-gradient(145deg, #0a1f38, #07162c); border: 2px solid #d4af37; border-radius: 15px; padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2); }
    .emergency-card { background: linear-gradient(145deg, #1f0b0b, #110303); border: 2px solid #ff4b4b; border-radius: 15px; padding: 25px; margin-bottom: 20px; box-shadow: 0 0 20px rgba(255, 75, 75, 0.3); }
    label, p, span, h3, h4 { color: #ffffff !important; font-weight: 600 !important; }
    .stButton>button { background: linear-gradient(90deg, #f3e5ab, #d4af37, #aa8422) !important; color: #040d1a !important; border-radius: 12px !important; font-weight: 900 !important; font-size: 16px !important; height: 3.2em; width: 100%; border: none !important; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important; }
    .stButton>button:hover { transform: scale(1.01); box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important; }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div { background-color: #07162c !important; color: #ffffff !important; border: 1px solid #d4af37 !important; }
    .metric-value-green { font-size: 24px; color: #00ffcc !important; font-weight: 900; }
    .metric-value-gold { font-size: 24px; color: #d4af37 !important; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# ⚖️ وثيقة الأمان الطبي والالتزام الصارم والكامل
if 'disclaimer_agreed' not in st.session_state:
    st.session_state.disclaimer_agreed = False

if not st.session_state.disclaimer_agreed:
    st.markdown("""
        <div class="emergency-card" style="margin-top: 30px;">
            <h2 style="color: #ff4b4b !important; text-align: center !important; font-weight: 900; margin-bottom: 15px;">🛡️ وثيقة الأمان الطبي والالتزام المشترك / Legal Disclaimer</h2>
            <p style="font-size: 15px; line-height: 1.8; text-align: justify !important; color: #ffffff;">
                <b>تنبيه قانوني وطبي صارم:</b> إن منصة <b>CellRevive AI</b> هي منظومة محاكاة رقمية متقدمة وأداة تثقيفية مخصصة لدعم هندسة التمثيل الغذائي وتحسين كفاءة الميتوكوندريا تحت الإشراف العلمي المباشر للصيدلي المختص <b>د/ إيهاب حشمت الظني</b>. 
                <br><br>
                1. لا يعتبر this البرنامج أو التقارير الصادرة عنه بديلاً عن التشخيص الطبي البشري أو الفحوصات المختبرية السريرية.<br>
                2. يجب على كل مستخدم مراجعة طبيبه المعالج قبل تعديل أو إيقاف أي جرعات دوائية موصوفة، لا سيما أدوية السكري والضغط الكيميائية.<br>
                3. المنصة تخلي مسؤوليتها تماماً من أي استخدام أحادي للبيانات الحيوية خارج نطاق الاستشارة الطبية المباشرة والتوجيه المعتمد داخل العيادة.
            </p>
        </div>
    """, unsafe_allow_html=True)
    agree_check = st.checkbox("لقد قرأت وثيقة الأمان الطبي الشاملة وأوافق تماماً وبشكل صارم على بنودها القانونية.")
    if agree_check:
        if st.button("الانطلاق وبدء الاتصال بالمنصة الخلوية 🚀"):
            st.session_state.disclaimer_agreed = True
            st.rerun()
    st.stop()

# إعداد مفاتيح التشفير والـ API
if "EMERGENCY_STATIC_KEY" not in st.session_state:
    st.session_state["EMERGENCY_STATIC_KEY"] = Fernet.generate_key().decode()
KEY = st.session_state["EMERGENCY_STATIC_KEY"].encode()
cipher_suite = Fernet(KEY)

def encrypt_data(data_str): return cipher_suite.encrypt(data_str.encode()).decode() if data_str else ""
def decrypt_data(crypto_str):
    try: return cipher_suite.decrypt(crypto_str.encode()).decode() if crypto_str else ""
    except: return ""

if "GEMINI_API_KEY" in st.secrets: ACTIVE_API_KEY = st.secrets["GEMINI_API_KEY"]
elif "api_key_input" in st.session_state and st.session_state.api_key_input: ACTIVE_API_KEY = st.session_state.api_key_input
else: ACTIVE_API_KEY = ""

if ACTIVE_API_KEY: genai.configure(api_key=ACTIVE_API_KEY)

# الهيدر الملكي للمنصة
st.markdown("""
    <div style="text-align: center; padding: 10px; margin-bottom: 5px;">
        <h1 style="color: #d4af37; font-size: 38px; font-weight: 900; text-align: center !important;">👑 CELLREVIVE AI</h1>
        <p style="color: #f3e5ab !important; font-size: 17px; font-weight: 800; text-align: center !important;">
            تحت إشراف: د/ إيهاب حشمت الظني <br>
            صيدلي وأخصائي الترميم الخلوي وطب طول العمر وعكس مسار السكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 15px;">
    </div>
""", unsafe_allow_html=True)

# 1️⃣ قاعدة البيانات وزراعة البيانات الافتراضية للتشغيل الفوري
def init_db():
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_code TEXT PRIMARY KEY, fbg REAL, ppbg REAL, rbg REAL, hba1c REAL,
            weight REAL, waist REAL, creatinine REAL, age INTEGER, gender TEXT,
            skin_analysis TEXT, selected_drugs TEXT, mthfr_mutation TEXT, fto_variant TEXT,
            fasting_insulin REAL, hscrp REAL, compliance_score INTEGER, anxiety_score INTEGER DEFAULT 0
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM patients")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, creatinine, age, gender, mthfr_mutation, fto_variant, fasting_insulin, hscrp, compliance_score, anxiety_score, selected_drugs, skin_analysis) 
            VALUES ('CR-SOHAG-2026', 115.0, 145.0, 120.0, 6.2, 80.0, 95.0, 0.9, 42, 'Male', 'Normal (CC)', 'Normal (TT)', 10.5, 0.8, 95, 4, '', '')
        """)
    conn.commit()
    conn.close()

init_db()

# دوال العمليات الحسابية الطبية والأيضية
def calculate_homa_ir(fbg, fasting_insulin): 
    try: return round((float(fbg) * float(fasting_insulin)) / 405, 2) if float(fasting_insulin) > 0 else 1.0
    except: return 1.0

def calculate_egfr(age, weight, creatinine, gender):
    try:
        cr = float(creatinine)
        if cr <= 0: return 90.0
        val = ((140 - int(age)) * float(weight)) / (72 * cr)
        if str(gender).lower() in ['female', 'أنثى']: val *= 0.85
        return min(round(val, 2), 150.0)
    except: return 90.0

def calculate_biological_age(age, hba1c, homa_ir, hscrp, waist):
    try:
        a = float(age)
        h = float(hba1c) if hba1c is not None else 5.4
        ir = float(homa_ir) if homa_ir is not None else 1.5
        crp = float(hscrp) if hscrp is not None else 0.5
        w = float(waist) if waist is not None else 90.0
        return max(round(a + (h - 5.4)*2.5 + (ir - 1.5)*1.8 + (crp - 0.5)*1.2, 1), 18.0)
    except:
        return float(age)

def simulate_glucose_curve(base_fbg, sequence, gi_score):
    t = np.linspace(0, 180, 100)
    flatten_factor = 2.2 if (sequence in ["ألياف -> بروتين -> نشويات", "دهون وبروتين -> نشويات"]) else 1.0
    amplitude = (gi_score * 1.5) / flatten_factor
    k1 = 0.04 / (flatten_factor * 0.8)
    k2 = 0.02 * flatten_factor
    curve = float(base_fbg) + amplitude * (np.exp(-k2 * t) - np.exp(-k1 * t)) * 1.5
    return t, curve

# المصادقة المبدئية والعبور الأمن
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
VALID_PATIENT_CODES = ["CR-SOHAG-2026"]

if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None
if 'auth_code' not in st.session_state: st.session_state.auth_code = ""

if not st.session_state.is_auth:
    st.markdown('<div class="premium-card"><h3 style="text-align:center; color:#d4af37;">🔐 بروتوكول المصادقة الرقمية والعبور المشفّر</h3></div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود العبور الخاص بك:", type="password")
    if st.button("تأكيد الهوية الحيوية"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth = True; st.session_state.role = "doctor"; st.session_state.auth_code = MASTER_CODE; st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth = True; st.session_state.role = "patient"; st.session_state.auth_code = input_code; st.rerun()
        else: st.error("كود غير صحيح، يرجى مراجعة العيادة.")
    st.stop()

if 'active_patient_code' not in st.session_state:
    st.session_state.active_patient_code = st.session_state.auth_code if st.session_state.role == "patient" else "CR-SOHAG-2026"

# جلب البيانات الصريحة بناءً على الكود النشط
def get_patient_data():
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE patient_code = ?", (st.session_state.active_patient_code,))
    row = c.fetchone()
    conn.close()
    return row

row = get_patient_data()

if row:
    p_data = {
        'fbg': row['fbg'] if row['fbg'] is not None else 115.0,
        'ppbg': row['ppbg'] if row['ppbg'] is not None else 145.0,
        'rbg': row['rbg'] if row['rbg'] is not None else 120.0,
        'hba1c': row['hba1c'] if row['hba1c'] is not None else 6.2,
        'weight': row['weight'] if row['weight'] is not None else 80.0,
        'waist': row['waist'] if row['waist'] is not None else 95.0,
        'creatinine': row['creatinine'] if row['creatinine'] is not None else 0.9,
        'age': row['age'] if row['age'] is not None else 42,
        'gender': row['gender'] if row['gender'] is not None else 'Male',
        'skin_analysis': decrypt_data(row['skin_analysis']),
        'selected_drugs': decrypt_data(row['selected_drugs']),
        'mthfr_mutation': row['mthfr_mutation'] if row['mthfr_mutation'] is not None else 'Normal (CC)',
        'fto_variant': row['fto_variant'] if row['fto_variant'] is not None else 'Normal (TT)',
        'fasting_insulin': row['fasting_insulin'] if row['fasting_insulin'] is not None else 10.5,
        'hscrp': row['hscrp'] if row['hscrp'] is not None else 0.8,
        'compliance_score': row['compliance_score'] if row['compliance_score'] is not None else 95,
        'anxiety_score': row['anxiety_score'] if row['anxiety_score'] is not None else 4
    }
else:
    p_data = {'fbg': 115.0, 'ppbg': 145.0, 'rbg': 120.0, 'hba1c': 6.2, 'weight': 80.0, 'waist': 95.0, 'creatinine': 0.9, 'age': 42, 'gender': 'Male', 'skin_analysis': '', 'selected_drugs': '', 'mthfr_mutation': 'Normal (CC)', 'fto_variant': 'Normal (TT)', 'fasting_insulin': 10.5, 'hscrp': 0.8, 'compliance_score': 95, 'anxiety_score': 4}

if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:22px; font-weight:900; text-align:center;">👑 لوحة الإشراف العيادي وطب طول العمر</div>', unsafe_allow_html=True)
    st.sidebar.markdown("### 🔐 الإشراف البرمجي")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=ACTIVE_API_KEY)
    
    selected_p = st.selectbox("اختر ملف المشترك لإدارته وتعديله فسيولوجياً:", VALID_PATIENT_CODES, index=VALID_PATIENT_CODES.index(st.session_state.active_patient_code))
    if selected_p != st.session_state.active_patient_code:
        st.session_state.active_patient_code = selected_p
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        dr_fbg = st.number_input("سكر صائم:", value=float(p_data['fbg']), key="dr_fbg_in")
        dr_ins = st.number_input("إنسولين صائم:", value=float(p_data['fasting_insulin']), key="dr_ins_in")
        dr_hba1c = st.number_input("التراكمي HbA1c%:", value=float(p_data['hba1c']), key="dr_hba1c_in")
    with col2:
        dr_weight = st.number_input("الوزن (كجم):", value=float(p_data['weight']), key="dr_weight_in")
        dr_waist = st.number_input("محيط الخصر (سم):", value=float(p_data['waist']), key="dr_waist_in")
        dr_anxiety = st.slider("مستوى التوتر والقلق العصبي (0-10):", 0, 10, int(p_data['anxiety_score']), key="dr_anxiety_in")
        
    if st.button("💾 حفظ وتحديث السجل الطبي للمشترك"):
        conn = sqlite3.connect('cellrevive_quantum_system.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE patients SET fbg=?, fasting_insulin=?, hba1c=?, weight=?, waist=?, anxiety_score=? WHERE patient_code=?
        """, (dr_fbg, dr_ins, dr_hba1c, dr_weight, dr_waist, dr_anxiety, st.session_state.active_patient_code))
        conn.commit()
        conn.close()
        st.success("🟢 تم تحديث وتأمين البيانات بنجاح.")
        st.rerun()

# 3️⃣ لوحة الحسابات الحيوية وعرض الأرقام بالألوان الملكية
if st.session_state.role == "patient" or st.session_state.role == "doctor":
    homa_calc = calculate_homa_ir(p_data['fbg'], p_data['fasting_insulin'])
    bio_age = calculate_biological_age(p_data['age'], p_data['hba1c'], homa_calc, p_data['hscrp'], p_data['waist'])
    egfr_calc = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; text-align:center; margin-bottom:15px;">🧬 مجهر الخلايا وعمرك البيولوجي للملف: {st.session_state.active_patient_code}</h3>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div><span style="font-size:14px; opacity:0.9;">العمر البيولوجي</span><br><b class="metric-value-green">{bio_age} سنة</b></div>
                <div><span style="font-size:14px; opacity:0.9;">مقاومة الإنسولين</span><br><b class="metric-value-gold">{homa_calc}</b></div>
                <div><span style="font-size:14px; opacity:0.9;">كفاءة الكلى</span><br><b class="metric-value-green">{egfr_calc}</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # الـ 4 محاور
    tab_meals, tab
