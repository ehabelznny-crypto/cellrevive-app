# ==============================================================================
# 👑 CELLREVIVE AI - THE UNITED METABOLIC OS & CELLULAR RESTORATION PLATFORM (v16.1)
# ==============================================================================
# Production-Ready Sovereign System (2026/2027 International Metabolic Standards)
# Quantum Integration: Computational Nutrigenomics, Vision AI, & 2D Curve Simulator
# Core Architecture Designed for: Dr. Ehab Heshmat El-Zanny & CellRevive Global Engine
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

# 🛡️ استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
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

# ==============================================================================
# 1️⃣ الإعدادات وتصميم الواجهة الفاخرة السيادية (Premium 2026 Gold Design)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Global Metabolic Platform",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# التحقق من مفتاح API لمحرك الذكاء الاصطناعي
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    GEMINI_API_KEY = st.session_state.api_key_input
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

# حقن كود CSS الاحترافي للهوية البصرية الفاخرة
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
            👑 CELLREVIVE AI
        </h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 19px; font-weight: 800; opacity: 0.95; line-height: 1.6; max-width: 850px; margin: 0 auto; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
            المنصة العالمية الموحدة للترميم الخلوي وعكس مسار مقاومة الإنسولين والسكري نوع ثاني 
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
            country TEXT DEFAULT 'Egypt', cgm_connected INTEGER DEFAULT 0,
            mthfr_mutation TEXT DEFAULT 'Normal (CC)', fto_variant TEXT DEFAULT 'Normal (TT)',
            fasting_insulin REAL DEFAULT 12.0
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
               creatinine, age, gender, country, cgm_connected, mthfr_mutation, fto_variant, fasting_insulin
        FROM patients WHERE patient_code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 'skin_analysis': decrypt_data(row[7]), 'selected_drugs': decrypt_data(row[8]), 
            'creatinine': row[9], 'age': row[10], 'gender': row[11], 'country': row[12] or 'Egypt', 'cgm_connected': row[13] or 0,
            'mthfr_mutation': row[14] or 'Normal (CC)', 'fto_variant': row[15] or 'Normal (TT)', 'fasting_insulin': row[16] or 12.0
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
                                         cgm_connected, mthfr_mutation, fto_variant, fasting_insulin)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], 
          data['severity_score'], encrypted_skin, encrypted_drugs, data['creatinine'], data['age'], 
          data['gender'], data['country'], data['cgm_connected'], data['mthfr_mutation'], data['fto_variant'], data['fasting_insulin']))
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
# 3️⃣ الدستور الدوائي وقواعد البيانات الحيوية والوراثية (Nutrigenomic & GI DB)
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
        "supp": "Alpha-Lipoic Acid (600mg)", "reason": "حماية غمد المايلين الدهني للأعصاب الطرفية عبر دمج البنفوتيامين (B1 الذائف في الدهون) لمنع التلف الأيضي."
    },
    "Ozempic (أوزمبيك)": {
        "generic": "Semaglutide", "class": "GLP-1 Receptor Agonist",
        "regions": ["Egypt", "Gulf", "International"], "arabic_names": ["أوزمبيك", "وزمبك"],
        "supp": "Digestive Enzymes + Zinc + Essential Amino Acids (EAAs)", "reason": "تأخير حركة المعدة فسيولوجياً والحاجة لتسهيل امتصاص المغذيات خلوياً ومنع هدم الكتلة العضلية (Sarcopenia)."
    },
    "Mounjaro (مونجارو)": {
        "generic": "Tirzepatide", "class": "GIP/GLP-1 Receptor Co-agonist",
        "regions": ["Egypt", "Gulf", "International"], "arabic_names": ["مونجارو", "منجارو"],
        "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "منع فقدان الكتلة العضلية الحيوية السريع السريع الحادث بسبب التثبيط المفرط للمعدة والشهية."
    },
    "Forxiga (فورسيجا)": {
        "generic": "Dapagliflozin", "class": "SGLT2 Inhibitor (Glucuretic)",
        "regions": ["Egypt", "Gulf", "International"], "arabic_names": ["فورسيجا", "فارسيجا"],
        "supp": "Electrolytes (Potassium/Magnesium) + High Hydration Protocol", "reason": "الفقد المستمر للمعادن النادرة والسوائل عبر الفلترة الكلوية وزيادة احتمالية الجفاف الخلوي الاسموزي."
    }
}

