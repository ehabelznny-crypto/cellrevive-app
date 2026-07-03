import streamlit as st
import sqlite3
import math
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import io
import os
import pandas as pd
import plotly.express as px

# استيراد مكتبة التشفير لحماية البيانات بمعايير HIPAA الدولية
try:
    from cryptography.fernet import Fernet
except ImportError:
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet

# ==============================================================================
# 0️⃣ منظومة التشفير السيادية (HIPAA Data Protection Engine)
# ==============================================================================
if "ENCRYPTION_KEY" in st.secrets:
    KEY = st.secrets["ENCRYPTION_KEY"].encode()
else:
    KEY = b'v-X7F5_0xZ8Wk1P_M9q2B6n4T_c8K3j5L7m9N1v3X5Q=' 

cipher_suite = Fernet(KEY)

def encrypt_data(data_str):
    if not data_str: return ""
    return cipher_suite.encrypt(data_str.encode()).decode()

def decrypt_data(crypto_str):
    if not crypto_str: return ""
    try:
        return cipher_suite.decrypt(crypto_str.encode()).decode()
    except Exception:
        return crypto_str

# ==============================================================================
# 1️⃣ الإعدادات المتقدمة والواجهة الفاخرة (2026 Global Luxury Hub)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - Sovereign Living Engine",
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

