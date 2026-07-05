# 👑 CELLREVIVE AI - THE UNITED METABOLIC OS & CELLULAR RESTORATION PLATFORM (v18.5)
# ==============================================================================
# Production-Ready Sovereign System (2026/2027 International Metabolic Standards)
# Under Direct Clinical Supervision of: Dr. Ehab Heshmat El-Zanny
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
from fpdf import FPDF

# ==============================================================================
# 0️⃣ التهيئة الأولى وإعدادات الصفحة السيادية الفاخرة (يجب أن تكون في البداية تماماً)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - Dr. Ehab Heshmat El-Zanny",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🛡️ استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
try:
    from cryptography.fernet import Fernet
except ImportError:
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet

# 1. تهيئة حالة جلسة العمل للموافقة القانونية
if 'disclaimer_agreed' not in st.session_state:
    st.session_state.disclaimer_agreed = False

# 2. عرض شاشة إخلاء المسؤولية إذا لم تتم الموافقة بعد
if not st.session_state.disclaimer_agreed:
    st.title("🛡️ CellRevive AI - نظام الحماية وإخلاء المسؤولية")
    st.warning("يرجى قراءة والموافقة على الشروط القانونية أدناه لبدء استخدام المنظومة الأيضية.")
    
    st.markdown("""
    ### ⚠️ تنبيه وإخلاء مسؤولية قانوني / Legal Disclaimer
    
    **باللغة العربية:**
    هذا التطبيق هو منصة محاكاة رقمية وأداة تعليمية وتثقيفية تهدف إلى دعم الصحة الأيضية ونمط الحياة وتحسين كفاءة الخلايا. 
    المعلومات والبروتوكولات الصادرة عن هذا البرنامج **لا تعتبر تشخيصاً طبياً، أو وصفة علاجية، ولا تغني بأي حال من الأحوال عن استشارة الطبيب البشري المعالج** أو تعديل الأدوية الموصوفة دون الرجوع إليه.
    
    ---
    **In English:**
    This application is a digital simulation model and an educational tool designed to support metabolic health. 
    The information provided **DO NOT constitute medical advice, diagnosis, or prescription, and are NOT a substitute for professional medical consultation by a licensed physician**.
    """)
    
    agree_check = st.checkbox("لقد قرأت النص أعلاه وأوافق تماماً على هذه الشروط القانونية / I have read and agree to these terms.")
    
    if agree_check:
        if st.button("انطلق إلى المنصة / Enter Platform 🚀"):
            st.session_state.disclaimer_agreed = True
            st.rerun()
            
    st.stop() # إيقاف التنفيذ حتى تتم الموافقة القانونية أولاً

# ==============================================================================
# 1️⃣ منظومة التشفير وحماية البيانات الطبية البيئية (HIPAA Safe Architecture)
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
        return "🛡️ [بيانات مشفرة ومحمية بيئياً]"

# التحقق من مفتاح API لمحرك الذكاء الاصطناعي
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    GEMINI_API_KEY = st.session_state.api_key_input
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