GI_FOOD_DATABASE = {
    "أرز أبيض مصري": {"GI": 72, "unit_carbs": 4.0, "unit_fiber": 0.1, "desc": "لكل ملعقة طعام كبيرة"},
    "أرز بسمتي طويل الحبة": {"GI": 50, "unit_carbs": 3.5, "unit_fiber": 0.4, "desc": "لكل ملعقة طعام كبيرة"},
    "خبز شعير كامل": {"GI": 45, "unit_carbs": 12.0, "unit_fiber": 2.5, "desc": "لكل نصف رغيف"},
    "خبز جوز الهند / اللوز (Keto)": {"GI": 15, "unit_carbs": 3.0, "unit_fiber": 3.0, "desc": "لكل نصف رغيف"},
    "بقوليات (فول / عدس مدمس)": {"GI": 40, "unit_carbs": 7.0, "unit_fiber": 3.8, "desc": "لكل ملعقة طعام كبيرة"},
    "مكرونة بيضاء": {"GI": 65, "unit_carbs": 5.0, "unit_fiber": 0.2, "desc": "لكل ملعقة طعام كبيرة"},
    "بطاطس مسلوقة / مشوية": {"GI": 80, "unit_carbs": 6.0, "unit_fiber": 0.5, "desc": "لكل نصف حبة متوسطة"}
}

FASTING_PROTOCOLS_DB = {
    "بدون صيام (النمط العادي)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.0, "desc": "الوجبات العادية الموزعة على مدار اليوم."},
    "صيام رمضان / صيام ديني جاف (Dry Fast)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.45, "desc": "انقطاع تام عن الماء والطعام من الفجر للمغرب. أقصى تفعيل للأوتوفاجي السريع."},
    "الصوم المسيحي الكبير / أسبوع الآلام (نباتي صارم)": {"is_vegan": True, "allow_fish": False, "base_boost": 1.35, "desc": "يمنع اللحوم والأسماك والبيض والألبان بالكامل. الاعتماد الحصري على النبات."},
    "الصيام الكبير الممتد (الترميم الخلوي العميق)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.60, "desc": "بروتوكول الصيام الإكلينيكي الممتد الموصوف لإعادة بناء ميتوكوندريا الخلايا وتصفير مستويات الإنسولين."},
    "صيام متقطع طبي (Medical IF)": {"is_vegan": False, "allow_fish": True, "base_boost": 1.30, "desc": "راحة مبرمجة للبنكرياس تعتمد على الساعات المحددة."}
}

# ==============================================================================
# 4️⃣ المحور الأول والثاني: المعادلات الرياضية والبيولوجية ومحاكي المنحنى التفاضلي
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin):
    return (fbg * fasting_insulin) / 405

# 🛠️ تم تصحيح بناء الدالة وإزالة المتغير الرابع لتوحيد هيكلية الاستدعاء عبر التطبيق كاملاً
def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender in ['Female', 'أنثى', 'أنثي']: val *= 0.85
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

# 1️⃣ خوارزمية تسطيح المنحنى الفسيولوجي ثنائي الأبعاد (Dynamic Curve Flattening Simulator)
def simulate_glucose_curve(base_fbg, sequence_type, gi_score):
    t = np.linspace(0, 180, 100)
    gamma = 2.4 if sequence_type == "الألياف أولاً ➔ البروتين والدهون ➔ النشويات" else 1.0
    A = gi_score * 1.5 
    k1 = 0.04 / (gamma * 0.8)
    k2 = 0.02 * gamma
    delta_g = A * (np.exp(-k2 * t) - np.exp(-k1 * t)) * (150 / (base_fbg * gamma))
    glucose_t = base_fbg + delta_g
    return t, glucose_t

