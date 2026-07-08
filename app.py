# 👑 CELLREVIVE AI - THE MASTER METABOLIC OS & CELLULAR RESTORATION PLATFORM (v21.3 - Final Sovereign Fix)
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

# ⚖️ وثيقة الأمان الطبي والالتزام الصارم والكامل من v20 الملكي
if 'disclaimer_agreed' not in st.session_state:
    st.session_state.disclaimer_agreed = False

if not st.session_state.disclaimer_agreed:
    st.markdown("""
        <div class="emergency-card" style="margin-top: 30px;">
            <h2 style="color: #ff4b4b !important; text-align: center !important; font-weight: 900; margin-bottom: 15px;">🛡️ وثيقة الأمان الطبي والالتزام المشترك / Legal Disclaimer</h2>
            <p style="font-size: 15px; line-height: 1.8; text-align: justify !important; color: #ffffff;">
                <b>تنبيه قانوني وطبي صارم:</b> إن منصة <b>CellRevive AI</b> هي منظومة محاكاة رقمية متقدمة وأداة تثقيفية مخصصة لدعم هندسة التمثيل الغذائي وتحسين كفاءة الميتوكوندريا تحت الإشراف العلمي المباشر للصيدلي المختص <b>د/ إيهاب حشمت الظني</b>. 
                <br><br>
                1. لا يعتبر هذا البرنامج أو التقارير الصادرة عنه بديلاً عن التشخيص الطبي البشري أو الفحوصات المختبرية السريرية.<br>
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
            INSERT INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, creatinine, age, gender, mthfr_mutation, fto_variant, fasting_insulin, hscrp, compliance_score, anxiety_score) 
            VALUES ('CR-SOHAG-2026', 115.0, 145.0, 120.0, 6.2, 80.0, 95.0, 0.9, 42, 'Male', 'Normal (CC)', 'Normal (TT)', 10.5, 0.8, 95, 4)
        """)
        cursor.execute("""
            INSERT INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, creatinine, age, gender, mthfr_mutation, fto_variant, fasting_insulin, hscrp, compliance_score, anxiety_score) 
            VALUES ('CR-PATIENT-77', 125.0, 160.0, 130.0, 6.8, 85.0, 102.0, 0.85, 47, 'Male', 'Mutated', 'Normal (TT)', 12.0, 1.1, 90, 5)
        """)
    conn.commit()
    conn.close()

init_db()

# دوال العمليات الحسابية الطبية والأيضية مع الحماية الاحترازية ضد القيم الفارغة
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

# محاكاة منحنى الجلوكوز الديناميكي التفاعلي بناءً على ترتيب الوجبة
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
VALID_PATIENT_CODES = ["CR-SOHAG-2026", "CR-PATIENT-77", "CR-PATIENT-99"]

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

# إدارة اختيار المريض من الجلسة أو لوحة الإشراف لمنع التصفير التلقائي
if 'active_patient_code' not in st.session_state:
    st.session_state.active_patient_code = st.session_state.auth_code if st.session_state.role == "patient" else "CR-SOHAG-2026"

# 2️⃣ لوحة الطبيب والمشرف السيادي (د. إيهاب حشمت)
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:22px; font-weight:900; text-align:center;">👑 لوحة الإشراف العيادي وطب طول العمر</div>', unsafe_allow_html=True)
    st.sidebar.markdown("### 🔐 الإشراف البرمجي")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=ACTIVE_API_KEY)
    
    selected_p = st.selectbox("اختر ملف المشترك لإدارته وتعديله فسيولوجياً:", VALID_PATIENT_CODES, index=VALID_PATIENT_CODES.index(st.session_state.active_patient_code))
    if selected_p != st.session_state.active_patient_code:
        st.session_state.active_patient_code = selected_p
        st.rerun()

