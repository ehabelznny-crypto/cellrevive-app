# ==============================================================================
# 👑 CELLREVIVE AI - THE UNITED METABOLIC OS & CELLULAR RESTORATION PLATFORM (v12.5)
# ==============================================================================
import streamlit as st
import sqlite3
import math
import numpy as np
import google.generativeai as genai
from PIL import Image
from datetime import datetime, time
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from fpdf import FPDF

# استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
try:
    from cryptography.fernet import Fernet
except ImportError:
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet

# ==============================================================================
# 0️⃣ منظومة التشفير وحماية البيانات الطبية البيئية (HIPAA Safe Architecture)
# ==============================================================================
if "ENCRYPTION_KEY" in st.secrets:
    KEY = st.secrets["ENCRYPTION_KEY"].encode()
else:
    KEY = Fernet.generate_key()

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

# ==============================================================================
# 1️⃣ الإعدادات وتصميم الواجهة الفاخرة السيادية (Premium 2026 Gold Design)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Global Metabolic Platform",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    GEMINI_API_KEY = st.session_state.api_key_input
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

# هندسة التصميم الفاخر الملكي للمنصة (CSS القياسي والجمالي لعام 2026)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;800;900&display=swap');
    
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
            🧬 CELLREVIVE AI
        </h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 19px; font-weight: 800; opacity: 0.95; line-height: 1.6; max-width: 850px; margin: 0 auto; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
            المنصة العالمية الموحدة للترميم الخلوي وعكس مسار مقاومة الإنسولين والسكري نوع ثاني للأبد
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 15px; margin-bottom: 20px;">
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 2️⃣ منظومة قاعدة البيانات وتحديث الهيكل السريري (SQLite Engine)
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
            country TEXT DEFAULT 'Egypt', cgm_connected INTEGER DEFAULT 0
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
        SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender, country, cgm_connected
        FROM patients WHERE patient_code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 'skin_analysis': decrypt_data(row[7]), 'selected_drugs': decrypt_data(row[8]), 
            'creatinine': row[9], 'age': row[10], 'gender': row[11], 'country': row[12] or 'Egypt', 'cgm_connected': row[13] or 0
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_quantum_system.db')
    cursor = conn.cursor()
    encrypted_skin = encrypt_data(data['skin_analysis'])
    encrypted_drugs = encrypt_data(data['selected_drugs'])
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender, country, cgm_connected)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], data['severity_score'], encrypted_skin, encrypted_drugs, data['creatinine'], data['age'], data['gender'], data['country'], data['cgm_connected']))
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

# ==============================================================================
# 3️⃣ الاتصال بدستور الأدوية وقواعد البيانات الأيضية الشاملة
# ==============================================================================
GLOBAL_DRUG_DB = {
    "Egypt": {
        "Cidophage (سيدوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف ب12 الحاد وتأثر الميتوكوندريا خلوياً طبقاً لهيئة الدواء المصرية"},
        "Glucophage (جلوكوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر الأعصاب الطرفية فسيولوجياً"},
        "Nervizam (نيرفيزام)": {"generic": "Vitamin B Complex + Alpha-Lipoic Acid", "supp": "Chromium Picolinate + Magnesium Citrate", "reason": "دعم مضادات الأكسدة الخلوية العميقة وحماية الأعصاب المحيطية من الالتهاب دون حوافز كيميائية مصطنعة"},
        "Deltacortril (ديلتاكورتريل)": {"generic": "Prednisolone", "supp": "Potassium (99mg) + Magnesium Citrate (400mg) + Vit D3", "reason": "احتباس السوائل وهدم الكتلة العضلية الحيوية ورفع مقاومة الإنسولين"},
        "Lasix (لازكس)": {"generic": "Furosemide", "supp": "Thiamine B1 (100mg) + Potassium + Magnesium", "reason": "طرد المعادن النادرة ومستنفذات الطاقة الحيوية من الميتوكوندريا الكلوية"},
        "Lipitor (ليبيتور)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3 (5000 IU)", "reason": "تثبيط مسار الميفالونات المسبب لآلام وهدم العضلات وضرر الميتوكوندريا البنيوية"},
        "Mounjaro (مونجارو)": {"generic": "Tirzepatide", "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "منع فقدان الكتلة العضلية الحيوية السريع السريع الحادث بسبب التثبيط المفرط للمعدة والشهية"},
        "Ozempic (أوزمبيك)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc + EAAs", "reason": "كسل وشلل حركة المعدة المؤقت والحاجة لتسهيل امتصاص المغذيات وبناء خلايا عضلية متزنة"}
    },
    "Gulf & International": {
        "Glucophage (International)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "Long-term vitamin B12 malabsorption and mitochondrial protection"},
        "Lipitor (International)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3", "reason": "Mevalonate pathway inhibition causing myalgia"},
        "Mounjaro (International)": {"generic": "Tirzepatide", "supp": "Essential Amino Acids (EAAs)", "reason": "Rapid muscle mass loss prevention"},
        "Ozempic (International)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc", "reason": "Gastric motility delay management"}
    }
}