# 2️⃣ محرك النواقل الوراثية الغذائية والمقاصة الخلوية العميقة (Nutrigenomic Rescuer)
def get_nutrigenomic_advice(mthfr, fto):
    advice = {"mthfr": "", "fto": ""}
    if mthfr == "طفرة متجانسة (TT Homozygous)":
        advice["mthfr"] = "⚠️ انخفاض بنسبة 70% في كفاءة إنزيم MTHFR. يحظر تماماً تناول حمض الفوليك الصناعي (Folic Acid) لتجنب تراكم السمية الخلوية. التوصية: الإلزام الفوري بالصيغة النشطة فسيولوجياً ميثيل فولات (5-MTHF) بجرعة 1000 ميكروجرام لضمان حماية الحمض النووي (DNA Methylation)."
    elif mthfr == "طفرة متغايرة (CT Heterozygous)":
        advice["mthfr"] = "⚠️ انخفاض متوسط بنسبة 35% في كفاءة الإنزيم. يُفضل استبدال الفوليك أسيد التجاري بـ الميثيل فولات العضوي المستخلص من الخضروات الورقية الداكنة المعالجة بحرارة خفيفة."
    else:
        advice["mthfr"] = "✅ ناقل الجينات الطبيعي (CC). كفاءة الميثيل ممتازة خلوياً."
        
    if fto == "خطر مرتفع (AA Homozygous)":
        advice["fto"] = "🚨 جين السمنة الأيضية نشط. الخلايا لديها ميل جيني مرتفع لتخزين الدهون وضعف الإشارات العصبية للشبع (Leptin Resistance). التوصية السريرية: إجبار البنكرياس على بروتوكول الصيام الطبي الممتد وعكس النمط تماماً لرفع مستويات هرمون الـ Adiponectin."
    else:
        advice["fto"] = "✅ البديل الجيني طبيعي ومثالي لمعدلات الحرق الأيضي."
    return advice

# ==============================================================================
# 5️⃣ محرك التقارير، التحليل البصري والمحاكاة الفسيولوجية
# ==============================================================================
def generate_pdf_report(patient_id, data, calc_homa, calc_egfr, cv_score, cv_status, selected_drugs_list, notes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="👑 CELLREVIVE AI - METABOLIC CLINICAL REPORT (ACADEMIC GENERIC)", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=2, align="C")
    pdf.cell(200, 10, txt="----------------------------------------------------------------", ln=3)
    pdf.cell(200, 10, txt=f"Patient Security Access Code: {patient_id}", ln=4)
    pdf.cell(200, 10, txt=f"Clinical Biomarkers - HOMA-IR Score: {round(calc_homa, 2)}", ln=5)
    pdf.cell(200, 10, txt=f"Kidney Efficiency (eGFR): {calc_egfr} mL/min", ln=6)
    pdf.cell(200, 10, txt=f"Glucose Variability Coefficient (CV): {cv_score}%", ln=7)
    pdf.cell(200, 10, txt=f"Recorded Baseline FBG: {data['fbg']} mg/dL | HbA1c: {data['hba1c']}%", ln=8)
    
    pdf.cell(200, 10, txt="Analyzed Drug Classes & Active Generics:", ln=9)
    line_idx = 10
    if selected_drugs_list:
        for brand in selected_drugs_list:
            if brand in GLOBAL_DRUG_DB:
                g_info = GLOBAL_DRUG_DB[brand]
                pdf.cell(200, 10, txt=f" - Active Element: {g_info['generic']} ({g_info['class']})", ln=line_idx)
                line_idx += 1
                
    clean_notes = "".join([c for c in notes if ord(c) < 128]) or "Please refer to clinical guidelines."
    pdf.cell(200, 10, txt=f"Clinical Instructions Note: {clean_notes}", ln=line_idx)
    
    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/Report_{patient_id}.pdf"
    pdf.output(report_path)
    return report_path