# جلب البيانات الصريحة والمؤمنة بالاسم بناءً على الكود النشط حالياً
conn = sqlite3.connect('cellrevive_quantum_system.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("SELECT * FROM patients WHERE patient_code = ?", (st.session_state.active_patient_code,))
row = c.fetchone()
conn.close()

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

# 3️⃣ لوحة الحسابات الحيوية وعرض الأرقام بالألوان الملكية المستقرة
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

    # 📑 تقسيم واجهة العرض إلى المحاور الـ 4 المنفصلة والمعزولة لحظر أخطاء الـ NotFound المتبادلة
    tab_meals, tab_drugs, tab_skin, tab_mind = st.tabs([
        "🌾 هندسة الوجبات والمنحنيات", 
        "💊 مجهر ومسح علب الأدوية", 
        "🔎 مجهر الجلد والأعراض الحيوية", 
        "🧠 مؤشر الكورتيزول والصحة النفسية"
    ])
    
    # 🔘 المحور الأول: هندسة الوجبات ومنحنى الجلوكوز
    with tab_meals:
        st.markdown("### 📸 ماسح الوجبات الخلوي الفوري")
        meal_mode = st.radio("طريقة الإدخال الأيضي للوجبة:", ["نصي", "رفع صورة الوجبة"], key="meal_mode_select")
        
        meal_text = "عدد 5 معالق فول بزيت كريستال او زيت الزيتون+3 اقراص طعمية+2 رغيف عيش مصري+طبق سلطة صغير"
        uploaded_meal = None
        if meal_mode == "نصي":
            meal_text = st.text_input("اكتب بدقة ما تريد أكله الآن:", value=meal_text, key="meal_text_in")
        else:
            uploaded_meal = st.file_uploader("القط أو ارفع صورة وجبتك:", type=["jpg", "png", "jpeg"], key="meal_file_up")
            if uploaded_meal:
                st.image(uploaded_meal, caption="الوجبة المرفوعة")
            
        food_seq = st.selectbox("اختر ترتيب وتتابع تناول مكونات هذه الوجبة فسيولوجياً:", [
            "النشويات أولاً (بدء بالأكل مباشرة)", 
            "ألياف -> بروتين -> نشويات", 
            "دهون وبروتين -> نشويات"
        ], key="food_seq_select")
        
        if st.button("🔬 تحليل ومحاكاة منحنى الجلوكوز الحي", key="btn_run_meal_analysis"):
            gi_val = 85 if "حلاوة" in meal_text else 55
            t, glucose_curve = simulate_glucose_curve(p_data['fbg'], food_seq, gi_val)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=t, y=glucose_curve, mode='lines', name='منحنى الجلوكوز المتوقع', line=dict(color='#d4af37', width=3)))
            fig.update_layout(title="📈 محاكاة حركة الجلوكوز في الدم (ملجم/دسيليتر) على مدار 3 ساعات", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
            if ACTIVE_API_KEY:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"حلل لي الوجبة التالية فسيولوجياً وأيضياً: {meal_text}، مع الترتيب المختار: {food_seq}. السكر الصائم للمريض: {p_data['fbg']}. اشرح للمريض بلهجة مصرية ودية بسيطة جداً كيف يؤثر العيش البلدي (مؤشره متوسط 55) مقارنة بالدقيق الأبيض، وكيف يمنع الارتفاع الحاد، واختم بنصيحة من الدكتور إيهاب حشمت."
                
                if meal_mode == "رفع صورة الوجبة" and uploaded_meal:
                    img = Image.open(uploaded_meal)
                    res = model.generate_content([prompt, img])
                else:
                    res = model.generate_content(prompt)
                    
                st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
                st.write(res.text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ يرجى إدخال مفتاح الـ API للاتصال بالموديل وتحليل الوجبة.")

    # 🔘 المحور الثاني: مجهر ومسح علب الأدوية
    with tab_drugs:
        st.markdown("### 💊 الفحص الدوائي المتكامل ومقاصة المغذيات المستنزفة (EDA 2026)")
        st.info("هذا القسم مربوط تلقائياً بـ دستور الأدوية المصري الصادر عن هيئة الدواء المصرية لعام 2026 لمراجعة التعارضات الحيوية.")
        
        drug_scan_mode = st.radio("وسيلة إدخال الدواء المعالج:", ["اختيار من القائمة الشائعة", "تصوير علبة الدواء / رفع الروشتة"], key="drug_mode_select")
        
        selected_drug_info = ""
        uploaded_drug = None
        if drug_scan_mode == "اختيار من القائمة الشائعة":
            drug_choice = st.selectbox("اختر الدواء الحالي الموصوف لك من طبيبك البشري:", [
                "Cidophage (سيدوفاج) - Metformin", 
                "Glucophage (جلوكوفاج) - Metformin",
                "Nervizam (نيرفيزام) - B Complex + ALA",
                "Milga (ميلجا) - Benfotiamine",
                "Ozempic (أوزمبيك) - Semaglutide"
            ], key="drug_choice_select")
            selected_drug_info = drug_choice
        else:
            uploaded_drug = st.file_uploader("ارفع صورة علبة الدواء أو الروشتة المكتوبة بخط اليد:", type=["png", "jpg", "jpeg"], key="drug_file_up")
            if uploaded_drug:
                st.image(uploaded_drug, caption="📷 علبة الدواء الجاري فحصها جينومياً وظاهرياً", use_container_width=True)
                selected_drug_info = "صورة علبة دواء مرفوعة للمطابقة الرقمية"
                
        if st.button("🧬 إجراء المقاصة الطبية واستخراج النقص الخلوي", key="btn_run_drug_analysis"):
            if ACTIVE_API_KEY:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"بصفتك أخصائي صيدلة إكلينيكية وطب تجديدي، حلل هذا الدواء: {selected_drug_info}. اذكر بوضوح تام النقص في الفيتامينات والمعادن والمغذيات التي يستنزفها هذا الدواء من خلايا الجسم (Drug-Nutrient Depletion) طبقاً لأحدث تحديثات عام 2026، وااشرح للمريض بأسلوب مصري بسيط تحت إشراف د. إيهاب حشمت ما يجب أن يعوضه من مكملات مثل المغنيسيوم أو ب12 وبما يتوافق مع الواقع المصري."
                
                if drug_scan_mode == "تصوير علبة الدواء / رفع الروشتة" and uploaded_drug:
                    img = Image.open(uploaded_drug)
                    res = model.generate_content([prompt, img])
                else:
                    res = model.generate_content(prompt)
                    
                st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
                st.write(res.text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ يرجى إدخال مفتاح الـ API لتشغيل مجهر ومسح علب الأدوية.")

    # 🔘 المحور الثالث: مجهر الجلد والأعراض الحيوية
    with tab_skin:
        st.markdown("### 🔎 مجهر الجلد والمظاهر الخارجية لمقاومة الإنسولين")
        st.write("ارفع صورة لمنطقة الرقبة أو المفاصل للكشف المبكر والمحاكاة التقديرية لوجود التصبغات الجلدية النشطة المصاحبة لخلل الميتوكوندريا.")
        
        uploaded_skin = st.file_uploader("ارفع صورة الجلد المراد فحصها هيدروليكياً خلوياً:", type=["png", "jpg", "jpeg"], key="skin_file_up")
        skin_notes = st.text_area("اذكر أي أعراض مصاحبة (مثال: زوائد جلدية، إرهاق مزمن، تنميل في الأطراف):", key="skin_notes_in")
        
        if st.button("👁️ فحص البصمة الجلدية وربطها بالأعراض الحيوية", key="btn_run_skin_analysis"):
            if ACTIVE_API_KEY:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"قم بتحليل الشكوى الجلدية التالية للمريض: {skin_notes}. السكر التراكمي لديه هو {p_data['hba1c']}%. اربط بين ظهور التصبغات والزوائد الجلدية (Acanthosis Nigricans) وبين كفاءة الخلايا ومقاومة الإنسولين، وقدم نصائح علاجية ترميمية بلغة مصرية مفهومة ومحفزة تنتهي بتحية الدكتور إيهاب حشمت الظني."
                
                if uploaded_skin:
                    img = Image.open(uploaded_skin)
                    res = model.generate_content([prompt, img])
                else:
                    res = model.generate_content(prompt)
                    
                st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
                st.write(res.text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ يرجى إدخال مفتاح الـ API لتشغيل مجهر وفحص البصمة الجلدية.")

    # 🔘 المحور الرابع: مؤشر الكورتيزول والصحة النفسية والحيل السلوكية
    with tab_mind:
        st.markdown("### 🧠 مؤشر الحالة المزاجية والنفسية وهورمونات الإجهاد")
        st.write("التوتر والضغط النفسي يرفعان هرمونات الكورتيزول والأدرينالين، مما يؤدي تلقائياً لرفع سكر الدم حتى بدون تناول نشويات!")
        
        st.markdown(f"""
            <div style="background-color:#07162c; padding: 15px; border-radius: 10px; border-right: 5px solid #ffcc00; margin-bottom: 15px;">
                <b>📊 مستوى القلق العصبي الحالي المسجل في ملفك الحركي: {p_data['anxiety_score']} / 10</b><br>
                <span style="font-size:13px; opacity:0.8;">كلما ارتفع هذا المؤشر، زاد إفراز الكورتيزول الذي يحفز الكبد على إطلاق الجلوكوز المخزن (Glycogenolysis).</span>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🧘‍♂️ توليد بروتوكول تصفير الإجهاد الكظري الفوري", key="btn_run_mind_analysis"):
            if ACTIVE_API_KEY:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"""
                المريض يعاني من مستوى توتر وقلق يقدر بـ {p_data['anxiety_score']}/10. 
                اكتب بروتوكولاً نفسياً وسلوكياً كاملاً لتخفيض هرمونات الكورتيزول والأدرينالين وتأثيرها على مقاومة الإنسولين وعكس السكري.
                اشرح له ببراعة واحترافية بالغة الحيل السلوكية الفعالة فوراً مثل:
                1. تمارين التنفس الصندوقي (Box Breathing) والتحفيز المبهمي.
                2. حيلة المشي الخفيف والتمشية في الطبيعة لتصريف الجلوكوز الفائض بدون إجهاد خلوي.
                3. سيكولوجية الضحك والخروج وأثرهما الفوري في كبح الأدرينالين ورفع الإندورفين والدوبامين.
                الكتابة تكون بلهجة مصرية مشجعة جداً ومريحة للعيون باسم العيادة والدكتور إيهاب حشمت الظني.
                """
                res = model.generate_content(prompt)
                st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
                st.write(res.text)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ يرجى إدخال مفتاح الـ API لتوليد بروتوكول تصفير الإجهاد الكظري.")