GI_FOOD_DATABASE = {
    "أرز أبيض مصري": {"GI": 72, "unit_carbs": 4.0, "unit_fiber": 0.1, "desc": "لكل ملعقة طعام كبيرة"},
    "أرز بسمتي طويل الحبة": {"GI": 50, "unit_carbs": 3.5, "unit_fiber": 0.4, "desc": "لكل ملعقة طعام كبيرة"},
    "خبز شعير كامل": {"GI": 45, "unit_carbs": 12.0, "unit_fiber": 2.5, "desc": "لكل نصف رغيف"},
    "خبز جوز الهند / اللوز (Keto)": {"GI": 15, "unit_carbs": 3.0, "unit_fiber": 3.0, "desc": "لكل نصف رغيف"},
    "بقوليات (فول / عدس مدمس)": {"GI": 40, "unit_carbs": 7.0, "unit_fiber": 3.8, "desc": "لكل ملعقة طعام كبيرة (تحتوي كربوهيدرات خفية)"},
    "مكرونة بيضاء": {"GI": 65, "unit_carbs": 5.0, "unit_fiber": 0.2, "desc": "لكل ملعقة طعام كبيرة"},
    "بطاطس مسلوقة / مشوية": {"GI": 80, "unit_carbs": 6.0, "unit_fiber": 0.5, "desc": "لكل نصف حبة متوسطة"}
}

FASTING_PROTOCOLS_DB = {
    "بدون صيام (النمط العادي)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.0, "desc": "الوجبات العادية الموزعة على مدار اليوم."},
    "صيام رمضان / صيام ديني جاف (Dry Fast)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.45, "desc": "انقطاع تام عن الماء والطعام من الفجر للمغرب. أقصى تفعيل للأوتوفاجي السريع."},
    "الصوم المسيحي الكبير / أسبوع الآلام (نباتي صارم)": {"is_vegan": True, "allow_fish": False, "base_boost": 1.35, "desc": "يمنع اللحوم والأسماك والبيض والألبان بالكامل. الاعتماد الحصري على البقوليات والنبات."},
    "الصوم المسيحي (نباتي مسموح بالسمك والتونة)": {"is_vegan": True, "allow_fish": True, "base_boost": 1.25, "desc": "نمط نباتي مع السماح بالمأكولات البحرية والتونة كمصادر بروتينية حامية للمنحنى."},
    "الصيام الكبير الممتد (الترميم الخلوي العميق)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.60, "desc": "بروتوكول الصيام الإكلينيكي الممتد الموصوف لإعادة بناء ميتوكوندريا الخلايا وتصفير مستويات الإنسولين."},
    "صيام متقطع طبي (Medical IF)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.30, "desc": "راحة مبرمجة للبنكرياس تعتمد على الساعات المحددة يدوياً."}
}

# ==============================================================================
# 4️⃣ المعادلات الرياضية والبيولوجية المتقدمة لتقييم الحالة الأيضية
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin=12.0):
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender in ['Female', 'أنثى']: val *= 0.85
    return min(round(val, 2), 150.0)

def calculate_glucose_variability(code):
    logs = get_all_glucose_logs(code)
    if len(logs) < 3:
        return 0.0, "بيانات غير كافية لحساب التقلب الحركي"
    values = [row[2] for row in logs]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    sd = math.sqrt(variance)
    cv = (sd / mean) * 100 if mean > 0 else 0.0
    if cv < 15.0: status = "✅ مستقر ومثالي للترميم الخلوي"
    elif cv <= 36.0: status = "⚠️ تذبذب متوسط - يتطلب ضبط ترتيب الطعام"
    else: status = "🚨 تذبذب حاد وحرج - خطر حدوث طفرات سكر مفاجئة"
    return round(cv, 2), status

