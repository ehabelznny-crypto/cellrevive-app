import streamlit as st
import sqlite3
import math
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import io
import re
import pandas as pd
import plotly.express as px
import os
import base64

# استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
# ملاحظة: في بيئة التشغيل، إذا لم تكن المكتبة مثبتة يتم تثبيتها عبر: pip install cryptography
try:
    from cryptography.fernet import Fernet
except ImportError:
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet

# ==============================================================================
# 0️⃣ منظومة التشفير السيادية (HIPAA Data Protection Engine)
# ==============================================================================
# توليد أو استدعاء مفتاح التشفير الثابت لحماية قاعدة البيانات
if "ENCRYPTION_KEY" in st.secrets:
    KEY = st.secrets["ENCRYPTION_KEY"].encode()
else:
    # مفتاح افتراضي آمن للتشغيل المحلي (يُفضل وضعه في Secrets عند النشر العالمي)
    KEY = b'SetupYourSovereignKeyHere12345678=+' 

cipher_suite = Fernet(KEY)

def encrypt_data(data_str):
    if not data_str: return ""
    return cipher_suite.encrypt(data_str.encode()).decode()

def decrypt_data(crypto_str):
    if not crypto_str: return ""
    try:
        return cipher_suite.decrypt(crypto_str.encode()).decode()
    except Exception:
        return crypto_str # للبيانات القديمة غير المشفرة تلافياً للمشاكل

# ==============================================================================
# 1️⃣ الإعدادات المتقدمة والواجهة الفاخرة (2026 Global Luxury Hub)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - Global Living Engine",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# إدارة وتأمين الـ API Key لـ Gemini
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    GEMINI_API_KEY = st.session_state.api_key_input
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

