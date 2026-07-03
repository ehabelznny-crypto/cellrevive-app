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

# ==============================================================================
# 1️⃣ الإعدادات المتقدمة والهوية البصرية الملكية الفاخرة (Sovereign Gold Theme)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Global Sovereign Engine",
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

# هندسة التصميم الفاخر بالـ CSS باللون الذهبي الملكي والخلفية العميقة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;800;900&display=swap');
    
    .stApp { 
        background-color: #030914; 
        color: #ffffff !important;
        font-family: 'Cairo', sans-serif !important;
    }
    [data-testid="stMainBlockContainer"] { 
        direction: rtl !important; 
        text-align: right !important; 
    }
    .premium-card {
        background: linear-gradient(145deg, #091930, #051020);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(212, 175, 55, 0.15);
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
    label, p, span, h3 { 
        color: #ffffff !important; 
        font-weight: 600 !important; 
    }
    .stButton>button {
        background: linear-gradient(90deg, #f3e5ab, #d4af37, #aa8422);
        color: #030914 !important;
        border-radius: 12px !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        height: 3.2em;
        width: 100%;
        border: none;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
    }
    .metric-box { 
        border-right: 4px solid #d4af37; 
        padding-right: 15px; 
        margin: 10px 0; 
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2️⃣ الهوية البصرية الملكية العلوية (المقدمة السيادية للمنصة)
# ==============================================================================
st.markdown("""
    <div style="text-align: center; padding: 20px; margin-bottom: 10px;">
        <h1 style="color: #d4af37; font-family: 'Cairo', sans-serif; font-size: 40px; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px; text-shadow: 3px 3px 8px rgba(0,0,0,0.9);">
            🧬 CELLREVIVE AI
        </h1>
        <p style="color: #f3e5ab !important; font-family: 'Cairo', sans-serif; font-size: 21px; font-weight: 800; opacity: 0.95; line-height: 1.6; max-width: 850px; margin: 0 auto; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
            المنصة المتكاملة للترميم الخلوي وعكس مسار مقاومة الإنسولين والسكري من النوع الثاني
        </p>
        <hr style="border: 0; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); margin-top: 25px; margin-bottom: 25px;">
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 3️⃣ إدارة قاعدة البيانات المطورة (SQLite Sovereign Engine)
# ==============================================================================
def init_db():
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_code TEXT PRIMARY KEY,
            fbg REAL,
            ppbg REAL DEFAULT 140.0,
            rbg REAL DEFAULT 120.0,
            hba1c REAL,
            weight REAL,
            waist REAL,
            creatinine REAL DEFAULT 1.0,
            age INTEGER DEFAULT 45,
            gender TEXT DEFAULT 'Male',
            severity_score REAL DEFAULT 5.0,
            skin_analysis TEXT DEFAULT '',
            selected_drugs TEXT DEFAULT ''
        )
    """)
    
    # تجنب أخطاء التشغيل عند تحديث الجداول القديمة
    try: cursor.execute("ALTER TABLE patients ADD COLUMN creatinine REAL DEFAULT 1.0")
    except sqlite3.OperationalError: pass
    try: cursor.execute("ALTER TABLE patients ADD COLUMN age INTEGER DEFAULT 45")
    except sqlite3.OperationalError: pass
    try: cursor.execute("ALTER TABLE patients ADD COLUMN gender TEXT DEFAULT 'Male'")
    except sqlite3.OperationalError: pass

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS glucose_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_code TEXT,
            reading_time TEXT,
            reading_type TEXT,
            reading_value REAL,
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
        SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender 
        FROM patients WHERE patient_code = ?
    """, (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 'skin_analysis': row[7], 'selected_drugs': row[8], 'creatinine': row[9],
            'age': row[10], 'gender': row[11]
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], data['severity_score'], data['skin_analysis'], data['selected_drugs'], data['creatinine'], data['age'], data['gender']))
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
# 4️⃣ الدليل الاستراتيجي الفسيولوجي للأدوية وعكس النقص الخلوي
# ==============================================================================
EGYPTIAN_DRUG_DB = {
    "Cidophage (سيدوفاج)": {"supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف ب12 الحاد وتأثر الميتوكوندريا خلوياً"},
    "Glucophage (جلوكوفاج)": {"supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر الأعصاب الطرفية"},
    "Deltacortril (ديلتاكورتريل)": {"supp": "Potassium (99mg) + Magnesium Citrate (400mg) + Vit D3", "reason": "احتباس السوائل وهدم الكتلة العضلية ورفع مقاومة الإنسولين"},
    "Lasix (لازكس)": {"supp": "Thiamine B1 (100mg) + Potassium + Magnesium", "reason": "طرد المعادن النادرة ومستنفذات الطاقة الحيوية من الميتوكوندريا"},
    "Lipitor (ليبيتور)": {"supp": "CoQ10 (200mg) + Vit D3 (5000 IU)", "reason": "تثبيط مسار الميفالونات المسبب لآلام العضلات وضرر الميتوكوندريا"},
    "Ator (آتور)": {"supp": "CoQ10 (200mg)", "reason": "استنزاف مخزون طاقة الخلية الحيوية"},
    "Crestor (كريستور)": {"supp": "CoQ10 (200mg) + Magnesium", "reason": "تعب العضلات الأيضي وتثبيط التصنيع الذاتي للمرافق الإنزيمي"},
    "Forxiga (فورسيجا)": {"supp": "Electrolytes Complex + High Hydration Protocol", "reason": "إدرار الجلوكوز الكلوي ومخاطر التهابات المسالك البولية والجفاف الخلوي"},
    "Jardiance (جاردينس)": {"supp": "Electrolytes Complex + Hydration", "reason": "استنزاف الأملاح والسوائل الخلوية عبر الفلترة الكلوية"},
    "Mounjaro (مونجارو)": {"supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "فقدان الكتلة العضلية الحيوية السريع بسبب التثبيط المفرط للشهية"},
    "Ozempic (أوزمبيك)": {"supp": "Digestive Enzymes + Zinc + EAAs", "reason": "كسل وشلل حركة المعدة المؤقت والحاجة لتسهيل امتصاص المغذيات وبناء العضلات"},
    "Exforge (إكسفورج)": {"supp": "Zinc (50mg) + Ginkgo Biloba", "reason": "استنزاف الزنك وتأثر الأوعية الحيوية الدقيقة"},
    "Amaryl (أماريل)": {"supp": "Alpha-Lipoic Acid (600mg) + Chromium Picolinate", "reason": "إجهاد خلايا بيتا بالبنكرياس واستهلاك الإنزيمات الحامية للأعصاب"}
}

# ==============================================================================
# 5️⃣ الحاسبات الطبية السريرية الأكاديمية المعتمدة لعام 2026
# ==============================================================================
def calculate_homa_ir(fbg, fasting_insulin=12.0):
    return (fbg * fasting_insulin) / 405

def calculate_egfr(age, weight, creatinine, gender):
    if creatinine <= 0: return 90.0
    val = ((140 - age) * weight) / (72 * creatinine)
    if gender == 'Female' or gender == 'أنثى': 
        val *= 0.85
    return min(round(val, 2), 150.0)

# ==============================================================================
# 6️⃣ محرك الرؤية الحاسوبية المتقدم والذكاء الاصطناعي الفيدرالي
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح الـ API المفعل للمنصة لتشغيل الرؤية الذكية الخلوية."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي المعتمد لدى ADA و EASD لعام 2026. 
        يجب أن تكون إجاباتك مبنية بنسبة 100% على الدليل العلمي الأكاديمي الصارم وبأسلوب فخم وموثوق.
        - لا تقم بتغيير جرعات الأدوية الكيميائية للمريض بل وجهه للمراجعة الطبية الدقيقة مع الدكتور إيهاب حشمت.
        - ركز على: ترتيب تناول الطعام الصارم (ألياف، بروتين، ثم كربوهيدرات معقدة)، المقاصة الميتوكوندرية، ومنع طفرات السكر الحادة (Glucose Spikes).
        - يمكنك استقبال صور متعددة معاً (وجبات، تحاليل، روشتات وعينات أدوية)، وربطها بالملف الأيضي للمريض بدقة تامة.
        """
        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)
        content = [prompt]
        for img in images:
            content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال بالشبكة الطبية: {str(e)}"

def check_emergency_status(value, context_phrase=""):
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0; font-weight:900 !important;">🚨 إنذار طوارئ حرج جداً (هبوط حاد): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل صادر عن المنصة ({context_phrase}):</b> تم رصد هبوط حاد دون النطاق الفسيولوجي الآمن. يرجى تناول مصدر جلوكوز سريع (نصف كوب عصير أو ملعقة عسل) فوراً والاتصال بالدكتور إيهاب حشمت!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0; font-weight:900 !important;">🚨 إنذار طوارئ حرج جداً (ارتفاع مفرط): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل صادر عن المنصة ({context_phrase}):</b> قراءة السكر مرتفعة وتتجاوز عتبة الأمان الخلوي. خطر الحماض الكيتوني (DKA). تواصل مع الطبيب فوراً أو توجه لأقرب مستشفى لتنظيم السوائل.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 7️⃣ جدار الحماية الرقمي وجدولة هيكل الأكواد المشفرة (24 كوداً للعملاء)
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"

# الأكواد الأربعة التأسيسية السابقة
CORE_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]

# توليد 10 أكواد مخصصة للمشتركين في نظام الشهر (1 Month Plan)
MONTH_PLAN_CODES = [f"CR-1M-{i:02d}" for i in range(1, 11)]

# توليد 10 أكواد مخصصة للمشتركين في نظام الـ 3 أشهر (3 Months Plan)
QUARTER_PLAN_CODES = [f"CR-3M-{i:02d}" for i in range(1, 11)]

# الدمج الشامل والمحكم لمنع أي لخبطة برمجية في التحقق
VALID_PATIENT_CODES = CORE_CODES + MONTH_PLAN_CODES + QUARTER_PLAN_CODES

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div style="text-align:center; color:#d4af37; font-size:22px; font-weight:900; margin-bottom:15px;">🔐 بروتوكول العبور الرقمي الآمن</div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود الوصول السيادي الخاص بك:", type="password")
    if st.button("تأكيد الاتصال والمصادقة الحيوية"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "doctor", MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "patient", input_code
            st.rerun()
        else:
            st.error("كود غير مصرح به. يرجى مراجعة الإدارة الطبية فوراً.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male'
}

# ==============================================================================
# 8️⃣ لوحة تحكم الخبير الإكلينيكي العليا (د. إيهاب حشمت)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; border-bottom:1px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة التحكم والتحليل السيادي الإكلينيكي</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإدارة الأمنية")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    target_patient = st.selectbox("اختر كود المريض المراد تأسيسه وتعديل بياناته الفسيولوجية:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
    with st.expander("📝 ضبط وتعديل المؤشرات الحيوية والمخبرية الحالية بدقة", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم (mg/dL):", value=float(current_p_data['fbg']))
            mod_ppbg = st.number_input("سكر فاطر بعد ساعتين (mg/dL):", value=float(current_p_data['ppbg']))
            mod_rbg = st.number_input("سكر عشوائي (mg/dL):", value=float(current_p_data['rbg']))
            mod_creatinine = st.number_input("الكرياتينين (Serum Creatinine):", value=float(current_p_data['creatinine']), step=0.1)
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']))
            mod_weight = st.number_input("الوزن الحالي (كجم):", value=float(current_p_data['weight']))
            mod_waist = st.number_input("محيط الخصر السريري (سم):", value=float(current_p_data['waist']))
            mod_age = st.number_input("عمر المريض الحالي:", value=int(current_p_data['age']), step=1)
            mod_gender = st.selectbox("الجنس الفسيولوجي:", ["Male", "Female"], index=0 if current_p_data['gender'] == "Male" else 1)

    with st.expander("💊 بروتوكول المقاصة الدوائية من واقع الدستور الطبي بالعيادة"):
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية الفعالة الحالية للمريض:", list(EGYPTIAN_DRUG_DB.keys()), default=[d for d in saved_drugs_list if d in EGYPTIAN_DRUG_DB])

    if st.button("💾 ترحيل وتثبيت ملف المريض Permanent في قاعدة البيانات"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم بنجاح تشفير وحفظ تحديثات المريض صاحب الكود المميز: {target_patient}")

# ==============================================================================
# 9️⃣ واجهة المريض التفاعلية الذكية والمقاصة الميتوكوندرية الخلوية
# ==============================================================================
if st.session_state.role == "patient":
    # استخلاص وتحديد طبيعة ونوع نظام الاشتراك المالي آلياً بناء على الكود المكتوب
    plan_text = "نظام الشهر الفيدرالي" if "1M" in current_code else "نظام الـ 3 أشهر الملكي المعمق" if "3M" in current_code else "باقة التأسيس الأولي"
    
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 1px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك.. تم تفعيل الدخول البرمجي بنجاح لمتابعة: ({plan_text}) للكود الآمن [{current_code}]</p>', unsafe_allow_html=True)
    
    # فحص الطوارئ اللحظي
    check_emergency_status(p_data['fbg'], "تحليل سكر صائم مخزن")
    check_emergency_status(p_data['ppbg'], "تحليل سكر فاطر مخزن")
    
    calc_homa = calculate_homa_ir(p_data['fbg'])
    calc_egfr_val = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    
    # بطاقة عرض المؤشرات الخلوية الفاخرة المعتمدة
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 20px 0; font-weight:800; font-size:18px;">📊 المؤشرات الفسيولوجية الخلوية المستنبطة (Clinical Biomarkers)</h3>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color: #f3e5ab !important;">مقاومة الإنسولين HOMA-IR</span><br>
                    <span style="font-size:22px; font-weight:900; color:#ff4b4b;">{round(calc_homa, 2)}</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color: #f3e5ab !important;">كفاءة الفلترة الكلوية (eGFR)</span><br>
                    <span style="font-size:22px; font-weight:900; color:#00ffcc;">{calc_egfr_val} mL/min</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8; color: #f3e5ab !important;">قياس محيط الخصر</span><br>
                    <span style="font-size:22px; font-weight:900; color:#ffffff;">{p_data['waist']} سم</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # عرض تذبذب السكر الحيوي للمريض عبر الرسم البياني الفخم
    st.markdown('<div class="premium-card"><h3>📈 مراقبة وتتبع تذبذب الجلوكوز المستمر</h3>', unsafe_allow_html=True)
    raw_logs = get_all_glucose_logs(current_code)
    if raw_logs:
        df = pd.DataFrame(raw_logs, columns=["التوقيت", "نوع القراءة", "القيمة mg/dL"])
        fig = px.line(df, x="التوقيت", y="القيمة mg/dL", color="نوع القراءة", title="مسار المنحنى الأيضي للحالة", markers=True)
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("سجل تتبع التذبذب فارغ حالياً. قم بتدوين قراءات القياس بالأسفل لتغذية المحرك البياني.")
    st.markdown('</div>', unsafe_allow_html=True)

    # قسم تدوين القياسات اليومية الفورية
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

    # مختبر فحص وتطهير الوجبات بالعين الاصطناعية الذكية
    st.markdown('<div class="premium-card"><h3>🥗 مختبر فحص وتطهير الوجبات والمقاصة الدوائية الفورية</h3>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "📸 التقط أو ارفع صورة وجبتك الحالية، أو علب الأدوية والروشتات الطبية (يمكن رفع صور متعددة معاً للتحليل المتكامل والـ OCR):", 
        type=['jpg','png','jpeg'], 
        accept_multiple_files=True
    )
    
    if uploaded_files and st.button("🚀 تشغيل محرك التحليل البصري والأكاديمي الصارم"):
        with st.spinner("يجري الآن معالجة الصور ومطابقتها مع محددات كفاءة الكلى والأدوية الحالية للمريض..."):
            meal_prompt = f"""
            بصفتك الخبير الأكاديمي الصارم، حلل كافة الصور المرفوعة (وجبات، علب أدوية، روشتات عبر الـ OCR)، واربطها بالمؤشرات المثبتة للمريض التالي:
            - عمر المريض: {p_data['age']} سنة | الجنس الفسيولوجي: {p_data['gender']}
            - قياس سكر صائم حالي: {p_data['fbg']} mg/dL
            - كفاءة الفلترة الكلوية الديناميكية (eGFR): {calc_egfr_val} mL/min
            - السكر التراكمي للحالة (HbA1c): {p_data['hba1c']}%
            - بروتوكول الأدوية الموصوف له حالياً: {p_data['selected_drugs']}
            - مؤشر حساب مقاومة الإنسولين الحالية HOMA-IR: {round(calc_homa, 2)}
            
            أعطِ تقريراً استراتيجياً حاداً ومقسماً بدقة وبخطوط واضحة إلى 4 نقاط جوهرية:
            1. التحليل البصري الدقيق والـ OCR لكافة المدخلات المصورة ونسبة المغذيات أو دقة مسميات الأدوية والروشتات.
            2. التعديل الفوري والإلزامي لمكونات الطعام لحماية جدار الخلية ومنع الـ Glucose Spike بناءً على كفاءته الكلوية والأيضية الحالية.
            3. بروتوكول التطهير الخلوي والترتيب الرياضي الدقيق لتناول الوجبة، ومواعيد الأدوية المكتشفة بالصورة والربط الفسيولوجي بينها.
            4. المكملات والمقاصة التغذوية لتعويض النقص الخلوي والميتوكوندري المستنزف جراء الأدوية الكيميائية المثبتة لديه.
            """
            res = analyze_with_gemini(uploaded_files, meal_prompt)
            st.markdown("<h4>📋 تقرير الفحص الطبي الصارم والترميم الميتوكوندري:</h4>", unsafe_allow_html=True)
            st.write(res)
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل المنصة الرسمي الصارم
st.markdown('<div style="text-align:center; font-size:11px; opacity:0.6; color:#d4af37 !important; font-weight:800; margin-top:20px;">CellRevive AI v7.0 • The Ultimate Sovereign Longevity Engine 2026</div>', unsafe_allow_html=True)