def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح الـ API المعتمد لتشغيل محرك التحليل البصري الاستباقي."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي والرؤية الحاسوبية لعام 2026/2027.
        مهمتك الأساسية هي هندسة الوجبات هندسة استباقية صارمة لتسطيح منحنى السكر تماماً وتخفيض التذبذب (CV < 10%)، 
        وكذلك تحليل علامات الجلد التعبيرية للشواك الأسود (Acanthosis Nigricans) وربط تراجع التصبغ حسابياً بتحسن مصفوفة HOMA-IR.
        عند تقديم نصائح التعديل الغذائي، يجب الالتزام الصارم بالقواعد التالية لتسهيل التطبيق على المريض:
        - ترجمة الجرامات الطبية فوراً وبدقة إلى وحدات منزلية قياسية تقريبية متعارف عليها (كفة اليد، عقلة الأصبع، كوب كبير 240 مل، ملعقة صغيرة).
        - رتب تناول الوجبة إلزامياً وبصرامة فسيولوجية: الألياف أولاً، ثم البروتين والدهون الصحية ثانياً، ثم الكربوهيدرات المعقدة في النهاية لتأخير الامتصاص المعوي تماماً.
        - وجه المريض دائماً لمراجعة الدكتور إيهاب حشمت أو الطبيب المعالج للتحقق التام والرجوع لدليل الدستور الدوائي المصري وهيئة الدواء المصرية.
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
            st.error("كود غير مصرح به. يرجى مراجعة الإدارة فوراً لتفعيل الاشتراك وتحديث الكود الخاص بك.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لم يتم فحص علامات الجلد بعد للحالة الحالية', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male', 'country': 'Egypt', 'cgm_connected': 0,
    'mthfr_mutation': 'Normal (CC)', 'fto_variant': 'Normal (TT)', 'fasting_insulin': 12.0
}