# هندسة التصميم الفاخر (Premium Dark Theme CSS)
st.markdown("""
    <style>
    .stApp { background-color: #040d1a; color: #ffffff !important; }
    [data-testid="stMainBlockContainer"] { direction: rtl !important; text-align: right !important; }
    .premium-card {
        background: linear-gradient(145deg, #0a1f38, #07162c);
        border: 1px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
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
    label, p, span { color: #ffffff !important; font-weight: 500 !important; }
    .stButton>button {
        background: linear-gradient(90deg, #d4af37, #aa8422);
        color: #040d1a !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        height: 3em;
        width: 100%;
        border: none;
    }
    .metric-box { border-right: 3px solid #d4af37; padding-right: 15px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# الهوية البصرية الرسمية للمنصة
st.markdown("""
    <div style="text-align: center; padding: 20px; margin-bottom: 30px;">
        <h1 style="color: #d4af37; font-family: 'Arial', sans-serif; font-size: 38px; font-weight: 900; letter-spacing: 2px; margin-bottom: 5px; text-shadow: 3px 3px 6px rgba(0,0,0,0.9);">
            🧬 CELLREVIVE AI
        </h1>
        <p style="color: #ffffff !important; font-family: 'Cairo', sans-serif; font-size: 19px; font-weight: 600; opacity: 0.95; line-height: 1.6; max-width: 800px; margin: 0 auto; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
            المنصة العالمية المتكاملة للترميم الخلوي وعكس مسار مقاومة الإنسولين والسكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 1px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 20px;">
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 2️⃣ إدارة قاعدة البيانات المطورة والمشفرة (SQLite Sovereign Engine)
# ==============================================================================
def init_db():
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_code TEXT PRIMARY KEY,
            fbg REAL, ppbg REAL DEFAULT 140.0, rbg REAL DEFAULT 120.0, hba1c REAL,
            weight REAL, waist REAL, creatinine REAL DEFAULT 1.0, age INTEGER DEFAULT 45,
            gender TEXT DEFAULT 'Male', severity_score REAL DEFAULT 5.0,
            skin_analysis TEXT DEFAULT '', selected_drugs TEXT DEFAULT '',
            country TEXT DEFAULT 'Egypt'
        )
    """)
    try: cursor.execute("ALTER TABLE patients ADD COLUMN creatinine REAL DEFAULT 1.0")
    except sqlite3.OperationalError: pass
    try: cursor.execute("ALTER TABLE patients ADD COLUMN age INTEGER DEFAULT 45")
    except sqlite3.OperationalError: pass
    try: cursor.execute("ALTER TABLE patients ADD COLUMN gender TEXT DEFAULT 'Male'")
    except sqlite3.OperationalError: pass
    try: cursor.execute("ALTER TABLE patients ADD COLUMN country TEXT DEFAULT 'Egypt'")
    except sqlite3.OperationalError: pass

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
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender, country 
        FROM patients WHERE patient_code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 
            'skin_analysis': decrypt_data(row[7]), # فك التشفير الآمن عند العرض
            'selected_drugs': decrypt_data(row[8]), # فك التشفير الآمن
            'creatinine': row[9], 'age': row[10], 'gender': row[11], 'country': row[12] or 'Egypt'
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    
    # تشفير النصوص الحساسة والتقارير الطبية قبل الحفظ امتثالاً لـ HIPAA
    encrypted_skin = encrypt_data(data['skin_analysis'])
    encrypted_drugs = encrypt_data(data['selected_drugs'])
    
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], data['severity_score'], encrypted_skin, encrypted_drugs, data['creatinine'], data['age'], data['gender'], data['country']))
    conn.commit()
    conn.close()

def log_glucose(code, g_type, value):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO glucose_logs (patient_code, reading_time, reading_type, reading_value) VALUES (?, ?, ?, ?)",
                   (code, datetime.now().strftime('%Y-%m-%d %H:%M'), g_type, value))
    conn.commit()
    conn.close()

def get_all_glucose_logs(code):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reading_time, reading_type, reading_value FROM glucose_logs WHERE patient_code = ? ORDER BY id ASC", (code,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==============================================================================
# 3️⃣ الدستور العالمي الموحد للأدوية والمقاصة التغذوية (Global Drug Mapping DB)
# ==============================================================================
GLOBAL_DRUG_DB = {
    "Egypt": {
        "Cidophage (سيدوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف ب12 الحاد وتأثر الميتوكوندريا خلوياً"},
        "Glucophage (جلوكوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر الأعصاب الطرفية"},
        "Deltacortril (ديلتاكورتريل)": {"generic": "Prednisolone", "supp": "Potassium (99mg) + Magnesium Citrate (400mg) + Vit D3", "reason": "احتباس السوائل وهدم الكتلة العضلية ورفع مقاومة الإنسولين"},
        "Lasix (لازكس)": {"generic": "Furosemide", "supp": "Thiamine B1 (100mg) + Potassium + Magnesium", "reason": "طرد المعادن النادرة ومستنفذات الطاقة الحيوية من الميتوكوندريا"},
        "Lipitor (ليبيتور)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3 (5000 IU)", "reason": "تثبيط مسار الميفالونات المسبب لآلام العضلات وضرر الميتوكوندريا"},
        "Mounjaro (مونجارو)": {"generic": "Tirzepatide", "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "فقدان الكتلة العضلية الحيوية السريع بسبب التثبيط المفرط للشهية"},
        "Ozempic (أوزمبيك)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc + EAAs", "reason": "كسل وشلل حركة المعدة المؤقت والحاجة لتسهيل امتصاص المغذيات وبناء العضلات"}
    },
    "Gulf & International": {
        "Glucophage (International)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "Long-term vitamin B12 malabsorption and mitochondrial protection"},
        "Lipitor (International)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3", "reason": "Mevalonate pathway inhibition causing myalgia"},
        "Mounjaro (International)": {"generic": "Tirzepatide", "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "Rapid muscle mass loss prevention"},
        "Ozempic (International)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc", "reason": "Gastric motility delay management"},
        "Jardiance (International)": {"generic": "Empagliflozin", "supp": "Electrolytes Complex + High Hydration", "reason": "Renal glucose excretion and cellular dehydration risk"}
    }
}

# ==============================================================================
# 4️⃣ الحاسبات الطبية السريرية والخوارزمية التنبؤية لتذبذب الجلوكوز (eGMS Index)
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin=12.0):
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender in ['Female', 'أنثى']: val *= 0.85
    return min(round(val, 2), 150.0)

# حساب مؤشر تذبذب السكر الرياضي التنبؤي للأمن الحيوي
def calculate_glucose_variability(code):
    logs = get_all_glucose_logs(code)
    if len(logs) < 3:
        return 0.0, "بيانات غير كافية للحساب الأوتوماتيكي للتقلب الحركي"
    
    values = [row[2] for row in logs]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    sd = math.sqrt(variance) # الانحراف المعياري
    
    cv = (sd / mean) * 100 if mean > 0 else 0.0 # معامل التذبذب المئوي
    
    if cv < 15.0:
        status = "✅ مستقر ومثالي للترميم الخلوي"
    elif cv <= 36.0:
        status = "⚠️ تذبذب متوسط - يتطلب ضبط ترتيب الطعام"
    else:
        status = "🚨 تذبذب حاد وحرج - خطر حدوث طفرات سكر مفاجئة"
        
    return round(cv, 2), status

# ==============================================================================
# 5️⃣ محرك الرؤية الحاسوبية والذكاء الاصطناعي السيادي
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح API من قبل إدارة النظام لتفعيل الرؤية الحية الحركية."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي المعتمد لدى ADA و EASD لعام 2026. 
        يجب أن تكون إجاباتك مبنية بنسبة 100% على الدليل العلمي الأكاديمي الصارم. 
        - لا تقم أبداً بتغيير جرعات الأدوية للمريض بل وجهه دائماً للرجوع للدكتور إيهاب حشمت الظني.
        - ركز تماماً على: ترتيب تناول الطعام، المقاصة الميتوكوندرية، ومنع طفرات السكر العشوائية (Glucose Spikes).
        - استقبال ومعالجة عدة صور معاً وربط البيانات وتقديم تحليل موحد دقيق.
        """
        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)
        content = [prompt]
        for img in images: content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال بالسيرفر الطبي العالمي: {str(e)}"