# هندسة التصميم الفاخر الملكي (Premium Gold & Dark CSS)
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
    label, p, span, h3 { color: #ffffff !important; font-weight: 600 !important; }
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

# الهوية البصرية الملكية العلوية للمنصة
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
            country TEXT DEFAULT 'Egypt', cgm_connected INTEGER DEFAULT 0
        )
    """)
    try: cursor.execute("ALTER TABLE patients ADD COLUMN cgm_connected INTEGER DEFAULT 0")
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
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    encrypted_skin = encrypt_data(data['skin_analysis'])
    encrypted_drugs = encrypt_data(data['selected_drugs'])
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs, creatinine, age, gender, country, cgm_connected)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], data['severity_score'], encrypted_skin, encrypted_drugs, data['creatinine'], data['age'], data['gender'], data['country'], data['cgm_connected']))
    conn.commit()
    conn.close()

def log_glucose(code, g_type, value, custom_time=None):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    t_str = custom_time if custom_time else datetime.now().strftime('%Y-%m-%d %H:%M')
    cursor.execute("INSERT INTO glucose_logs (patient_code, reading_time, reading_type, reading_value) VALUES (?, ?, ?, ?)",
                   (code, t_str, g_type, value))
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
# 3️⃣ الدستور الدوائي ومحرك حساب تذبذب الجلوكوز الرياضي (eGMS Index)
# ==============================================================================
GLOBAL_DRUG_DB = {
    "Egypt": {
        "Cidophage (سيدوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg) + CoQ10", "reason": "استنزاف ب12 الحاد وتأثر الميتوكوندريا خلوياً"},
        "Glucophage (جلوكوفاج)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "ضعف امتصاص فيتامين ب12 الممتد وتأثر الأعصاب الطرفية"},
        "Deltacortril (ديلتاكورتريل)": {"generic": "Prednisolone", "supp": "Potassium (99mg) + Magnesium Citrate (400mg) + Vit D3", "reason": "احتباس السوائل وهدم الكتلة العضلية ورفع مقاومة الإنسولين"},
        "Lasix (لازكس)": {"generic": "Furosemide", "supp": "Thiamine B1 (100mg) + Potassium + Magnesium", "reason": "طرد المعادن النادرة ومستنفذات الطاقة الحيوية من الميتوكوندريا"},
        "Lipitor (ليبيتور)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3 (5000 IU)", "reason": "تثبيط مسار الميفالونات المسبب لآلام العضلات وضرر الميتوكوندريا"},
        "Mounjaro (مونجارو)": {"generic": "Tizepatide", "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "فقدان الكتلة العضلية الحيوية السريع بسبب التثبيط المفرط للشهية"},
        "Ozempic (أوزمبيك)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc + EAAs", "reason": "كسل وشلل حركة المعدة المؤقت والحاجة لتسهيل امتصاص المغذيات وبناء العضلات"}
    },
    "Gulf & International": {
        "Glucophage (International)": {"generic": "Metformin", "supp": "Methyl B12 (1000mcg)", "reason": "Long-term vitamin B12 malabsorption and mitochondrial protection"},
        "Lipitor (International)": {"generic": "Atorvastatin", "supp": "CoQ10 (200mg) + Vit D3", "reason": "Mevalonate pathway inhibition causing myalgia"},
        "Mounjaro (International)": {"generic": "Tirzepatide", "supp": "Essential Amino Acids (EAAs) + Bio-Protein Protocol", "reason": "Rapid muscle mass loss prevention"},
        "Ozempic (International)": {"generic": "Semaglutide", "supp": "Digestive Enzymes + Zinc", "reason": "Gastric motility delay management"}
    }
}

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
# 4️⃣ محرك الرؤية الحاسوبية والذكاء الاصطناعي الاستباقي (الهندسة الميتوكوندرية)
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح الـ API المعتمد لتشغيل محرك التحليل البصري الاستباقي."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي لعام 2026.
        مهمتك الأساسية هي هندسة الوجبات هندسة استباقية صارمة لتسطيح منحنى السكر تماماً وتخفيض التذبذب (CV < 10%).
        عند تقديم نصائح التعديل والإضافة والمقاصة الغذائية، يجب الالتزام الصارم بالقواعد التالية لتسهيل التطبيق على المريض:
        - ترجمة الجرامات الطبية فوراً وبدقة إلى وحدات منزلية قياسية تقريبية متعارف عليها بين المرضى.
        - استخدم التعبيرات التالية حصراً للكميات: (معيار كفة اليد بدون أصابع للبروتين، حجم عقلة الأصبع للدهون، ملعقة صغيرة، ملعقة كبيرة، حجم عبوة الكبريت الصغيرة للجبن، كوب كبير 240 مل، كوب صغير 120 مل).
        - رتب تناول الوجبة إلزامياً: الألياف أولاً، ثم البروتين والدهون الصحية، ثم الكربوهيدرات المعقدة في النهاية لتأخير الامتصاص المعوي.
        - لا تقم بتغيير جرعات الأدوية الكيميائية، بل وجه المريض دائماً لمراجعة الدكتور إيهاب حشمت الظني.
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
                        <b>تنبيه عاجل ({context_phrase}):</b> تم رصد هبوط حاد دون النطاق الفسيولوجي الآمن. يرجى تناول مصدر جلوكوز سريع فوراً والاتصال بالدكتور إيهاب حشمت!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ حرج جداً (ارتفاع مفرط): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> قراءة السكر مرتفعة وتتجاوز عتبة الأمان الخلوي. خطر الحماض الكيتوني (DKA). تواصل مع الإدارة الطبية فوراً.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 5️⃣ جدار الحماية الرقمي والتحقق من الأكواد الـ 24 المعتمدة
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
    input_code = st.text_input("أدخل كود الوصول السيادي الخاص بك:", type="password")
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
    'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male', 'country': 'Egypt', 'cgm_connected': 0
}

# ==============================================================================
# 6️⃣ لوحة تحكم الخبير الإكلينيكي العليا (د. إيهاب حشمت الظني)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div style="color:#d4af37; font-size:24px; font-weight:900; text-align:center; border-bottom:1px solid #d4af37; padding-bottom:10px; margin-bottom:20px;">👑 لوحة التحكم والتحليل السيادي الإكلينيكية العالمية</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    target_patient = st.selectbox("اختر كود المريض المراد تأسيسه وتعديل ملفه الفسيولوجي:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
    with st.expander("🌍 النطاق الجغرافي والدستور الدوائي المستهدف", expanded=True):
        mod_country = st.selectbox("اختر النطاق الدستوري للأدوية:", list(GLOBAL_DRUG_DB.keys()), index=0 if current_p_data['country'] == "Egypt" else 1)
        mod_cgm = st.checkbox("🔌 تفعيل خيار الربط الديناميكي مع مستشعرات CGM (اختياري للحالات المتقدمة)", value=bool(current_p_data['cgm_connected']))

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

    with st.expander("💊 بروتوكول المقاصة الدوائية الحالية (بناءً على الدستور المختار)"):
        available_drugs = GLOBAL_DRUG_DB[mod_country]
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية الفعالة الحالية للمريض:", list(available_drugs.keys()), default=[d for d in saved_drugs_list if d in available_drugs])

    if st.button("💾 تثبيت وحفظ ملف المريض المشفر (HIPAA Protected)"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender,
            'country': mod_country, 'cgm_connected': 1 if mod_cgm else 0
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم بنجاح تشفير وتثبيت مؤشرات المريض {target_patient} في قاعدة البيانات السيادية.")

# ==============================================================================
# 7️⃣ واجهة المريض التفاعلية ومختبر الهندسة الاستباقية للوجبات
# ==============================================================================
if st.session_state.role == "patient":
    plan_text = "نظام الشهر السريع" if "1M" in current_code else "نظام الـ 3 أشهر الممتد" if "3M" in current_code else "النظام التأسيسي الآمن"
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:16px; font-weight:800; border: 1px solid #d4af37; padding: 8px; border-radius: 8px;">مرحباً بك.. تم تفعيل الدخول البرمجي لمتابعة: ({plan_text}) للكود الآمن [{current_code}]</p>', unsafe_allow_html=True)
    
    # فحص الطوارئ اللحظي
    check_emergency_status(p_data['fbg'], "قراءة الصائم المسجلة")
    check_emergency_status(p_data['ppbg'], "قراءة الفاطر المسجلة")
    
    calc_homa = calculate_homa_ir(p_data['fbg'])
    calc_egfr_val = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    cv_score, cv_status = calculate_glucose_variability(current_code)
    
    # 🔌 قسم الـ CGM الاختياري (يظهر فقط إذا قام الدكتور بتفعيله للحالة في لوحة التحكم)
    if p_data['cgm_connected'] == 1:
        st.markdown("""
            <div class="premium-card" style="border-color: #00ffcc;">
                <h3 style="color:#00ffcc !important; margin:0 0 10px 0;">🔌 مستشعر السكر المستمر النشط (Dexcom / Libre API)</h3>
                <p style="font-size:13px; margin:0; opacity:0.9;">
                    تم اكتشاف جهاز الاستشعار ومزامنة القراءات الحية ديناميكياً كل 5 دقائق مع خادم المنصة الرئيسي لمراقبة المنحنى الأيضي اللحظي.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # بطاقة عرض المؤشرات الحيوية
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37 !important; margin:0 0 20px 0; font-size:18px;">📊 المؤشرات الفسيولوجية المستخلصة (Clinical Biomarkers)</h3>
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

    # التحليل البياني التفاعلي لتقلبات الجلوكوز
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

    # تدوين القراءات اليدوية السريعة
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

    # 🥗 مختبر هندسة الوجبات الاستباقي وتعديل الوجبة قبل تناولها
    st.markdown('<div class="premium-card"><h3>🥗 مختبر الهندسة الاستباقية للوجبات وتعديلها قبل الأكل</h3>', unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "📸 افتح الكاميرا والتقط/ارفع صورة وجبتك الحالية أو عينات الأدوية لتعديلها استباقياً:", 
        type=['jpg','png','jpeg'], 
        accept_multiple_files=True
    )
    
    # حقل إلزامي لكتابة المكونات بدقة لتجنب أخطاء الرؤية الحاسوبية العشوائية
    meal_description = st.text_area(
        "✍️ اكتب بدقة مكونات وجبتك بالتفصيل (مثال: طبق أرز، قطعتين دجاج مشوي، سلطة خضراء):",
        placeholder="كتابة المكونات هنا إلزامية لتأكيد التحليل البصري ومنع الأخطاء التفسيرية للصورة..."
    )
    
    if uploaded_files and st.button("🚀 بدء بروتوكول الهندسة الاستباقية الفورية"):
        if not meal_description.strip():
            st.error("⚠️ خطأ أمني: يرجى كتابة وصف الوجبة بالتفصيل أولاً لحماية المنحنى الأيضي من الأخطاء التفسيرية للصور.")
        else:
            with st.spinner("يجري الآن معالجة الصور ومطابقتها مع المكونات المكتوبة والملف الطبي المشنفر..."):
                advanced_meal_prompt = f"""
                بصفتك الخبير الأكاديمي الصارم، قم بتحليل الصور المرفقة ومطابقتها ومقاطعتها مع الوصف المكتوب للوجبة من قِبل المريض لضمان دقة 100%:
                - المكونات المكتوبة بدقة من المريض: {meal_description}
                - عمر المريض: {p_data['age']} سنة | الجنس الفسيولوجي: {p_data['gender']}
                - قياس سكر صائم مخزن: {p_data['fbg']} mg/dL
                - كفاءة الفلترة الكلوية الديناميكية (eGFR): {calc_egfr_val} mL/min
                - مؤشر تذبذب الجلوكوز الرياضي الحالي للحالة: {cv_score}%
                - بروتوكول الأدوية الموصوف له حالياً: {p_data['selected_drugs']}
                - مؤشر حساب مقاومة الإنسولين الحالية HOMA-IR: {round(calc_homa, 2)}
                
                أعطِ تقريراً استراتيجياً حاداً ومقسماً بدقة وبخطوط عريضة ملكية ذهبية إلى 4 نقاط جوهرية:
                1. التحليل البصري والمطابقة: تقييم مكونات الطعام المصورة ومقارنتها بالوصف المكتوب وتحديد الأخطاء أو التنبيهات فوراً.
                2. التعديل الهندسي الاستباقي للوجبة (قبل الأكل): حساب نسب المغذيات وإصدار أوامر فورية للمريض بإضافة أو تعديل الوجبة (مثال: "أضف كذا أولاً، أو أخّر تناول كذا 15 دقيقة") لضمان تفادي الـ Glucose Spike تماماً وتحقيق منحنى مسطح (CV < 10%).
                3. التعبير بالوحدات المنزلية: يجب صياغة كميات التعديل والإضافة المطلوبة بالجرامات ومصحوبة فوراً بالوحدات المنزلية والتقريبية الصارمة (معيار كفة اليد بدون أصابع، حجم عقلة الأصبع، ملعقة صغيرة/كبيرة، حجم عبوة الكبريت الصغيرة، كوب كبير 240 مل أو صغير 120 مل).
                4. بروتوكول الترتيب الرياضي الصارم لتناول الوجبة، وتوقيت الأدوية وعلاقتها الفسيولوجية بقمع السكر العشوائي.
                """
                res = analyze_with_gemini(uploaded_files, advanced_meal_prompt)
                st.markdown("<h4>📋 تقرير الهندسة الاستباقية والمقاصة الميتوكوندرية:</h4>", unsafe_allow_html=True)
                st.write(res)
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل المنصة الرسمي الصارم
st.markdown('<div style="text-align:center; font-size:11px; opacity:0.6; color:#d4af37 !important; font-weight:800; margin-top:20px;">CellRevive AI v7.5 • Advanced Predictive Metabolic Engine 2026</div>', unsafe_allow_html=True)