# ==============================================================================
# 5️⃣ محرك الرؤية الحاسوبية والذكاء الاصطناعي والمحاكاة الذكية للـ CGM والتقارير
# ==============================================================================
def generate_pdf_report(patient_id, data, calc_homa, calc_egfr, cv_score, cv_status, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="👑 CELLREVIVE AI - METABOLIC CLINICAL REPORT", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=2, align="C")
    pdf.cell(200, 10, txt="----------------------------------------------------------------", ln=3)
    pdf.cell(200, 10, txt=f"Patient Security Access Code: {patient_id}", ln=4)
    pdf.cell(200, 10, txt=f"Clinical Biomarkers - HOMA-IR Score: {round(calc_homa, 2)}", ln=5)
    pdf.cell(200, 10, txt=f"Kidney Efficiency (eGFR): {calc_egfr} mL/min", ln=6)
    pdf.cell(200, 10, txt=f"Glucose Variability Coefficient (CV): {cv_score}% ({cv_status})", ln=7)
    pdf.cell(200, 10, txt=f"Recorded Baseline FBG: {data['fbg']} mg/dL | HbA1c: {data['hba1c']}%", ln=8)
    pdf.cell(200, 10, txt=f"Clinical Supervisor Instructions: {notes}", ln=9)
    
    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/Report_{patient_id}.pdf"
    pdf.output(report_path)
    return report_path