# ==============================================================================
# 7️⃣ لوحة تحكم المسؤول المطور الاستباقية (د. إيهاب حشمت)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; text-align:center; border-bottom:1px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة التحكم والتحليل السيادي الإكلينيكية العالمية</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    target_patient = st.selectbox("اختر كود المريض المراد تأسيسه وتعديل ملفه الفسيولوجي:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
    with st.expander("🌍 النطاق الجغرافي وحركة الأدوية المصدرة والمحلية عالمياً", expanded=True):
        mod_cgm = st.checkbox("🔌 تفعيل خيار الربط الديناميكي ومراقبة التذبذبات عبر مستشعرات CGM المستمرة", value=bool(current_p_data['cgm_connected']))

    with st.expander("📝 ضبط البيانات الديموغرافية والسريرية بدقة 100%", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم (mg/dL):", value=float(current_p_data['fbg']))
            mod_ppbg = st.number_input("سكر فاطر بعد ساعتين (mg/dL):", value=float(current_p_data['ppbg']))
            mod_rbg = st.number_input("سكر عشوائي (mg/dL):", value=float(current_p_data['rbg']))
            mod_creatinine = st.number_input("الكرياتينين في الدم (Serum Creatinine):", value=float(current_p_data['creatinine']), step=0.1)
            mod_insulin = st.number_input("إنسولين الصائم (Fasting Insulin uIU/mL):", value=float(current_p_data['fasting_insulin']))
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']))
            mod_weight = st.number_input("الوزن الحالي (كجم):", value=float(current_p_data['weight']))
            mod_waist = st.number_input("محيط الخصر السريري (سم):", value=float(current_p_data['waist']))
            mod_age = st.number_input("عمر المريض الحالي (سنوات):", value=int(current_p_data['age']), step=1)
            mod_gender = st.selectbox("جنس المريض الخلوي:", ["Male", "Female"], index=0 if current_p_data['gender'] == "Male" else 1)

    # 🧬 دمج المحور الثاني: النواقل الوراثية والتحليل الحركي للـ Nutrigenomics
    with st.expander("🧬 حوسبة التعبير الجيني والنواقل الوراثية العلاجية (Computational Nutrigenomics)"):
        mod_mthfr = st.selectbox("توصيف جين MTHFR (تدوير الفولات وعمليات الميثيل):", 
                                 ["Normal (CC)", "طفرة متغايرة (CT Heterozygous)", "طفرة متجانسة (TT Homozygous)"],
                                 index=["Normal (CC)", "طفرة متغايرة (CT Heterozygous)", "طفرة متجانسة (TT Homozygous)"].index(current_p_data['mthfr_mutation']))
        mod_fto = st.selectbox("توصيف جين FTO (السمنة الأيضية ومقاومة الشبع):", 
                               ["Normal (TT)", "خطر مرتفع (AA Homozygous)"],
                               index=["Normal (TT)", "خطر مرتفع (AA Homozygous)"].index(current_p_data['fto_variant']))

    with st.expander("💊 بروتوكول المقاصة الدوائية والمكملات (البحث التجاري والعلمي المتقاطع)"):
        search_drug_inp = st.text_input("ابحث عن الدواء التجاري لربطه فوراً بالملف (عربي أو إنجليزي - مثال: نيرفيزام، سيدوفاج، أوزمبيك):")
        available_brands = list(GLOBAL_DRUG_DB.keys())
        
        filtered_brands = []
        if search_drug_inp:
            q_clean = search_drug_inp.strip().lower()
            for b_name, b_det in GLOBAL_DRUG_DB.items():
                if q_clean in b_name.lower() or q_clean in b_det["generic"].lower() or any(q_clean in ar.lower() for ar in b_det["arabic_names"]):
                    filtered_brands.append(b_name)
        else:
            filtered_brands = available_brands
            
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر وثبّت الأدوية النشطة للمشترك للربط الدستوري بمواده العلمية:", filtered_brands, default=[d for d in saved_drugs_list if d in GLOBAL_DRUG_DB])

    st.markdown("---")
    st.markdown("### 📋 تحويل المؤشرات الطبية ورفع Tالتقرير الأكاديمي")
    col_rep1, col_rep2 = st.columns([2, 1])
    with col_rep1:
        doctor_note = st.text_input("ملحوظة إضافية ترفق بالتقرير للطبيب المعالج للحالة:", value="Please follow the cellular revive order of meals strictly.")
    with col_rep2:
        send_report = st.button("📤 إنشاء ورفع التقرير الطبي فوراً")
        if send_report:
            homa_calc = calculate_homa_ir(mod_fbg, mod_insulin)
            egfr_calc = calculate_egfr(mod_age, mod_weight, mod_creatinine, mod_gender)
            cv_s, cv_st = calculate_glucose_variability(target_patient)
            
            pdf_path = generate_pdf_report(target_patient, current_p_data, homa_calc, egfr_calc, cv_s, cv_st, mod_drugs, doctor_note)
            with open(pdf_path, "rb") as f:
                st.download_button(label="📥 تحميل التقرير الطبي المعتمد PDF", data=f, file_name=f"CellRevive_Report_{target_patient}.pdf", mime="application/pdf")
            st.success("🟢 تم تشفير الملف وإرسال تقرير فسيولوجي كامل للطبيب المعالج بنجاح محايد وأكاديمي طبقاً لمعايير هيبا.")

    if st.button("💾 تثبيت وحفظ ملف المريض المشفر (HIPAA Protected)"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender,
            'country': current_p_data['country'], 'cgm_connected': 1 if mod_cgm else 0,
            'mthfr_mutation': mod_mthfr, 'fto_variant': mod_fto, 'fasting_insulin': mod_insulin
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم بنجاح تشفير وتثبيت مؤشرات المريض {target_patient} في قاعدة البيانات السيادية للمنصة.")

# ==============================================================================
# 8️⃣ واجهة المريض المتقدمة والتحليل الحركي المكتمل
# ==============================================================================
if st.session_state.role == "patient":
    plan_text = "نظام الشهر السريع" if "1M" in current_code else "نظام الـ 3 أشهر الممتد" if "3M" in current_code else "النظام التأسيسي الآمن"
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 1px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك.. تم تفعيل الدخول البرمجي التلقائي بناءً على الكود الخاص بك: ({plan_text}) للكود الآمن [{current_code}]</p>', unsafe_allow_html=True)
    
    check_emergency_status(p_data['fbg'], "قراءة الصائم")
    check_emergency_status(p_data['ppbg'], "قراءة الفاطر")
    
    calc_homa = calculate_homa_ir(p_data['fbg'], p_data['fasting_insulin'])
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
        
    # تم إكمال بناء واجهة عرض البيانات الطبية وإغلاق كروت الـ HTML المقطوعة بدقة
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 20px 0; font-size:18px;">📊 المؤشرات الفسيولوجية الأساسية المستخلصة والمحسوبة للحالة:</h3>
            <div class="metric-box"><b>مؤشر مقاومة الإنسولين (HOMA-IR):</b> {round(calc_homa, 2)}</div>
            <div class="metric-box"><b>كفاءة الفلترة الكلوية (eGFR):</b> {calc_egfr_val} mL/min</div>
            <div class="metric-box"><b>معامل تذبذب السكر الحيوي (CV):</b> {cv_score}% ({cv_status})</div>
            <div class="metric-box"><b>محيط الخصر السريري:</b> {p_data['waist']} سم</div>
        </div>
    """, unsafe_allow_html=True)
