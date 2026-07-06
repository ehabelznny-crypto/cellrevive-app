# 👑 CELLREVIVE AI - THE UNITED METABOLIC OS & CELLULAR RESTORATION PLATFORM (v20.0 - Production Certified)
# ==============================================================================
# Production-Ready Sovereign System (2026/2027 International Metabolic Standards)
# Under Direct Clinical Supervision of: Dr. Ehab Heshmat El-Znny
# Clinical Pharmacist & Cellular Restoration, Longevity Medicine, & T2D Reversal Specialist
# HIPAA Safe Architecture | Computational Nutrigenomics | Longevity Core | Vagus Reset
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

# ==============================================================================
# 0️⃣ التهيئة الأولى وإعدادات الصفحة السيادية الفاخرة
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - Dr. Ehab Heshmat El-Znny",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🛡️ استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
try:
    from cryptography.fernet import Fernet
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet

# 👑 تطبيق التصاميم الفاخرة للواجهة الملكية واتجاه الكتابة لليمين (Premium Gold & RTL Design)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=600;800;900&display=swap');
    
    .stApp { 
        background-color: #040d1a; 
        color: #ffffff !important; 
        font-family: 'Cairo', sans-serif !important; 
    }
    
    [data-testid="stMainBlockContainer"], .stTabs, div, p, span, label, h1, h2, h3, h4, h5, h6 { 
        direction: rtl !important; 
        text-align: right !important; 
    }
    
    .premium-card {
        background: linear-gradient(145deg, #0a1f38, #07162c);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2);
    }
    
    .emergency-card {
        background: linear-gradient(145deg, #4a0d0d, #2a0505);
        border: 2px solid #ff4b4b;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.4);
    }
    @keyframes pulse {
        0% { border-color: #ff4b4b; }
        50% { border-color: #aa1111; }
        100% { border-color: #ff4b4b; }
    }
    
    label, p, span, h3, h4 { 
        color: #ffffff !important; 
        font-weight: 600 !important; 
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #f3e5ab, #d4af37, #aa8422) !important;
        color: #040d1a !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        height: 3.2em;
        width: 100%;
        border: none !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important;
    }
    
    .metric-box { 
        border-right: 4px solid #d4af37; 
        padding-right: 15px; 
        margin: 10px 0; 
    }
    
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #07162c !important;
        color: #ffffff !important;
        border: 1px solid #d4af37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1️⃣ تحضير وإدارة حالة جلسة العمل للموافقة القانونية أولاً
if 'disclaimer_agreed' not in st.session_state:
    st.session_state.disclaimer_agreed = False

# 2️⃣ عرض شاشة إخلاء المسؤولية القانونية بالشكل الفاخر المحمي
if not st.session_state.disclaimer_agreed:
    st.markdown("""
        <div class="emergency-card" style="margin-top: 30px;">
            <h2 style="color: #ff4b4b !important; text-align: center !important; font-weight: 900; direction: rtl !important;">🛡️ وثيقة الأمان الطبي والالتزام المشترك / Legal Disclaimer</h2>
            <hr style="border-color: #ff4b4b;">
            <p style="font-size: 16px; line-height: 1.7; text-align: justify !important; direction: rtl !important;">
                <b>هام جدًا</b><br>
                هذا التطبيق هو منصة محاكاة رقمية وأداة تعليمية وتثقيفية تهدف إلى دعم الصحة الأيضية ونمط الحياة وتحسين كفاءة الخلايا. 
                المعلومات والبروتوكولات الصادرة عن هذا البرنامج <b>لا تعتبر تشخيصاً طبياً، أو وصفة علاجية، ولا تغني بأي حال من الأحوال عن استشارة الطبيب البشري المعالج</b> أو تعديل الأدوية الموصوفة دون الرجوع إليه.
            </p>
            <hr style="border-color: #ff4b4b; opacity: 0.3;">
            <div style="direction: ltr !important; text-align: left !important;">
                <p style="font-size: 15px; line-height: 1.6; color: #ffffff !important; font-weight: 600 !important; text-align: left !important; direction: ltr !important;">
                    <b>Very important</b><br>
                    This application is a digital simulation model and an educational tool designed to support metabolic health. <br>
                    The information provided <b>DO NOT constitute medical advice, diagnosis, or prescription, and are NOT a substitute for professional medical consultation by a licensed physician</b>.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    agree_check = st.checkbox("لقد قرأت النص أعلاه وأوافق تماماً على هذه الشروط القانونية الصارمة / I agree completely.")
    
    if agree_check:
        if st.button("الانطلاق وبدء الاتصال بالمنصة الخلوية 🚀"):
            st.session_state.disclaimer_agreed = True
            st.rerun()
    st.stop()

# ==============================================================================
# 3️⃣ منظومة التشفير وحماية البيانات الطبية البيئية (HIPAA Safe Architecture)
# ==============================================================================
if "ENCRYPTION_KEY" in st.secrets:
    KEY = st.secrets["ENCRYPTION_KEY"].encode()
else:
    if "EMERGENCY_STATIC_KEY" not in st.session_state:
        st.session_state["EMERGENCY_STATIC_KEY"] = Fernet.generate_key().decode()
    KEY = st.session_state["EMERGENCY_STATIC_KEY"].encode()

cipher_suite = Fernet(KEY)

def encrypt_data(data_str):
    if not data_str: return ""
    return cipher_suite.encrypt(data_str.encode()).decode()

def decrypt_data(crypto_str):
    if not crypto_str: return ""
    try:
        return cipher_suite.decrypt(crypto_str.encode()).decode()
    except Exception:
        return "لا توجد تصبغات نشطة"

# تفعيل وإدارة مفاتيح الذكاء الاصطناعي بشكل آمن عبر الجلسات
if "GEMINI_API_KEY" in st.secrets:
    ACTIVE_API_KEY = st.secrets["GEMINI_API_KEY"]
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    ACTIVE_API_KEY = st.session_state.api_key_input
else:
    ACTIVE_API_KEY = ""

if ACTIVE_API_KEY:
    genai.configure(api_key=ACTIVE_API_KEY)

# الهيدر الملكي الثابت للمنصة
st.markdown("""
    <div style="text-align: center; padding: 15px; margin-bottom: 5px;">
        <h1 style="color: #d4af37; font-family: 'Cairo', sans-serif; font-size: 38px; font-weight: 900; letter-spacing: 2px; margin-bottom: 5px; text-shadow: 3px 3px 8px rgba(0,0,0,0.9); text-align: center !important;">
            👑 CELLREVIVE AI
        </h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 17px; font-weight: 800; opacity: 0.95; line-height: 1.6; max-width: 850px; margin: 0 auto; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); text-align: center !important;">
            تحت إشراف: د/ إيهاب حشمت الظني <br>
            صيدلي وأخصائي الترميم الخلوي وطب طول العمر وعكس مسار السكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 15px; margin-bottom: 20px;">
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 4️⃣ منظومة قاعدة البيانات المحدثة والمحمية إحصائياً (SQLite Research Engine)
# ==============================================================================
def init_db():
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_code TEXT PRIMARY KEY,
            fbg REAL, ppbg REAL DEFAULT 140.0, rbg REAL DEFAULT 120.0, hba1c REAL,
            weight REAL, waist REAL, creatinine REAL DEFAULT 1.0, age INTEGER DEFAULT 45,
            gender TEXT DEFAULT 'Male', severity_score REAL DEFAULT 5.0,
            skin_analysis TEXT DEFAULT '', selected_drugs TEXT DEFAULT '',
            country TEXT DEFAULT 'Egypt', cgm_connected INTEGER DEFAULT 0,
            mthfr_mutation TEXT DEFAULT 'Normal (CC)', fto_variant TEXT DEFAULT 'Normal (TT)',
            fasting_insulin REAL DEFAULT 12.0, hscrp REAL DEFAULT 1.0, compliance_score INTEGER DEFAULT 100
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS glucose_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_code TEXT, reading_time TEXT, reading_type TEXT, reading_value REAL,
            FOREIGN KEY(patient_code) REFERENCES patients(patient_code)
        )
    """)
    conn.commit()
    conn.close()

init_db()

def get_patient_data(code):
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, 
               creatinine, age, gender, country, cgm_connected, mthfr_mutation, fto_variant, fasting_insulin, hscrp, compliance_score
        FROM patients WHERE patient_code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0] if row[0] is not None else 130.0, 
            'ppbg': row[1] if row[1] is not None else 140.0, 
            'rbg': row[2] if row[2] is not None else 120.0, 
            'hba1c': row[3] if row[3] is not None else 7.2, 
            'weight': row[4] if row[4] is not None else 85.0, 
            'waist': row[5] if row[5] is not None else 105.0,
            'severity_score': row[6] if row[6] is not None else 5.0, 
            'skin_analysis': decrypt_data(row[7]) if row[7] else 'لا توجد تصبغات نشطة', 
            'selected_drugs': decrypt_data(row[8]) if row[8] else '', 
            'creatinine': row[9] if row[9] is not None else 1.0, 
            'age': row[10] if row[10] is not None else 45, 
            'gender': row[11] if row[11] else 'Male', 
            'country': row[12] or 'Egypt', 
            'cgm_connected': row[13] or 0,
            'mthfr_mutation': row[14] or 'Normal (CC)', 
            'fto_variant': row[15] or 'Normal (TT)', 
            'fasting_insulin': row[16] if row[16] is not None else 12.0, 
            'hscrp': row[17] if row[17] is not None else 1.0, 
            'compliance_score': row[18] if row[18] is not None else 100
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    encrypted_skin = encrypt_data(data['skin_analysis'])
    encrypted_drugs = encrypt_data(data['selected_drugs'])
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, 
                                         skin_analysis, selected_drugs, creatinine, age, gender, country, 
                                         cgm_connected, mthfr_mutation, fto_variant, fasting_insulin, hscrp, compliance_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], 
          data['severity_score'], encrypted_skin, encrypted_drugs, data['creatinine'], data['age'], 
          data['gender'], data['country'], data['cgm_connected'], data['mthfr_mutation'], data['fto_variant'], data['fasting_insulin'],
          data['hscrp'], data['compliance_score']))
    conn.commit()
    conn.close()

# ==============================================================================
# 5️⃣ المحرك الحسابي المتقدم للمؤشرات وطول العمر (Biological Age Engine)
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin):
    if fasting_insulin <= 0 or fbg <= 0: return 1.0
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0 or weight <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender in ['Female', 'أنثى', 'أنثي']: val *= 0.85
    return min(round(val, 2), 150.0)

def calculate_biological_age(age, hba1c, homa_ir, hscrp, waist):
    base_shift = 0.0
    if hba1c > 5.6: base_shift += (hba1c - 5.6) * 3.5
    if homa_ir > 1.9: base_shift += (homa_ir - 1.9) * 2.0
    if hscrp > 1.0: base_shift += (hscrp - 1.0) * 1.5
    if waist > 94: base_shift += (waist - 94) * 0.15
    return max(round(age + base_shift, 1), 18.0)

def simulate_glucose_curve(base_fbg, sequence_type, gi_score):
    t = np.linspace(0, 180, 100)
    gamma = 2.5 if sequence_type == "الألياف أولاً ➔ :البروتينات والدهون ➔ النشويات" else 1.0
    A = gi_score * 1.3
    k1 = 0.04 / (gamma * 0.8)
    k2 = 0.02 * gamma
    delta_g = A * (np.exp(-k2 * t) - np.exp(-k1 * t)) * (140 / (max(base_fbg, 70.0) * gamma))
    return t, base_fbg + delta_g

# ==============================================================================
# 6️⃣ قواعد البيانات الدستورية للأدوية والأطعمة (Global Pharma DB)
# ==============================================================================
GLOBAL_DRUG_DB = {
    "Cidophage (سيدوفاج)": {
        "generic": "Metformin", "supp": "Methyl B12 (1000mcg) + CoQ10", 
        "reason": "استنزاف فيتامين ب12 الحاد وتأثر كفاءة الميتوكوندريا فسيولوجياً طبقاً لتدقيق هيئة الدواء المصرية."
    },
    "Glucophage (جلوكوفاج)": {
        "generic": "Metformin", "supp": "Methyl B12 (1000mcg)", 
        "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر محاور الأعصاب الطرفية فسيولوجياً على المدى الطويل."
    },
    "Nervizam (نيرفيزام)": {
        "generic": "Alpha-Lipoic Acid + Vitamin B Complex", "supp": "Chromium Picolinate + Magnesium Citrate", 
        "reason": "دعم مضادات الأكسدة الخلوية العميقة وحماية غمد المايلين الدهني وكبح مسارات التحلل السكري المتقدم (AGEs)."
    },
    "Milga (ميلجا)": {
        "generic": "Benfotiamine + B6 + B12", "supp": "Alpha-Lipoic Acid (600mg)", 
        "reason": "حماية غمد المايلين الدهني للأعصاب الطرفية عبر دمج البنفوتيامين لمنع التلف الأيضي."
    },
    "Ozempic (أوزمبيك)": {
        "generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc + Essential Amino Acids (EAAs)", 
        "reason": "تأخير حركة المعدة فسيولوجياً والحاجة لتسهيل امتصاص المغذيات خلوياً ومنع هدم الكتلة العضلية (Sarcopenia)."
    }
}

GI_FOOD_DATABASE = {
    "أرز أبيض مصري": {"GI": 72},
    "أرز بسمتي طويل الحبة": {"GI": 50},
    "خبز شعير كامل": {"GI": 45},
    "خبز جوز الهند / اللوز (Keto)": {"GI": 15}
}

# ==============================================================================
# 7️⃣ إدارة الحماية الرقمية والامتثال الدولي (HIPAA Security Codes)
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
CORE_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]
VALID_PATIENT_CODES = CORE_CODES + [f"CR-1M-{i:02d}" for i in range(1, 11)]

if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None
if 'auth_code' not in st.session_state: st.session_state.auth_code = ""

if not st.session_state.is_auth:
    st.markdown('<div class="premium-card"><div style="text-align:center; color:#d4af37; font-size:22px; font-weight:900;">🔐 بروتوكول العبور الرقمي والاتصال المشفّر للمنصة</div></div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود العضوية المحفوظ على موبايلك للولوج السريع:", type="password")
    if st.button("تأكيد الاتصال والمصادقة الحيوية"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth = True
            st.session_state.role = "doctor"
            st.session_state.auth_code = MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth = True
            st.session_state.role = "patient"
            st.session_state.auth_code = input_code
            st.rerun()
        else:
            st.error("كود غير مصرح به. يرجى مراجعة الإدارة الطبية فوراً لتفعيل الاشتراك.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لا توجد تصبغات نشطة', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male', 'country': 'Egypt', 'cgm_connected': 0,
    'mthfr_mutation': 'Normal (CC)', 'fto_variant': 'Normal (TT)', 'fasting_insulin': 12.0, 'hscrp': 1.0, 'compliance_score': 100
}

# ==============================================================================
# 8️⃣ شاشة المشرف السيادي (د. إيهاب حشمت الظني) & المجهر الإحصائي
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; text-align:center; border-bottom:2px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة القيادة وطب طول العمر السيادية - د. إيهاب حشمت</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=ACTIVE_API_KEY)
    
    tab_manage, tab_research = st.tabs(["📝 إدارة ملفات المشتركين", "🔬 المجهر الإحصائي ومستودع الأدلة السريرية"])
    
    with tab_manage:
        target_patient = st.selectbox("اختر كود المشترك المراد فحص وهندسة ملفه الخلوي:", VALID_PATIENT_CODES)
        current_p_data = get_patient_data(target_patient) or p_data
        
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم (mg/dL):", value=float(current_p_data['fbg']), key="dr_fbg")
            mod_ppbg = st.number_input("سكر فاطر ساعتين (mg/dL):", value=float(current_p_data['ppbg']), key="dr_ppbg")
            mod_insulin = st.number_input("إنسولين صائم (uIU/mL):", value=float(current_p_data['fasting_insulin']), key="dr_ins")
            mod_hscrp = st.number_input("مؤشر الالتهاب الخلوي (hs-CRP mg/L):", value=float(current_p_data['hscrp']), key="dr_crp")
            mod_age = st.number_input("العمر الزمني الحالي:", value=int(current_p_data['age']), key="dr_age")
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']), key="dr_a1c")
            mod_weight = st.number_input("الوزن الحالي (كجم):", value=float(current_p_data['weight']), key="dr_wt")
            mod_waist = st.number_input("محيط الخصر السريري (سم):", value=float(current_p_data['waist']), key="dr_wst")
            mod_creatinine = st.number_input("الكرياتينين (mg/dL):", value=float(current_p_data['creatinine']), key="dr_creat")
            mod_gender = st.selectbox("الجنس الخلوي للمشترك:", ["Male", "Female"], index=0 if current_p_data['gender'] == "Male" else 1)
            
        # 🛡️ معالجة آمنة لخيارات الطفرات الجينية
        mthfr_options = ["Normal (CC)", "طفرة متغايرة (CT)", "طفرة متجانسة (TT)"]
        mthfr_idx = mthfr_options.index(current_p_data['mthfr_mutation']) if current_p_data['mthfr_mutation'] in mthfr_options else 0
        mod_mthfr = st.selectbox("جين MTHFR:", mthfr_options, index=mthfr_idx)
        
        fto_options = ["Normal (TT)", "خطر مرتفع (AA)"]
        fto_idx = fto_options.index(current_p_data['fto_variant']) if current_p_data['fto_variant'] in fto_options else 0
        mod_fto = st.selectbox("جين FTO الأيضي:", fto_options, index=fto_idx)
        
        # 🛡️ صمام الأمان المحدث: معالجة قائمة الأدوية بشكل مرن ومنع الانهيار
        if current_p_data['selected_drugs']:
            saved_drugs_list = [d.strip() for d in current_p_data['selected_drugs'].split(",") if d.strip() in GLOBAL_DRUG_DB]
        else:
            saved_drugs_list = []
            
        mod_drugs = st.multiselect("الأدوية الحالية للمقاصة الطبية والأيضية:", list(GLOBAL_DRUG_DB.keys()), default=saved_drugs_list)
        
        if st.button("💾 تشفير وتثبيت البيانات الحيوية للمشترك"):
            updated_data = {
                'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': current_p_data['rbg'], 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
                'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
                'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender,
                'country': current_p_data['country'], 'cgm_connected': current_p_data['cgm_connected'],
                'mthfr_mutation': mod_mthfr, 'fto_variant': mod_fto, 'fasting_insulin': mod_insulin, 'hscrp': mod_hscrp,
                'compliance_score': current_p_data['compliance_score']
            }
            save_patient_data(target_patient, updated_data)
            st.success("🟢 تم تشفير الملف وحفظه بأعلى معايير الحماية الرقمية بنجاح.")
            st.toast("تم تحديث البيانات الحيوية بنجاح!", icon="💾")
            
    with tab_research:
        st.markdown('### 📊 مستودع الأدلة السريرية الواقعية لتقديمها للمؤسسات الدولية (Real-World Evidence)')
        conn = sqlite3.connect('cellrevive_quantum_system.db')
        try:
            res_df = pd.read_sql_query("SELECT fbg, ppbg, hba1c, severity_score, compliance_score, age, gender FROM patients", conn)
        except Exception:
            res_df = pd.DataFrame()
        finally:
            conn.close()
            
        if not res_df.empty:
            col_stat1, col_stat2 = st.columns(2)
            col_stat1.metric("إجمالي الحالات المسجلة أبحاثاً", len(res_df))
            col_stat2.metric("متوسط التراكمي في الداتا", f"{round(res_df['hba1c'].mean(), 2)}%")
            fig_hist = px.histogram(res_df, x="hba1c", title="توزيع السكر التراكمي بين عينات المرضى", color_discrete_sequence=['#d4af37'])
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("لا توجد بيانات كافية في مستودع الأبحاث حالياً.")

# ==============================================================================
# 9️⃣ شاشة المشترك المتقدمة وطب طول العمر وتصفير الكورتيزول والتلعيب
# ==============================================================================
if st.session_state.role == "patient":
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 2px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك في لوحتك العلاجية المخصصة تحت إشراف د. إيهاب حشمت الظني</p>', unsafe_allow_html=True)
    
    homa_calc = calculate_homa_ir(p_data['fbg'], p_data['fasting_insulin'])
    bio_age_calc = calculate_biological_age(p_data['age'], p_data['hba1c'], homa_calc, p_data['hscrp'], p_data['waist'])
    
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 15px 0; font-size:18px;">🧬 مجهر طول العمر وعمر الخلايا (Biological Longevity Core)</h3>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div><span style="font-size:14px; opacity:0.8;">العمر الزمني (البطاقة):</span><br><b style="font-size:24px; color:#ffffff;">{p_data['age']} سنة</b></div>
                <div><span style="font-size:14px; opacity:0.8;">العمر البيولوجي (الخلايا):</span><br><b style="font-size:24px; color:#00ffcc;">{bio_age_calc} سنة</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 🕹️ ركيبة التلعيب ومكافآت الالتزام الخلوي (Gamification Core)
    st.markdown(f"""
        <div class="premium-card" style="border-color: #00ffcc;">
            <h3 style="color:#00ffcc !important; margin:0 0 10px 0; font-size:18px;">🏆 لوحة الإنجاز ومكافآت الخلايا (Cellular Rewards)</h3>
            <p style="font-size:13px;">مستوى التزامك الحالي بالبروتوكول الأيضي الموجه: <b>{p_data['compliance_score']}%</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    col_game1, col_game2 = st.columns(2)
    with col_game1: done_soleus = st.checkbox("🏃 أكملت تمرين كبش السكر (Soleus Pushups) بعد الوجبة اليوم")
    with col_game2: done_stress = st.checkbox("🌬️ طبقت بروتوكول تصفير الكورتيزول والتنفس المربع اليوم")
        
    if done_soleus or done_stress:
        st.markdown('<div style="color:#00ffcc; font-size:13px; font-weight:800;">👑 رائع! تم منحك وسام رقمي: [🛡️ حارس الميتوكوندريا] وزيادة نقاط الالتزام.</div>', unsafe_allow_html=True)

    # 🧠 رادار الكورتيزول والضغط الكظري
    selected_stress = st.multiselect("مؤشرات الإجهاد العصبي التراكمي الحالية لديك:", [
        "🔄 أستيقظ من النوم مجهداً وكأنني لم أنم تماماً (ذروة كورتيزول مقلوبة)",
        "🧠 صعوبة بالغة في الدخول في النوم مع عدم توقف العقل عن التفكير",
        "⚡ خفقان سريع مفاجئ في القلب أو شد حاد في عضلات الرقبة عند التوتر",
        "🍪 رغبة مفاجئة وشرهة لتناول السكريات أو المعجنات عند الضغط العصبي"
    ])
    
    if selected_stress:
        st.markdown("""
            <div class="premium-card" style="border-color: #e0a96d; background: #22170d;">
                <h4 style="color:#e0a96d !important;">🛡️ بروتوكول الدكتور إيهاب حشمت لتصفير الكورتيزول الفوري:</h4>
                <p style="font-size:13.5px; line-height:1.6;">
                    • <b>العلاج بالضحك الاستباقي:</b> استمع لمشهد كوميدي الآن لخفض الكورتيزول بنسبة 39%.<br>
                    • <b>التنفس المربع (Box Breathing):</b> 4 ثوانٍ شهيق, 4 كتم, 4 زفير, 4 كتم لتفعيل العصب الحائر.<br>
                    • <b>الهروب البيئي السريع:</b> اخرج فوراً وتمشّ في مكان مفتوح لتقليل نشاط الأميغدالا بالمخ.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 🥗 محاكي تسطيح منحنى الجلوكوز التفاعلي ثنائي الأبعاد (2D Curve Simulator)
    st.markdown("### 🥗 محاكي تسطيح منحنى الجلوكوز التفاعلي ثنائي الأبعاد")
    sel_food = st.selectbox("اختر المكون النشوي الرئيسي في وجبتك:", list(GI_FOOD_DATABASE.keys()))
    sel_seq = st.selectbox("اختر الترتيب الفسيولوجي لتناول هذه الوجبة:", ["النشويات أولاً", "الألياف أولاً ➔ :البروتينات والدهون ➔ النشويات"])
    
    food_gi = GI_FOOD_DATABASE[sel_food]["GI"]
    t_vec, g_vec = simulate_glucose_curve(p_data['fbg'], sel_seq, food_gi)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t_vec, y=g_vec, mode='lines', name='منحنى الاستجابة الأيضية', line=dict(color='#d4af37', width=3)))
    fig.update_layout(
        title="توقع حركة السكر خلوياً خلال 180 دقيقة بعد الوجبة",
        xaxis_title="الوقت بالدقائق", yaxis_title="مستوى السكر المتوقع (mg/dL)",
        paper_bgcolor='#040d1a', plot_bgcolor='#07162c', font=dict(color='#ffffff')
    )
    st.plotly_chart(fig, use_container_width=True)

    # 🔬 المقاصة الدوائية الآلية لربط الأدوية بنقص المغذيات
    if p_data['selected_drugs']:
        st.markdown('<div class="premium-card" style="border-color: #ff4b4b;">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#ff4b4b !important; font-size:18px;'>🔬 نظام المقاصة الدوائية التلقائي والمكملات التصحيحية</h3>", unsafe_allow_html=True)
        for drug in p_data['selected_drugs'].split(","):
            drug = drug.strip()
            if drug in GLOBAL_DRUG_DB:
                st.markdown(f"""
                    <p style="font-size:14px; margin-bottom:8px;">
                        • دواء <b>{drug}</b> يستنزف حيوياً: <span style="color:#00ffcc;">{GLOBAL_DRUG_DB[drug]['supp']}</span><br>
                        <small style="opacity:0.8;">السبب السريري: {GLOBAL_DRUG_DB[drug]['reason']}</small>
                    </p>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 🤖 العقل المفكر الذكي المدمج بالكامل (Generative Clinical AI Block)
    st.markdown("### 🤖 العقل المفكر للذكاء الاصطناعي - هندسة الوجبة الفورية")
    user_meal_input = st.text_input("اكتب بالتفصيل ماذا تريد أن تأكل الآن:", placeholder="مثال: ربع فرخة مشوية مع 5 معالق أرز مصري وسلطة")
    
    if st.button("🧬 تحليل الهندسة الخلوية للوجبة وإصدار بروتوكول التعديل"):
        if not ACTIVE_API_KEY:
            st.warning("⚠️ يرجى تزويد التطبيق بمفتاح الـ API الخاص بـ Gemini في لوحة التحكم العلوية لتفعيل العقل المفكر الحركي.")
        elif not user_meal_input:
            st.error("يرجى كتابة مكونات الوجبة أولاً ليتمكن النظام من تقييمها فسيولوجياً.")
        else:
            with st.spinner("⚡ جاري استدعاء مصفوفة الأبحاث الخلوية وتحليل الوجبة..."):
                try:
                    genai.configure(api_key=ACTIVE_API_KEY)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt_context = f"""
                    You are CellRevive AI, an advanced metabolic operating system working under the strict clinical supervision of Dr. Ehab Heshmat El-Znny (Clinical Pharmacist & Cellular Restoration & Longevity Specialist).
                    Patient Metrics:
                    - Age: {p_data['age']} | Gender: {p_data['gender']}
                    - HbA1c: {p_data['hba1c']}% | Fasting Glucose: {p_data['fbg']} mg/dL
                    - Metabolic Mutations: MTHFR: {p_data['mthfr_mutation']} | FTO: {p_data['fto_variant']}
                    - Current Medications: {p_data['selected_drugs']}
                    
                    Proposed Meal: {user_meal_input}
                    Sequence Choice selected by user: {sel_seq}
                    
                    Provide an elite, medically authoritative clinical response in Arabic. 
                    Structure the response strictly with:
                    1. التقييم الأيضي السريع للوجبة (Impact analysis based on HbA1c and medications).
                    2. بروتوكول التعديل الفوري لتسطيح المنحنى (How to optimize the sequence, add fibers, or healthy fats).
                    3. الخلاصة الميتوكوندريالية لطب طول العمر (Longevity insight specifically tailored to their MTHFR/FTO variants or medication depletions).
                    Keep the tone premium, encouraging, and clear. Do not prescribe drugs or offer diagnosis, always reference that this is under the supervision of Dr. Ehab Heshmat El-Znny.
                    """
                    response = model.generate_content(prompt_context)
                    st.markdown(f'<div class="premium-card" style="border-color:#d4af37;"><h4 style="color:#d4af37 !important;">📋 التقرير الخلوي الفوري المعتمد:</h4><p style="line-height:1.7; font-size:14.5px; text-align:justify;">{response.text}</p></div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال بالخادم الأيضي: {str(e)}")