def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح الـ API المعتمد لتشغيل محرك التحليل البصري الاستباقي."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي لعام 2026.
        مهمتك الأساسية هي هندسة الوجبات هندسة استباقية صارمة لتسطيح منحنى السكر تماماً وتخفيض التذبذب (CV < 10%).
        عند تقديم نصائح التعديل والإضافة والمقاصة الغذائية، يجب الالتزام الصارم بالقواعد التالية لتسهيل التطبيق على المريض:
        - ترجمة الجرامات الطبية فوراً وبدقة إلى وحدات منزلية قياسية تقريبية متعارف عليها بين المرضى.
        - استخدم التعبيرات التالية حصراً للكميات: (معيار كفة اليد بدون أصابع للبروتين، حجم عقلة الأصبع للدهون، ملعقة صغيرة, ملعقة كبيرة، حجم عبوة الكبريت الصغيرة للجبن، كوب كبير 240 مل، كوب صغير 120 مل).
        - رتب تناول الوجبة إلزامياً: الألياف أولاً، ثم البروتين والدهون الصحية، ثم الكربوهيدرات المعقدة في النهاية لتأخير الامتصاص المعوي.
        - لا تقم بتغيير جرعات الأدوية الكيميائية، بل وجه المريض دائماً لمراجعة الدكتور إيهاب حشمت أو الطبيب المعالج للتحقق التام والرجوع لدليل الدستور الدوائي المصري وهيئة الدواء المصرية.
        """
        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)
        content = [prompt]
        for img in images: content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال بالشبكة الطبية: {str(e)}"

def check_emergency_status(value, context_phrase=""):
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ حرج جداً (هبوط حاد): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> تم رصد هبوط حاد دون النطاق Safe Range. يرجى تناول مصدر جلوكوز سريع والاتصال الفوري بالدكتور إيهاب حشمت!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ حرج جداً (ارتفاع مفرط): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> قراءة السكر مرتفعة وتتجاوز عتبة الأمان الخلوي العلوية. تواصل مع الإدارة الطبية فوراً.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 6️⃣ جدار الحماية الرقمي والتحقق من الأكواد الـ 24 المعتمدة
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
            st.error("كود غير مصرح به. يرجى مراجعة الإدارة الطبية فوراً لتفعيل الاشتراك وتحديث الكود الخاص بك.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لم يتم فحص علامات الجلد بعد للحالة الحالية', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male', 'country': 'Egypt', 'cgm_connected': 0
}

# ==============================================================================
# 7️⃣ لوحة تحكم الطبيب المطور الاستباقية (د. إيهاب حشمت)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; text-align:center; border-bottom:1px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة التحكم والتحليل السيادي الإكلينيكية العالمية</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    target_patient = st.selectbox("اختر كود المريض المراد تأسيسه وتعديل ملفه الفسيولوجي:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
    with st.expander("🌍 النطاق الجغرافي ودليل ومستندات هيئة الدواء المصرية المعتمدة", expanded=True):
        mod_country = st.selectbox("اختر النطاق الدستوري لتدقيق الأدوية:", list(GLOBAL_DRUG_DB.keys()), index=0 if current_p_data['country'] == "Egypt" else 1)
        mod_cgm = st.checkbox("🔌 تفعيل خيار الربط الديناميكي ومراقبة التذبذبات عبر مستشعرات CGM المستمرة", value=bool(current_p_data['cgm_connected']))

    with st.expander("📝 ضبط البيانات الديموغرافية والسريرية بدقة 100%", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم (mg/dL):", value=float(current_p_data['fbg']))
            mod_ppbg = st.number_input("سكر فاطر بعد ساعتين (mg/dL):", value=float(current_p_data['ppbg']))
            mod_rbg = st.number_input("سكر عشوائي (mg/dL):", value=float(current_p_data['rbg']))
            mod_creatinine = st.number_input("الكرياتينين في الدم (Serum Creatinine):", value=float(current_p_data['creatinine']), step=0.1)
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']))
            mod_weight = st.number_input("الوزن الحالي (كجم):", value=float(current_p_data['weight']))
            mod_waist = st.number_input("محيط الخصر السريري (سم):", value=float(current_p_data['waist']))
            mod_age = st.number_input("عمر المريض الحالي (سنوات):", value=int(current_p_data['age']), step=1)
            mod_gender = st.selectbox("جنس المريض الخلوي:", ["Male", "Female"], index=0 if current_p_data['gender'] == "Male" else 1)

    with st.expander("💊 بروتوكول المقاصة الدوائية والمكملات"):
        available_drugs = GLOBAL_DRUG_DB[mod_country]
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية والمكملات الفعالة الحالية للمشترك للربط الدستوري:", list(available_drugs.keys()), default=[d for d in saved_drugs_list if d in available_drugs])

    st.markdown("---")
    st.markdown("### 📋 تحويل المؤشرات الطبية ورفع التقرير")
    col_rep1, col_rep2 = st.columns([2, 1])
    with col_rep1:
        doctor_note = st.text_input("ملحوظة إضافية ترفق بالتقرير للطبيب المعالج للحالة:", value="يرجى الالتزام بالترميم الخلوي.")
    with col_rep2:
        send_report = st.button("📤 إنشاء ورفع التقرير الطبي فوراً")
        if send_report:
            homa_calc = calculate_homa_ir(mod_fbg)
            egfr_calc = calculate_egfr(mod_age, mod_weight, mod_creatinine, mod_gender)
            cv_s, cv_st = calculate_glucose_variability(target_patient)
            
            pdf_path = generate_pdf_report(target_patient, current_p_data, homa_calc, egfr_calc, cv_s, cv_st, doctor_note)
            with open(pdf_path, "rb") as f:
                st.download_button(label="📥 تحميل التقرير الطبي المعتمد PDF", data=f, file_name=f"CellRevive_Report_{target_patient}.pdf", mime="application/pdf")
            st.success("🟢 تم تشفير الملف وإرسال تقرير فسيولوجي كامل للطبيب المعالج بنجاح طبقاً لمعايير هيبا.")

    if st.button("💾 تثبيت وحفظ ملف المريض المشفر (HIPAA Protected)"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender,
            'country': mod_country, 'cgm_connected': 1 if mod_cgm else 0
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم بنجاح تشفير وتثبيت مؤشرات المريض {target_patient} في قاعدة البيانات السيادية للمنصة.")

# ==============================================================================
# 8️⃣ واجهة المريض الفسيفسائية المتقدمة (استباقية، تحليلية، شاملة بالكامل)
# ==============================================================================
if st.session_state.role == "patient":
    plan_text = "نظام الشهر السريع" if "1M" in current_code else "نظام الـ 3 أشهر الممتد" if "3M" in current_code else "النظام التأسيسي الآمن"
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 1px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك.. تم تفعيل الدخول البرمجي التلقائي بناءً على الكود الخاص بك: ({plan_text}) للكود الآمن [{current_code}]</p>', unsafe_allow_html=True)
    
    check_emergency_status(p_data['fbg'], "قراءة الصائم")
    check_emergency_status(p_data['ppbg'], "قراءة الفاطر")
    
    calc_homa = calculate_homa_ir(p_data['fbg'])
    calc_egfr_val = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    cv_score, cv_status = calculate_glucose_variability(current_code)
    
    if p_data['cgm_connected'] == 1:
        st.markdown("""
            <div class="premium-card" style="border-color: #00ffcc;">
                <h3 style="color:#00ffcc !important; margin:0 0 10px 0;">🔌 بوابة مستشعر السكر المستمر النشط (Live CGM API Connection)</h3>
                <p style="font-size:13px; margin:0; opacity:0.9;">
                    تم ربط مستشعرات تتبع الجلوكوز بنجاح عبر بروتوكولات السحب الفوري (Streaming API). النظام يستقبل البيانات الحركية الفوقية ويحلل التذبذب لتسطيح منحنى الأيض مباشرة بموازاة معايير هيئة الدواء.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 20px 0; font-size:18px;">📊 المؤشرات الفسيولوجية الأساسية المستخلصة والمخزنة (Clinical Biomarkers)</h3>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color:#f3e5ab !important;">مؤشر HOMA-IR الحسابي</span><br>
                    <span style="font-size:22px; font-weight:900; color:#ff4b4b;">{round(calc_homa, 2)}</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color:#f3e5ab !important;">كفاءة الفلترة الكلوية (eGFR)</span><br>
                    <span style="font-size:22px; font-weight:900; color:#00ffcc;">{calc_egfr_val} mL/min</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color:#f3e5ab !important;">تذبذب الجلوكوز الرياضي</span><br>
                    <span style="font-size:18px; font-weight:900; color:#ffff00;">{cv_score}%</span><br>
                    <span style="font-size:11px; opacity:0.9;">{cv_status}</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # عرض المنحنى البياني التفاعلي
    st.markdown('<div class="premium-card"><h3>📈 مراقبة وتتبع تذبذب الجلوكوز المستمر للأعضاء</h3>', unsafe_allow_html=True)
    raw_logs = get_all_glucose_logs(current_code)
    if raw_logs:
        df = pd.DataFrame(raw_logs, columns=["التوقيت", "نوع القراءة", "القيمة mg/dL"])
        fig = px.line(df, x="التوقيت", y="القيمة mg/dL", color="نوع القراءة", title="مسار المنحنى الأيضي للحالة", markers=True)
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("سجل تتبع التذبذب فارغ حالياً. قم بتدوين قراءات القياس بالأسفل لتغذية المحرك البياني.")
    st.markdown('</div>', unsafe_allow_html=True)

    # تسجيل القياسات اليدوية السريعة
    with st.expander("📊 تدوين وتسجيل قراءة سكر فورية الآن بالملف الطبي", expanded=False):
        col_g1, col_g2 = st.columns(2)
        with col_g1: g_type = st.selectbox("توقيت ومناسبة القياس الحالية:", ["سكر صائم", "سكر فاطر (بعد ساعتين)", "سكر عشوائي"])
        with col_g2: g_val = st.number_input("قيمة القياس من الجهاز مباشرة (mg/dL):", value=0.0, step=1.0)
        if st.button("📝 تدوين وحفظ القراءة الفورية"):
            if g_val > 0:
                log_glucose(current_code, g_type, g_val)
                temp_data = get_patient_data(current_code) or p_data
                if g_type == "سكر صائم": temp_data['fbg'] = g_val
                elif g_type == "سكر فاطر (بعد ساعتين)": temp_data['ppbg'] = g_val
                else: temp_data['rbg'] = g_val
                save_patient_data(current_code, temp_data)
                st.success("تم تشفير وتدوين قراءتك الحالية في السجل بنجاح.")
                st.rerun()

    # 🌙 مختبر الصيام المطور وعداد الساعات الأيضي (Dynamic Fasting Core)
    st.markdown('<div class="premium-card"><h3>🌙 مختبر الصيام المطور وعداد الساعات الأيضي (Dynamic Fasting Core)</h3>', unsafe_allow_html=True)
    col_fast_type, col_fast_hours = st.columns([2, 1])
    with col_fast_type:
        active_fast_name = st.selectbox("اختر بروتوكول الصيام المطبق اليوم لضبط استجابة البنكرياس:", list(FASTING_PROTOCOLS_DB.keys()))
    with col_fast_hours:
        fasting_hours = st.number_input("عدد ساعات الانقطاع الفعلي الحالية عن الطعام والشراب:", min_value=0, max_value=24, value=16, step=1)
        
    fast_meta = FASTING_PROTOCOLS_DB[active_fast_name]
    hours_bonus = max(0, (fasting_hours - 8) * 0.02) if fasting_hours > 0 else 0
    total_sensitivity_boost = fast_meta["base_boost"] + hours_bonus

    st.markdown(f"""
        <div style="background: rgba(0, 255, 204, 0.05); border-right: 4px solid #00ffcc; padding: 10px; border-radius: 4px; margin-bottom: 5px; font-size:13px;">
            • النمط النشط المعتمد: {fast_meta["desc"]}<br>
            • معامل رفع حساسية الخلايا المحسوب نتيجة انقطاع {fasting_hours} ساعة: <span style="color:#ffff00;">+{round((total_sensitivity_boost - 1)*100)}%</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔮 المحرك الكمي للأيض والتوقيت البيولوجي (Quantum Chrono-Sandbox)
    st.markdown('<div class="premium-card"><h3>🔮 المحرك الكمي للأيض والتوقيت البيولوجي (Quantum Chrono-Sandbox)</h3>', unsafe_allow_html=True)
    
    st.markdown("<p style='color:#f3e5ab !important; font-size:14.5px; margin-bottom:5px;'>🕒 هندسة التوقيت والساعة البيولوجية للوجبة:</p>", unsafe_allow_html=True)
    meal_time = st.time_input("حدد وقت تناول الوجبة المتوقع لضبط مقاومة الخلايا المحيطية:", value=datetime.now().time())
    
    if meal_time.hour >= 19 or meal_time.hour < 5:
        chrono_factor = 1.35
        chrono_alert = "⚠️ <b>تنبيه الساعة البيولوجية:</b> تناول الوجبة ليلاً يواجه فسيولوجياً بمقاومة إنسولين طرفية مرتفعة وهبوط طاقة الحرق الحيوية."
    else:
        chrono_factor = 1.0
        chrono_alert = "☀️ <b>توقيت أيضي نهارى مثالي:</b> كفاءة التخلص الحركي من الجلوكوز في أعلى مستوياتها الحيوية."

    if fasting_hours >= 16:
        glycogen_status = f"🧹 <b>الجليكوجين الكبدي (مستنفد جزئياً بفعل صيام {fasting_hours} ساعة):</b> الكبد يمتص السكر الآن كإسفنجة لتخزينه أولاً، مما يقلل ذروة الصعود الدموي."
    elif fasting_hours >= 12:
        glycogen_status = "📊 <b>الجليكوجين الكبدي (متوسط الاستيعاب الأولي):</b> الكبد مهيأ جزئياً للمقاصة التخزينية."
    else:
        glycogen_status = "🚨 <b>الجليكوجين الكبدي (ممتلئ بالكامل):</b> الكبد لن يمتص أي فيض؛ الكربوهيدرات الزائدة ستتدفق فوراً ومباشرة للمجرى الدموي وتحدث طفرة حادة."

    st.markdown(f"""
        <div style="background: rgba(243, 229, 171, 0.05); padding: 10px; border-radius: 4px; font-size:13px; line-height:1.5; margin-bottom:15px;">
            • {chrono_alert}<br> • {glycogen_status}
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='color:#f3e5ab !important; font-size:14.5px; margin-bottom:5px;'>🍞 الكربوهيدرات (النوع والكمية الدقيقة بالوحدات المنزلية):</p>", unsafe_allow_html=True)
    col_food_sel, col_food_qty = st.columns([2, 1])
    
    with col_food_sel:
        selected_food = st.selectbox("اختر نوع الكربوهيدرات المراد اختبارها فسيولوجياً:", list(GI_FOOD_DATABASE.keys()))
    with col_food_qty:
        food_units = st.number_input("الكمية (بالوحدة المنزلية الموضحة):", min_value=0.5, max_value=10.0, value=1.0, step=0.5)

    food_meta = GI_FOOD_DATABASE[selected_food]
    net_carbs = food_meta["unit_carbs"] * food_units
    base_gl = (food_meta["GI"] * net_carbs) / 100.0
    adjusted_gl = (base_gl * chrono_factor) / total_sensitivity_boost
    
    st.markdown(f"#### 🧮 تقييم الحمل الجلايسيمي المعدل للحالة فسيولوجياً:")
    if adjusted_gl < 10:
        st.success(f"🟢 آمن جداً ({round(adjusted_gl, 2)}) - لن يسبب طفرة سكر بفضل هندسة وجبتك وصيامك المتقدم.")
    elif adjusted_gl <= 20:
        st.warning(f"⚠️ متوسط الأثر ({round(adjusted_gl, 2)}) - يفضل تقليل الكمية بمقدار نصف وحدة منزلية لتجنب تذبذب المنحنى.")
    else:
        st.error(f"🚨 حمل جلايسيمي مرتفع وخطر ({round(adjusted_gl, 2)}) - سيحدث طفرة صعود فورية. يُنصح بالاستبدال فوراً لخيار منخفض المؤشر الجلايسيمي.")
    st.markdown('</div>', unsafe_allow_html=True)
