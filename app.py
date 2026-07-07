# 👑 CELLREVIVE AI - THE UNITED METABOLIC OS & CELLULAR RESTORATION PLATFORM (v20.3 - Premium Complete)
# ==============================================================================
# Production-Ready Sovereign System (2026 International Metabolic Standards)
# Under Direct Clinical Supervision of: Dr. Ehab Heshmat El-Znny
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

# 0️⃣ التهيئة الأولى وإعدادات الصفحة السيادية الفاخرة
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

# تطبيق التصاميم الفاخرة للواجهة الملكية واتجاه الكتابة لليمين
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=600;800;900&display=swap');
    .stApp { background-color: #040d1a; color: #ffffff !important; font-family: 'Cairo', sans-serif !important; }
    [data-testid="stMainBlockContainer"], .stTabs, div, p, span, label, h1, h2, h3, h4, h5, h6 { direction: rtl !important; text-align: right !important; }
    .premium-card { background: linear-gradient(145deg, #0a1f38, #07162c); border: 2px solid #d4af37; border-radius: 15px; padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2); }
    .emergency-card { background: linear-gradient(145deg, #4a0d0d, #2a0505); border: 2px solid #ff4b4b; border-radius: 15px; padding: 25px; margin-bottom: 20px; animation: pulse 2s infinite; box-shadow: 0 0 20px rgba(255, 75, 75, 0.4); }
    @keyframes pulse { 0% { border-color: #ff4b4b; } 50% { border-color: #aa1111; } 100% { border-color: #ff4b4b; } }
    label, p, span, h3, h4 { color: #ffffff !important; font-weight: 600 !important; }
    .stButton>button { background: linear-gradient(90deg, #f3e5ab, #d4af37, #aa8422) !important; color: #040d1a !important; border-radius: 12px !important; font-weight: 900 !important; font-size: 16px !important; height: 3.2em; width: 100%; border: none !important; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important; transition: all 0.3s ease; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(212, 175, 55, 0.6) !important; }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div { background-color: #07162c !important; color: #ffffff !important; border: 1px solid #d4af37 !important; }
    </style>
""", unsafe_allow_html=True)

if 'disclaimer_agreed' not in st.session_state:
    st.session_state.disclaimer_agreed = False

if not st.session_state.disclaimer_agreed:
    st.markdown("""
        <div class="emergency-card" style="margin-top: 30px;">
            <h2 style="color: #ff4b4b !important; text-align: center !important; font-weight: 900; direction: rtl !important;">🛡️ وثيقة الأمان الطبي والالتزام المشترك / Legal Disclaimer</h2>
            <p style="font-size: 16px; line-height: 1.7; text-align: justify !important; direction: rtl !important;">
                <b>هام جدًا</b><br>
                هذا التطبيق هو منصة محاكاة رقمية وأداة تعليمية وتثقيفية تهدف إلى دعم الصحة الأيضية ونمط الحياة وتحسين كفاءة الخلايا وتحت الإشراف المباشر للصيدلي المختص.
            </p>
        </div>
    """, unsafe_allow_html=True)
    agree_check = st.checkbox("لقد قرأت النص أعلاه وأوافق تماماً على هذه الشروط القانونية الصارمة / I agree completely.")
    if agree_check:
        if st.button("الانطلاق وبدء الاتصال بالمنصة الخلوية 🚀"):
            st.session_state.disclaimer_agreed = True
            st.rerun()
    st.stop()

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
    try: return cipher_suite.decrypt(crypto_str.encode()).decode()
    except Exception: return "لا توجد تصبغات نشطة"

if "GEMINI_API_KEY" in st.secrets: ACTIVE_API_KEY = st.secrets["GEMINI_API_KEY"]
elif "api_key_input" in st.session_state and st.session_state.api_key_input: ACTIVE_API_KEY = st.session_state.api_key_input
else: ACTIVE_API_KEY = ""

if ACTIVE_API_KEY: genai.configure(api_key=ACTIVE_API_KEY)

st.markdown("""
    <div style="text-align: center; padding: 15px; margin-bottom: 5px;">
        <h1 style="color: #d4af37; font-family: 'Cairo', sans-serif; font-size: 38px; font-weight: 900; text-align: center !important;">👑 CELLREVIVE AI</h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 17px; font-weight: 800; text-align: center !important;">
            تحت إشراف: د/ إيهاب حشمت الظني <br>
            صيدلي وأخصائي الترميم الخلوي وطب طول العمر وعكس مسار السكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 15px; margin-bottom: 20px;">
    </div>
""", unsafe_allow_html=True)

# 4️⃣ منظومة قاعدة البيانات وزراعة البيانات التجريبية تلقائياً لمنع المستطيلات الفارغة
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
    
    cursor.execute("SELECT COUNT(*) FROM patients")
    if cursor.fetchone()[0] == 0:
        enc_drug1 = cipher_suite.encrypt("Ozempic (أوزمبيك)".encode()).decode()
        enc_drug2 = cipher_suite.encrypt("Cidophage (سيدوفاج)".encode()).decode()
        cursor.execute("INSERT INTO patients (patient_code, fbg, ppbg, hba1c, weight, waist, age, gender, selected_drugs, mthfr_mutation, fto_variant) VALUES ('CR-PATIENT-77', 125, 155, 6.8, 82, 96, 52, 'Male', ?, 'طفرة متغايرة (CT)', 'Normal (TT)')", (enc_drug1,))
        cursor.execute("INSERT INTO patients (patient_code, fbg, ppbg, hba1c, weight, waist, age, gender, selected_drugs, mthfr_mutation, fto_variant) VALUES ('CR-PATIENT-99', 145, 190, 8.1, 95, 110, 47, 'Female', ?, 'Normal (CC)', 'خطر مرتفع (AA)')", (enc_drug2,))
        cursor.execute("INSERT INTO patients (patient_code, fbg, ppbg, hba1c, weight, waist, age, gender, selected_drugs) VALUES ('CR-SOHAG-2026', 110, 138, 5.9, 74, 88, 39, 'Male', '')")
        
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
            'fbg': row[0] if row[0] is not None else 130.0, 'ppbg': row[1] if row[1] is not None else 140.0, 
            'rbg': row[2] if row[2] is not None else 120.0, 'hba1c': row[3] if row[3] is not None else 7.2, 
            'weight': row[4] if row[4] is not None else 85.0, 'waist': row[5] if row[5] is not None else 105.0,
            'severity_score': row[6] if row[6] is not None else 5.0, 'skin_analysis': decrypt_data(row[7]) if row[7] else 'لا توجد تصبغات نشطة', 
            'selected_drugs': decrypt_data(row[8]) if row[8] else '', 'creatinine': row[9] if row[9] is not None else 1.0, 
            'age': row[10] if row[10] is not None else 45, 'gender': row[11] if row[11] else 'Male', 
            'country': row[12] or 'Egypt', 'cgm_connected': row[13] or 0,
            'mthfr_mutation': row[14] or 'Normal (CC)', 'fto_variant': row[15] or 'Normal (TT)', 
            'fasting_insulin': row[16] if row[16] is not None else 12.0, 'hscrp': row[17] if row[17] is not None else 1.0, 'compliance_score': row[18] if row[18] is not None else 100
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

def calculate_homa_ir(fbg, fasting_insulin):
    if fasting_insulin <= 0 or fbg <= 0: return 1.0
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0 or weight <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if str(gender).strip().lower() in ['female', 'أنثى', 'أنثي']: val *= 0.85
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
    gamma = 2.5 if "الألياف" in str(sequence_type) else 1.0
    A = gi_score * 1.3
    k1 = 0.04 / (gamma * 0.8)
    k2 = 0.02 * gamma
    delta_g = A * (np.exp(-k2 * t) - np.exp(-k1 * t)) * (140 / (max(base_fbg, 70.0) * gamma))
    return t, base_fbg + delta_g

GLOBAL_DRUG_DB = {
    "Cidophage (سيدوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف فيتامين ب12 الحاد وتأثر كفاءة الميتوكوندريا فسيولوجياً."},
    "Glucophage (جلوكوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر محاور الأعصاب الطرفية."},
    "Nervizam (نيرفيزام)": {"generic": "Alpha-Lipoic Acid + Vitamin B Complex", "supp": "Chromium Picolinate + Magnesium Citrate", "reason": "دعم مضادات الأكسدة الخلوية العميقة وكبح مسارات التحلل السكري."},
    "Milga (ميلجا)": {"generic": "Benfotiamine + B6 + B12", "supp": "Alpha-Lipoic Acid (600mg)", "reason": "حماية غمد المايلين الدهني للأعصاب الطرفية."},
    "Ozempic (أوزمبيك)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc + EAAs", "reason": "تأخير حركة المعدة فسيولوجياً والحاجة لتسهيل امتصاص المغذيات خلوياً."}
}

# 🌾 تم إدراج العيش البلدي المصري رسمياً بالمعامل الجلايسيمي الدقيق الخاص به
GI_FOOD_DATABASE = {
    "عيش بلدي / عيش مصري (ردة)": {"GI": 55},
    "أرز أبيض مصري": {"GI": 72}, 
    "أرز بسمتي طويل الحبة": {"GI": 50}, 
    "خبز شعير كامل": {"GI": 45}, 
    "خبز جوز الهند / اللوز (Keto)": {"GI": 15}
}

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

# 8️⃣ شاشة المشرف السيادي (د. إيهاب حشمت الظني) & المجهر الإحصائي
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
            
        mthfr_options = ["Normal (CC)", "طفرة متغايرة (CT)", "طفرة متجانسة (TT)"]
        mthfr_idx = mthfr_options.index(current_p_data['mthfr_mutation']) if current_p_data['mthfr_mutation'] in mthfr_options else 0
        mod_mthfr = st.selectbox("جين MTHFR:", mthfr_options, index=mthfr_idx)
        
        fto_options = ["Normal (TT)", "خطر مرتفع (AA)"]
        fto_idx = fto_options.index(current_p_data['fto_variant']) if current_p_data['fto_variant'] in fto_options else 0
        mod_fto = st.selectbox("جين FTO الأيضي:", fto_options, index=fto_idx)
        
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
            st.success("🟢 تم تشفير الملف وحفظه بنجاح.")
            st.rerun()
            
    with tab_research:
        st.markdown('### 📊 مستودع الأدلة السريرية الواقعية لتقديمها للمؤسسات الدولية (Real-World Evidence)')
        conn = sqlite3.connect('cellrevive_quantum_system.db')
        try: res_df = pd.read_sql_query("SELECT fbg, ppbg, hba1c, severity_score, compliance_score, age, gender FROM patients", conn)
        except Exception: res_df = pd.DataFrame()
        finally: conn.close()
            
        if not res_df.empty:
            col_stat1, col_stat2 = st.columns(2)
            col_stat1.metric("إجمالي الحالات المسجلة أبحاثاً", len(res_df))
            col_stat2.metric("متوسط التراكمي في الداتا", f"{round(res_df['hba1c'].mean(), 2)}%")
            fig_hist = px.histogram(res_df, x="hba1c", title="توزيع السكر التراكمي بين عينات المرضى", color_discrete_sequence=['#d4af37'])
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("لا توجد بيانات كافية في مستودع الأبحاث حالياً.")

# 9️⃣ شاشة المشترك المتقدمة وطب طول العمر
if st.session_state.role == "patient":
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; border: 2px solid #d4af37; padding: 8px; border-radius: 8px;">لوحتك العلاجية المخصصة تحت إشراف د. إيهاب حشمت الظني</p>', unsafe_allow_html=True)
    homa_calc = calculate_homa_ir(p_data['fbg'], p_data['fasting_insulin'])
    bio_age_calc = calculate_biological_age(p_data['age'], p_data['hba1c'], homa_calc, p_data['hscrp'], p_data['waist'])
    egfr_calc = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 15px 0; font-size:18px;">🧬 مجهر طول العمر وعمر الخلايا (Biological Longevity Core)</h3>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div><span style="font-size:14px; opacity:0.8;">العمر الزمني:</span><br><b style="font-size:24px; color:#ffffff;">{p_data['age']} سنة</b></div>
                <div><span style="font-size:14px; opacity:0.8;">العمر البيولوجي:</span><br><b style="font-size:24px; color:#00ffcc;">{bio_age_calc} سنة</b></div>
                <div><span style="font-size:14px; opacity:0.8;">كفاءة الكلى (eGFR):</span><br><b style="font-size:24px; color:#ffcc00;">{egfr_calc}</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 📸 تبويب مسح الوجبة وتصويرها باستخدام الذكاء الاصطناعي المحدث 2026
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown("### 📸 ماسح الوجبات الخلوي الفوري والذكاء الأيضي")
    
    analysis_mode = st.radio("اختر طريقة إدخال الوجبة لتحليلها خلوياً:", ["تصوير الوجبة بالكاميرا / رفع صورة", "كتابة الوجبة نصياً"])
    
    meal_image = None
    user_meal_text = ""
    
    if analysis_mode == "تصوير الوجبة بالكاميرا / رفع صورة":
        meal_image = st.file_uploader("التقط صورة لوجبتك الآن أو قم برفعها لوضعها تحت المجهر الأيضي:", type=["jpg", "jpeg", "png"])
        if meal_image:
            st.image(meal_image, caption="📷 الوجبة المراد فحصها وهندستها", use_container_width=True)
    else:
        user_meal_text = st.text_input("اكتب ما تريد أن تأكله الآن بدقة (مثال: حلاوة سبريد و2 رغيف عيش بلدي):")

    if st.button("🔬 بدء المسح والتحليل الجينومي للوجبة"):
        if not ACTIVE_API_KEY:
            st.error("⚠️ يرجى التأكد من إدخال مفتاح الـ API الخاص بجوجل في لوحة الإشراف لتفعيل وظائف الذكاء الاصطناعي.")
        else:
            with st.spinner("⏳ جاري تحليل البصمة الأيضية ومحاكاة الاستجابة الخلوية للوجبة..."):
                prompt = f"""
                You are CellRevive AI, an expert metabolic operating system under the supervision of clinical pharmacist Dr. Ehab Heshmat El-Zanny.
                Analyze this meal for a patient with Fasting Glucose: {p_data['fbg']}, HbA1c: {p_data['hba1c']}%, and MTHFR: {p_data['mthfr_mutation']}.
                
                Provide a complete medical and nutritional critique in professional yet highly accessible Egyptian Arabic vernacular.
                Include:
                1. Impact on glucose spike (هل ستسبب طفرة سكر حادة؟).
                2. Explicit food sequencing advice (الترتيب الأمثل لتناول مكونات الوجبة لتسطيح المنحنى).
                3. Propose local, healthy alternatives if the meal is hazardous (like halawa spread which triggers massive spikes). Mention how 'Eish Baladi' (Egyptian flatbread with bran) acts compared to white bread.
                4. Tone must be encouraging, tailored to Egyptian patients, and ends with a greeting from Dr. Ehab.
                """
                try:
                    # 🛠️ التحديث الحاسم لعام 2026: استخدام الموديل المستقر المحدث لحل خطأ 404
                    model = genai.GenerativeModel('gemini-1.5-flash-latest')
                    
                    if analysis_mode == "تصوير الوجبة بالكاميرا / رفع صورة" and meal_image:
                        img = Image.open(meal_image)
                        response = model.generate_content([prompt, img])
                    else:
                        if not user_meal_text:
                            st.warning("برجاء كتابة مكونات الوجبة أولاً.")
                            st.stop()
                        response = model.generate_content(f"{prompt}\n\nPatient says he wants to eat: {user_meal_text}")
                    
                    st.markdown("### 🧬 التقرير الأيضي وهندسة الوجبة فسيولوجياً:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال بالخادم الأيضي: {e}")
    st.markdown('</div>', unsafe_allow_html=True)