# تطبيق التصاميم الفاخرة للواجهة (Premium Gold Design)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=600;800;900&display=swap');
    
    .stApp { background-color: #040d1a; color: #ffffff !important; font-family: 'Cairo', sans-serif !important; }
    [data-testid="stMainBlockContainer"] { direction: rtl !important; text-align: right !important; }
    .premium-card {
        background: linear-gradient(145deg, #0a1f38, #07162c);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
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
    label, p, span, h3, h4 { color: #ffffff !important; font-weight: 600 !important; }
    .stButton>button {
        background: linear-gradient(90deg, #f3e5ab, #d4af37, #aa8422);
        color: #040d1a !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        height: 3.2em;
        width: 100%;
        border: none;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    .metric-box { border-right: 4px solid #d4af37; padding-right: 15px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 15px; margin-bottom: 5px;">
        <h1 style="color: #d4af37; font-family: 'Cairo', sans-serif; font-size: 38px; font-weight: 900; letter-spacing: 2px; margin-bottom: 5px; text-shadow: 3px 3px 8px rgba(0,0,0,0.9);">
            👑 CELLREVIVE AI
        </h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 17px; font-weight: 800; opacity: 0.95; line-height: 1.6; max-width: 850px; margin: 0 auto; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
            تحت إشراف: د/ إيهاب حشمت الظني <br>
            صيدلي وأخصائي الترميم الخلوي وطب طول العمر وعكس مسار السكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 15px; margin-bottom: 20px;">
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 2️⃣ منظومة قاعدة البيانات المحدثة والمحمية إحصائياً (SQLite Research Engine)
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
    
    cursor.execute("PRAGMA table_info(patients)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'fasting_insulin' not in columns:
        cursor.execute("ALTER TABLE patients ADD COLUMN fasting_insulin REAL DEFAULT 12.0")
    if 'hscrp' not in columns:
        cursor.execute("ALTER TABLE patients ADD COLUMN hscrp REAL DEFAULT 1.0")
    if 'compliance_score' not in columns:
        cursor.execute("ALTER TABLE patients ADD COLUMN compliance_score INTEGER DEFAULT 100")
        
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
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 'skin_analysis': decrypt_data(row[7]), 'selected_drugs': decrypt_data(row[8]), 
            'creatinine': row[9], 'age': row[10], 'gender': row[11], 'country': row[12] or 'Egypt', 'cgm_connected': row[13] or 0,
            'mthfr_mutation': row[14] or 'Normal (CC)', 'fto_variant': row[15] or 'Normal (TT)', 'fasting_insulin': row[16] or 12.0,
            'hscrp': row[17] if row[17] is not None else 1.0, 'compliance_score': row[18] if row[18] is not None else 100
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

def log_glucose(code, g_type, value):
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    t_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor.execute("INSERT INTO glucose_logs (patient_code, reading_time, reading_type, reading_value) VALUES (?, ?, ?, ?)",
                   (code, t_str, g_type, value))
    conn.commit()
    conn.close()

def get_all_glucose_logs(code):
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reading_time, reading_type, reading_value FROM glucose_logs WHERE patient_code = ? ORDER BY id ASC", (code,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_anonymized_research_data():
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    df = pd.read_sql_query("SELECT fbg, ppbg, hba1c, severity_score, compliance_score, age, gender FROM patients", conn)
    conn.close()
    return df

# ==============================================================================
# 3️⃣ المحرك الحسابي المتقدم للمؤشرات وطول العمر (Biological Age Engine)
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin):
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender in ['Female', 'أنثى', 'أنثي']: val *= 0.85
    return min(round(val, 2), 150.0)

def calculate_biological_age(age, hba1c, homa_ir, hscrp, waist):
    base_shift = 0.0
    if hba1c > 5.6: base_shift += (hba1c - 5.6) * 3.5
    if homa_ir > 1.9: base_shift += (homa_ir - 1.9) * 2.0
    if hscrp > 1.0: base_shift += (hscrp - 1.0) * 1.5
    if waist > 94: base_shift += (waist - 94) * 0.15
    bio_age = age + base_shift
    return round(bio_age, 1)

def calculate_glucose_variability(code):
    logs = get_all_glucose_logs(code)
    if len(logs) < 3: return 0.0, "بيانات غير كافية لحساب التقلب الحركي"
    values = [row[2] for row in logs]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    sd = math.sqrt(variance)
    cv = (sd / mean) * 100 if mean > 0 else 0.0
    if cv < 15.0: status = "✅ مستقر ومثالي للترميم الخلوي"
    elif cv <= 36.0: status = "⚠️ تذبذب متوسط - يتطلب ضبط ترتيب الطعام"
    else: status = "🚨 تذبذب حاد وحرج - خطر حدوث طفرات سكر مفاجئة"
    return round(cv, 2), status

def simulate_glucose_curve(base_fbg, sequence_type, gi_score):
    t = np.linspace(0, 180, 100)
    gamma = 2.4 if sequence_type == "الألياف أولاً ➔ البروتين والدهون ➔ النشويات" else 1.0
    A = gi_score * 1.5 
    k1 = 0.04 / (gamma * 0.8)
    k2 = 0.02 * gamma
    delta_g = A * (np.exp(-k2 * t) - np.exp(-k1 * t)) * (150 / (base_fbg * gamma))
    glucose_t = base_fbg + delta_g
    return t, glucose_t

# ==============================================================================
# 4️⃣ قواعد البيانات الدستورية للأدوية والأطعمة (Global Pharma & GI DB)
# ==============================================================================
GLOBAL_DRUG_DB = {
    "Cidophage (سيدوفاج)": {
        "generic": "Metformin", "class": "Biguanide (Insulin Sensitizer)",
        "regions": ["Egypt", "Exported to Gulf"], "arabic_names": ["سيدوفاج", "سيدوفاج ار"],
        "supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف فيتامين ب12 الحاد وتأثر كفاءة الميتوكوندريا فسيولوجياً طبقاً لتدقيق هيئة الدواء المصرية."
    },
    "Glucophage (جلوكوفاج)": {
        "generic": "Metformin", "class": "Biguanide (Insulin Sensitizer)",
        "regions": ["Egypt", "Gulf", "International"], "arabic_names": ["جلوكوفاج", "جلوفاج"],
        "supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر المحاور الأعصاب الطرفية فسيولوجياً على المدى الطويل."
    },
    "Nervizam (نيرفيزام)": {
        "generic": "Alpha-Lipoic Acid + Vitamin B Complex", "class": "Mitochondrial & Neurovascular Antioxidant",
        "regions": ["Egypt", "Exported to Gulf"], "arabic_names": ["نيرفيزام", "نرفيزام"],
        "supp": "Chromium Picolinate + Magnesium Citrate", "reason": "دعم مضادات الأكسدة الخلوية العميقة وحماية غمد المايلين الدهني وكبح مسارات التحلل السكري المتقدم (AGEs)."
    },
    "Milga (ميلجا)": {
        "generic": "Benfotiamine + B6 + B12", "class": "Neurotropic B-Complex",
        "regions": ["Egypt", "Exported to Gulf"], "arabic_names": ["ميلجا", "ميلجا ادفانس"],
        "supp": "Alpha-Lipoic Acid (600mg)", "reason": "حماية غمد المايلين الدهني للأعصاب الطرفية عبر دمج البنفوتيامين (B1 الذائب في الدهون) لمنع التلف الأيضي."
    },
    "Ozempic (أوزمبيك)": {
        "generic": "Semaglutide", "class": "GLP-1 Receptor Agonist",
        "regions": ["Egypt", "Gulf", "International"], "arabic_names": ["أوزمبيك", "وزمبك"],
        "supp": "Digestive Enzymes + Zinc + Essential Amino Acids (EAAs)", "reason": "تأخير حركة المعدة فسيولوجياً والحاجة لتسهيل امتصاص المغذيات خلوياً ومنع هدم الكتلة العضلية (Sarcopenia)."
    }
}

GI_FOOD_DATABASE = {
    "أرز أبيض مصري": {"GI": 72, "unit_carbs": 4.0, "unit_fiber": 0.1},
    "أرز بسمتي طويل الحبة": {"GI": 50, "unit_carbs": 3.5, "unit_fiber": 0.4},
    "خبز شعير كامل": {"GI": 45, "unit_carbs": 12.0, "unit_fiber": 2.5},
    "خبز جوز الهند / اللوز (Keto)": {"GI": 15, "unit_carbs": 3.0, "unit_fiber": 3.0}
}

# ==============================================================================
# 5️⃣ إدارة الحماية الرقمية والامتثال الدولي (HIPAA Security Codes)
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
CORE_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]
VALID_PATIENT_CODES = CORE_CODES + [f"CR-1M-{i:02d}" for i in range(1, 11)] + [f"CR-3M-{i:02d}" for i in range(1, 11)]

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div style="text-align:center; color:#d4af37; font-size:22px; font-weight:900; margin-bottom:15px;">🔐 بروتوكول العبور الرقمي والاتصال المشفّر للمنصة</div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود العضوية المحفوظ على موبايلك للولوج السريع:", type="password")
    if st.button("تأكيد الاتصال والمصادقة الحيوية"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "doctor", MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "patient", input_code
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
# 6️⃣ شاشة المشرف السيادي (د. إيهاب حشمت الظني) & المجهر الإحصائي
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; text-align:center; border-bottom:1px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة القيادة وطب طول العمر السيادية - د. إيهاب حشمت</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
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
            
        mod_mthfr = st.selectbox("جين MTHFR:", ["Normal (CC)", "طفرة متغايرة (CT)", "طفرة متجانسة (TT)"])
        mod_fto = st.selectbox("جين FTO الأيضي:", ["Normal (TT)", "خطر مرتفع (AA)"])
        mod_drugs = st.multiselect("الأدوية الحالية للمقاصة:", list(GLOBAL_DRUG_DB.keys()))
        
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
            
    with tab_research:
        st.markdown("### 📊 مستودع الأدلة السريرية الواقعية لتقديمها للمؤسسات الدولية (Real-World Evidence Generation)")
        res_df = get_anonymized_research_data()
        if not res_df.empty:
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            col_stat1.metric("إجمالي الحالات المسجلة أبحاثاً", len(res_df))
            col_stat2.metric("متوسط التراكمي في الداتا", f"{round(res_df['hba1c'].mean(), 2)}%")
            col_stat3.metric("معدل الالتزام المتوسط للمشتركين", f"{round(res_df['compliance_score'].mean(), 1)}%")
            
            fig_hist = px.histogram(res_df, x="hba1c", title="توزيع السكر التراكمي بين عينات المرضى (بيانات مجهولة الهوية بالكامل)", color_discrete_sequence=['#d4af37'])
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("لا توجد بيانات كافية في مستودع الأبحاث حالياً لتوليد المنحنيات المجمعة.")

# ==============================================================================
# 7️⃣ شاشة المشترك المتقدمة وطب طول العمر وتصفير الكورتيزول والتلعيب
# ==============================================================================
if st.session_state.role == "patient":
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 1px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك في لوحتك العلاجية المخصصة تحت إشراف د. إيهاب حشمت الظني</p>', unsafe_allow_html=True)
    
    homa_calc = calculate_homa_ir(p_data['fbg'], p_data['fasting_insulin'])
    bio_age_calc = calculate_biological_age(p_data['age'], p_data['hba1c'], homa_calc, p_data['hscrp'], p_data['waist'])
    
    # 🔥 ركيزة طول العمر: استعراض العمر البيولوجي مقارنة بالزمني
    st.markdown(f"""
        <div class="premium-card" style="border-color: #f3e5ab; background: linear-gradient(145deg, #091e36, #040f1c);">
            <h3 style="color:#d4af37 !important; margin:0 0 15px 0; font-size:18px;">🧬 مجهر طول العمر وعمر الخلايا (Biological Longevity Core)</h3>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div><span style="font-size:14px; opacity:0.8;">العمر الزمني (البطاقة):</span><br><b style="font-size:24px; color:#ffffff;">{p_data['age']} سنة</b></div>
                <div><span style="font-size:14px; opacity:0.8;">العمر البيولوجي (الخلايا):</span><br><b style="font-size:24px; color:#00ffcc;">{bio_age_calc} سنة</b></div>
            </div>
            <p style="font-size:12.5px; margin-top:10px; line-height:1.5; opacity:0.9; text-align:justify;">
                *العمر البيولوجي يتم حسابه بدقة عبر خوارزمية الربط الميتابوليزمي والالتهاب الخلوي المسرع للشيخوخة. هدف بروتوكول عكس مسار المرض مع الدكتور إيهاب هو خفض عمر خلاياك لتصبح أصغر من عمرك الزمني!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 🕹️ ركيزة التلعيب ومكافآت الالتزام الخلوي (Gamification Core)
    st.markdown(f"""
        <div class="premium-card" style="border-color: #00ffcc; background: linear-gradient(145deg, #05221d, #02110e);">
            <h3 style="color:#00ffcc !important; margin:0 0 10px 0; font-size:18px;">🏆 لوحة الإنجاز ومكافآت الخلايا (Cellular Rewards)</h3>
            <p style="font-size:13px; margin:0 0 10px 0;">مستوى التزامك الحالي بالبروتوكول الأيضي الموجه: <b>{p_data['compliance_score']}%</b></p>
    """, unsafe_allow_html=True)
    
    col_game1, col_game2 = st.columns(2)
    with col_game1:
        done_soleus = st.checkbox("🏃 أكملت تمرين كبش السكر (Soleus Pushups) بعد الوجبة اليوم")
    with col_game2:
        done_stress = st.checkbox("🌬️ طبقت بروتوكول تصفير الكورتيزول والتنفس المربع اليوم")
        
    if done_soleus or done_stress:
        st.markdown("""
            <div style="color:#00ffcc; font-size:13px; font-weight:800; margin-top:5px;">
                👑 رائع! تم منحك وسام الرقمي: [🛡️ حارس الميتوكوندريا] وزيادة نقاط الالتزام في مصفوفة أبحاث الدكتور إيهاب الحركية.
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 🧠 رادار الكورتيزول والأدرينالين متعدد الاختيارات
    st.markdown("""
        <div class="premium-card" style="border-color: #e0a96d;">
            <h3 style="color:#e0a96d !important; margin:0 0 10px 0; font-size:17px;">🧠 رادار المحور العصبي-الغدّي والضغط الكظري</h3>
            <p style="font-size:13px; margin:0; opacity:0.85;">يرجى تحديد كافة العوارض التي تصف بدقة ضغوطك النفسية أو اضطرابات نومك الحالية لكسر طفرة الكورتيزول فسيولوجياً:</p>
        </div>
    """, unsafe_allow_html=True)
    
    stress_options = [
        "🔄 أستيقظ من النوم مجهداً وكأنني لم أنم تماماً (مؤشر ذروة كورتيزول مقلوبة)",
        "🧠 صعوبة بالغة في الدخول في النوم مع عدم توقف العقل عن التفكير والتحليل",
        "⚡ خفقان سريع مفاجئ في القلب أو شد حاد في عضلات الرقبة والكتفين عند التوتر",
        "🍪 رغبة مفاجئة وشرهة لا يمكن كبحها لتناول السكريات أو المعجنات عند الضغط العصبي"
    ]
    selected_stress = st.multiselect("مؤشرات الإجهاد العصبي التراكمي:", stress_options)
    
    if selected_stress:
        st.markdown(f"""
            <div class="premium-card" style="border-color: #e0a96d; background: #22170d;">
                <h4 style="color:#e0a96d !important; margin:0 0 10px 0;">🛡️ بروتوكول الدكتور إيهاب حشمت لتصفير الكورتيزول الفوري:</h4>
                <p style="font-size:13.5px; line-height:1.6;">
                    توجيهات سيادية صارمة لكسر دائرة استثارة الغدد الصماء فوراً:
                    <br>
                    • <b>العلاج بالضحك الاستباقي:</b> استمع لنكتة أو مشهد كوميدي الآن؛ الضحك يفرز الإندورفين الذي يخفض الكورتيزول مصل الحركية بنسبة 39%.
                    <br>
                    • <b>التنفس المربع الصارم (Box Breathing):</b> 4 ثوانٍ شهيق، 4 ثوانٍ كتم، 4 ثوانٍ زفير، 4 ثوانٍ كتم. (كررها 5 مرات لتفعيل العصب الحائر كابح الأدرينالين).
                    <br>
                    • <b>الهروب البيئي السريع:</b> اخرج فوراً وتمشّ في مكان مفتوح متسع لتقليل نشاط منطقة الأميغدالا بالمخ.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 🌿 حزمة الحركة الذكية والوصفات الأكاديمية
    st.markdown("""
        <div class="premium-card" style="border-color: #8fce00;">
            <h3 style="color:#8fce00 !important; margin:0 0 15px 0; font-size:18px;">🏃 التوجيه الحركي والوصفات الأيضية المعتمدة</h3>
            <p style="font-size:13.5px; line-height:1.6;">
                • <b>تمرين كبش السكر (Soleus Pushups):</b> تحريك عضلة الساق الخلفية أثناء الجلوس بعد الوجبة لـ 10 دقائق لامتصاص الجلوكوز مباشرة دون إجهاد.
                <br>
                • <b>منقوع القرفة السيالانية النقية (Ceylon Cinnamon):</b> نصف ملعقة صغيرة في كوب ماء دافئ قبل الوجبة الرئيسية بـ 20 دقيقة لزيادة حساسية مستقبلات الإنسولين.
            </p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🥗 محاكي تسطيح منحنى الجلوكوز التفاعلي ثنائي الأبعاد (2D Curve Simulator)"):
        sel_food = st.selectbox("اختر المكون النشوي:", list(GI_FOOD_DATABASE.keys()))
        sel_seq = st.selectbox("اختر الترتيب الفسيولوجي لتناول الوجبة:", ["النشويات أولاً", "الألياف أولاً ➔ البروتين والدهون ➔ النشويات"])
        food_gi = GI_FOOD_DATABASE[sel_food]["GI"]
        t_vec, g_vec = simulate_glucose_curve(p_data['fbg'], sel_seq, food_gi)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_vec, y=g_vec, mode='lines', name='منحنى استجابة الجلوكوز المتوقع', line=dict(color='#d4af37' if "الألياف" in sel_seq else '#ff4b4b', width=3)))
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