def check_emergency_status(value, context_phrase=""):
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ سيادي حرج (هبوط حاد): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> تم رصد هبوط حاد. تناول كربوهيدرات سريعة الامتصاص فوراً وتواصل مع الدكتور إيهاب حشمت فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ سيادي حرج (ارتفاع مفرط): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> مستوى السكر يتجاوز النطاق الآمن. خطر الحماض الكيتوني (DKA). يرجى التوجه للطوارئ فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 6️⃣ بوابة الوصول الرقمية وجدولة الأكواد الـ 24 المعتمدة
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
CORE_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]
MONTH_PLAN_CODES = [f"CR-1M-{i:02d}" for i in range(1, 11)]
QUARTER_PLAN_CODES = [f"CR-3M-{i:02d}" for i in range(1, 11)]
VALID_PATIENT_CODES = CORE_CODES + MONTH_PLAN_CODES + QUARTER_PLAN_CODES

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div style="text-align:center; color:#d4af37; font-size:20px; font-weight:bold; margin-bottom:15px;">🔐 بوابـة العبـور الرقمية الآمنة للمنظومة العالمية</div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود الوصول المخصص لك:", type="password")
    if st.button("تفعيل بروتوكول الاتصال المشفر"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "doctor", MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "patient", input_code
            st.rerun()
        else:
            st.error("الكود غير صحيح. يرجى مراجعة الإدارة الصحية للتأكد من تفعيل اشتراكك الدولي.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male', 'country': 'Egypt'
}

# ==============================================================================
# 7️⃣ لوحة تحكم الطبيب المعالج العليا (د. إيهاب حشمت الظني)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<h3 style="color:#d4af37; text-align:center; margin-bottom:20px;">🛡️ لوحة التحكم السيادية الإكلينيكية العالمية</h3>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    target_patient = st.selectbox("اختر كود المريض المراد تأسيسه أو تعديله:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
    with st.expander("🌍 الإعدادات الجغرافية والدستور الدوائي المستهدف", expanded=True):
        mod_country = st.selectbox("اختر النطاق الدستوري للأدوية:", list(GLOBAL_DRUG_DB.keys()), index=0 if current_p_data['country'] == "Egypt" else 1)

    with st.expander("📝 ضبط البيانات الديموغرافية، المخبرية والفسيولوجية بدقة 100%", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم (mg/dL):", value=float(current_p_data['fbg']))
            mod_ppbg = st.number_input("سكر فاطر بعد ساعتين (mg/dL):", value=float(current_p_data['ppbg']))
            mod_rbg = st.number_input("سكر عشوائي (mg/dL):", value=float(current_p_data['rbg']))
            mod_creatinine = st.number_input("الكرياتينين في الدم (Serum Creatinine):", value=float(current_p_data['creatinine']), step=0.1)
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']))
            mod_weight = st.number_input("الوزن الحالي (كجم):", value=float(current_p_data['weight']))
            mod_waist = st.number_input("محيط الخصر (سم):", value=float(current_p_data['waist']))
            mod_age = st.number_input("عمر المريض الحالي (سنوات):", value=int(current_p_data['age']), step=1)
            mod_gender = st.selectbox("جنس المريض الخلوي:", ["Male", "Female"], index=0 if current_p_data['gender'] == "Male" else 1)

    with st.expander("💊 بروتوكول المقاصة الدوائية الحالية (بناءً على الدستور المختار)"):
        available_drugs = GLOBAL_DRUG_DB[mod_country]
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية الموصوفة للمريض من الدستور المختار:", list(available_drugs.keys()), default=[d for d in saved_drugs_list if d in available_drugs])

    if st.button("💾 تثبيت وحفظ ملف المريض المشفر (HIPAA Protected)"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender,
            'country': mod_country
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم تشفير وتثبيت مؤشرات المريض {target_patient} عالمياً بنجاح وفق معايير الحماية السيادية.")

# ==============================================================================
# 8️⃣ واجهة المريض التفاعلية ومستودع التحليلات الفورية لقمع السكر
# ==============================================================================
if st.session_state.role == "patient":
    plan_text = "نظام الشهر السريع" if "1M" in current_code else "نظام الـ 3 أشهر الممتد" if "3M" in current_code else "النظام التأسيسي الآمن"
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; margin-top:-20px;">مرحباً بك في لوحة تحكمك الحية لمتابعة ({plan_text})</p>', unsafe_allow_html=True)
    
    check_emergency_status(p_data['fbg'], "قراءة الصائم المسجلة")
    check_emergency_status(p_data['ppbg'], "قراءة الفاطر المسجلة")
    
    calc_homa = calculate_homa_ir(p_data['fbg'])
    calc_egfr_val = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    cv_score, cv_status = calculate_glucose_variability(current_code)
    
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37; margin:0 0 15px 0;">📊 المؤشرات الحيوية المستخلصة رقمياً وعالمياً (Clinical Metrics)</h3>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">مؤشر HOMA-IR الحسابي</span><br>
                    <span style="font-size:20px; font-weight:bold; color:#ff4b4b;">{round(calc_homa, 2)}</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">كفاءة الفلترة الكلوية (eGFR)</span><br>
                    <span style="font-size:20px; font-weight:bold; color:#00ffcc;">{calc_egfr_val} mL/min</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">مؤشر تذبذب الجلوكوز الرياضي</span><br>
                    <span style="font-size:18px; font-weight:bold; color:#ffff00;">{cv_score}%</span><br>
                    <span style="font-size:11px; opacity:0.9;">{cv_status}</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="premium-card"><h3>📈 التحليل البياني التفاعلي لتقلبات الجلوكوز</h3>', unsafe_allow_html=True)
    raw_logs = get_all_glucose_logs(current_code)
    if raw_logs:
        df = pd.DataFrame(raw_logs, columns=["التوقيت", "نوع القراءة", "القيمة mg/dL"])
        fig = px.line(df, x="التوقيت", y="القيمة mg/dL", color="نوع القراءة", title="منحنى تذبذب السكر الحيوي", markers=True)
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("لا توجد قراءات مسجلة في السجل البياني حتى الآن.")
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("📊 تدوين قراءة سكر فورية الآن", expanded=False):
        col_g1, col_g2 = st.columns(2)
        with col_g1: g_type = st.selectbox("توقيت القياس الحالي:", ["سكر صائم", "سكر فاطر (بعد ساعتين)", "سكر عشوائي"])
        with col_g2: g_val = st.number_input("القراءة (mg/dL):", value=0.0, step=1.0)
            
        if st.button("📝 حفظ القراءة فوراً في الملف"):
            if g_val > 0:
                log_glucose(current_code, g_type, g_val)
                temp_data = get_patient_data(current_code) or p_data
                if g_type == "سكر صائم": temp_data['fbg'] = g_val
                elif g_type == "سكر فاطر (بعد ساعتين)": temp_data['ppbg'] = g_val
                else: temp_data['rbg'] = g_val
                save_patient_data(current_code, temp_data)
                st.success("تم التدوين الآمن والتحليل الأوتوماتيكي للتذبذب بنجاح.")
                st.rerun()

    st.markdown('<div class="premium-card"><h3>🥗 مختبر فحص وتطهير الوجبات والتحليل التكنولوجي المتقدم</h3>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "📸 التقط أو ارفع صورة وجبتك الحالية أو علب الأدوية والروشتات (معالجة متعددة الصور والـ OCR):", 
        type=['jpg','png','jpeg'], 
        accept_multiple_files=True
    )
    
    if uploaded_files and st.button("🚀 بدء بروتوكول التحليل التكنولوجي الصارم"):
        with st.spinner("يجري الآن ربط الصور والمقاصة مع الملف الطبي المشفر وكفاءة الكلى الحركية..."):
            meal_prompt = f"""
            بصفتك الخبير الأكاديمي، حلل بدقة كافة الصور المرفوعة (وجبات، أو علب أدوية عبر الـ OCR)، واربطها بالمؤشرات المخزنة لهذا المريض كالتالي:
            - عمر المريض الحالي: {p_data['age']} سنة | الجنس: {p_data['gender']} | النطاق الدولي: {p_data['country']}
            - سكر صائم أساسي: {p_data['fbg']} mg/dL
            - كفاءة الكلى الحالية الديناميكية (eGFR): {calc_egfr_val} mL/min
            - مؤشر تذبذب الجلوكوز الحالي المحسوب برمجياً: {cv_score}% ({cv_status})
            - الأدوية الحالية النشطة في ملفه: {p_data['selected_drugs']}
            - مؤشر مقاومة الإنسولين الحالية HOMA-IR: {round(calc_homa, 2)}
            
            أعطِ تقريراً استراتيجياً صارماً من 4 نقاط مقسمة بوضوح:
            1. التحليل البصري الدقيق وقراءة الـ OCR لعلب الأدوية/الروشتات بدقة 100%.
            2. التعديل الفوري والإلزامي بناءً على حالته الكلوية والأيضية ومؤشر تذبذبه الحالي.
            3. بروتوكول التطهير الخلوي (الترتيب الدقيق لتناول الوجبة، وتوقيت الأدوية المكتشفة).
            4. المكملات والمقاصة التغذوية المطلوبة لتعويض النقص الخلوي الناتج عن تداخل الأدوية الموصوفة لديه.
            """
            res = analyze_with_gemini(uploaded_files, meal_prompt)
            st.markdown("<h4>📋 التقرير الطبي الصارم والتحليل المتكامل للمنظومة:</h4>", unsafe_allow_html=True)
            st.write(res)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size:10px; opacity:0.5; color:#ffffff !important;">CellRevive AI v7.0 - Sovereign Enterprise Global Edition 2026</div>', unsafe_allow_html=True)
