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
# 1️⃣ الإعدادات المتقدمة والواجهة الفاخرة (2026 Luxury Hub)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Living Engine",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# إدارة وتأمين الـ API Key لـ Gemini (قراءة تلقائية من السيرفر أو إدخال يدوي مؤمن)
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
elif "api_key_input" in st.session_state and st.session_state.api_key_input:
    GEMINI_API_KEY = st.session_state.api_key_input
    genai.configure(api_key=GEMINI_API_KEY)
else:
    GEMINI_API_KEY = ""

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
    .main-title { color: #d4af37; text-align: center; font-size: 28px; font-weight: bold; text-shadow: 2px 2px 4px #000; }
    .sub-title { color: #ffffff; text-align: center; font-size: 16px; margin-bottom: 30px; opacity: 0.9; }
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

# ==============================================================================
# 2️⃣ إدارة قاعدة البيانات المطورة ديناميكياً (SQLite Engine)
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
# 3️⃣ الدليل الاستراتيجي للأدوية والمقاصة التغذوية
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
# 4️⃣ الحاسبات الطبية السريرية الصارمة الديناميكية
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
# 5️⃣ محرك الرؤية الحاسوبية ومعالجة الصور المتعددة
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح API من قبل إدارة النظام لتفعيل الرؤية الحية الحركية."
    try:
        system_instruction = """
        بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي المعتمد لدى ADA و EASD لعام 2026. 
        يجب أن تكون إجاباتك مبنية بنسبة 100% على الدليل العلمي الأكاديمي الصارم. 
        - لا تقم أبداً بتغيير جرعات الأدوية الكيميائية للمريض بل وجهه دائماً للرجوع للدكتور إيهاب حشمت.
        - ركز تماماً على: ترتيب تناول الطعام (ألياف، بروتين، ثم نشويات معقدة)، المقاصة الميتوكوندرية، ومنع طفرات السكر العشوائية (Glucose Spikes).
        - يمكنك استقبال ومعالجة عدة صور معاً (وجبات، تحاليل، روشتات، أو علب أدوية)، وقم بربط البيانات وتقديم تحليل موحد دقيق.
        - إذا كانت الصور غير واضحة، اعتذر فوراً واطلب صوراً أكثر وضوحاً لحماية دقة التشخيص.
        """
        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)
        content = [prompt]
        for img in images:
            content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال بالسيرفر الطبي: {str(e)}"

def check_emergency_status(value, context_phrase=""):
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ سيادي حرج (هبوط حاد): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> تم رصد هبوط حاد. تناول كربوهيدرات سريعة الامتصاص (نصف كوب عصير أو ملعقة عسل) فوراً وتواصل مع الدكتور إيهاب حشمت فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إنذار طوارئ سيادي حرج (ارتفاع مفرط): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه عاجل ({context_phrase}):</b> مستوى السكر يتجاوز النطاق الآمن. خطر الحماض الكيتوني (DKA). يرجى التوجه للطوارئ لضبط السوائل والجرعات فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 6️⃣ بوابة الوصول الرقمية وجدولة الأكواد المحدثة
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"

# الأكواد التأسيسية السابقة
CORE_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]

# توليد 10 أكواد لنظام الشهر (1 Month Plan)
MONTH_PLAN_CODES = [f"CR-1M-{i:02d}" for i in range(1, 11)]  # تنتج: CR-1M-01 إلى CR-1M-10

# توليد 10 أكواد لنظام الـ 3 أشهر (3 Months Plan)
QUARTER_PLAN_CODES = [f"CR-3M-{i:02d}" for i in range(1, 11)]  # تنتج: CR-3M-01 إلى CR-3M-10

# دمج كافة الأكواد المصرح لها بالدخول في مصفوفة واحدة موحدة
VALID_PATIENT_CODES = CORE_CODES + MONTH_PLAN_CODES + QUARTER_PLAN_CODES

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div class="main-title">🧬 CELLREVIVE AI • بوابـة العبـور الرقمية السيادية</div>', unsafe_allow_html=True)
    input_code = st.text_input("أدخل كود الوصول الآمن:", type="password")
    if st.button("تفعيل بروتوكول الاتصال المشفر"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "doctor", MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "patient", input_code
            st.rerun()
        else:
            st.error("الكود غير صحيح. يرجى مراجعة إدارة العيادة.")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': '', 'creatinine': 1.0,
    'age': 45, 'gender': 'Male'
}

# ==============================================================================
# 7️⃣ لوحة تحكم الطبيب المعالج العليا (د. إيهاب حشمت)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div class="main-title">🧬 CellRevive AI - التحكم السيادي الإكلينيكي</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### 🔐 الإشراف الأمني")
    st.session_state.api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=GEMINI_API_KEY)
    
    # اختيار المريض يضم الآن جميع المشتركين الجدد والقدامى مصنفين ومفرودين بالكامل
    target_patient = st.selectbox("اختر كود المريض للتأسيس الصارم:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or p_data
    
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

    with st.expander("💊 بروتوكول المقاصة الدوائية الحالية بالعيادة"):
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية الموصوفة للمريض من الدستور:", list(EGYPTIAN_DRUG_DB.keys()), default=[d for d in saved_drugs_list if d in EGYPTIAN_DRUG_DB])

    if st.button("💾 تثبيت وحفظ ملف المريض Permanent الحركي"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs), 'creatinine': mod_creatinine, 'age': int(mod_age), 'gender': mod_gender
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم تشفير وتثبيت مؤشرات المريض {target_patient} الأكاديمية بنجاح.")

# ==============================================================================
# 8️⃣ واجهة المريض التفاعلية + محرك التحليلات والحاسبات الطبية الديناميكية
# ==============================================================================
if st.session_state.role == "patient":
    # تمييز نوع الاشتراك للمريض في العنوان ترحيباً به وبناء على كوده
    plan_text = "نظام الشهر" if "1M" in current_code else "نظام الـ 3 أشهر" if "3M" in current_code else "النظام التأسيسي الآمن"
    st.markdown(f'<div class="main-title">🧬 منظومة الترميم الخلوي وعكس الأمراض الأيضية</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; color:#d4af37 !important; font-size:14px;">مرحباً بك في لوحة تحكمك الحية لمتابعة ({plan_text})</p>', unsafe_allow_html=True)
    
    check_emergency_status(p_data['fbg'], "قراءة الصائم المسجلة")
    check_emergency_status(p_data['ppbg'], "قراءة الفاطر المسجلة")
    
    calc_homa = calculate_homa_ir(p_data['fbg'])
    calc_egfr_val = calculate_egfr(p_data['age'], p_data['weight'], p_data['creatinine'], p_data['gender'])
    
    st.markdown(f"""
        <div class="premium-card">
            <h3 style="color:#d4af37; margin:0 0 15px 0;">📊 المؤشرات الحيوية المستخلصة رقمياً (Clinical Metrics)</h3>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">مؤشر HOMA-IR الحسابي</span><br>
                    <span style="font-size:20px; font-weight:bold; color:#ff4b4b;">{round(calc_homa, 2)}</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">كفاءة الفلترة الكلوية الديناميكية (eGFR)</span><br>
                    <span style="font-size:20px; font-weight:bold; color:#00ffcc;">{calc_egfr_val} mL/min</span>
                </div>
                <div class="metric-box" style="flex:1; min-width:140px;">
                    <span style="font-size:12px; opacity:0.8;">محيط الخصر الحالي</span><br>
                    <span style="font-size:20px; font-weight:bold; color:#ffffff;">{p_data['waist']} سم</span>
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
                st.success("تم التدوين الآمن بنجاح.")
                st.rerun()

    st.markdown('<div class="premium-card"><h3>🥗 مختبر فحص وتطهير الوجبات والتحليل التكنولوجي المتقدم</h3>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "📸 التقط أو ارفع صورة وجبتك الحالية أو علب الأدوية والروشتات (يمكن اختيار عدة صور معاً للتحليل المتكامل والـ OCR):", 
        type=['jpg','png','jpeg'], 
        accept_multiple_files=True
    )
    
    if uploaded_files and st.button("🚀 بدء بروتوكول التحليل التكنولوجي الصارم"):
        with st.spinner("يجري الآن ربط وقراءة الصور المرفوعة ومقاصتها مع الملف الطبي وكفاءة الكلى الحركية للمريض..."):
            meal_prompt = f"""
            بصفتك الخبير الأكاديمي، حلل بدقة كافة الصور المرفوعة (قد تحتوي على وجبات طعام، أو علب أدوية، أو روشتات طبية عبر الـ OCR)، واربطها بالمؤشرات المخزنة لهذا المريض كالتالي:
            - عمر المريض الحالي: {p_data['age']} سنة | الجنس: {p_data['gender']}
            - سكر صائم أساسي: {p_data['fbg']} mg/dL
            - كفاءة الكلى الحالية الديناميكية (eGFR): {calc_egfr_val} mL/min
            - السكر التراكمي (HbA1c): {p_data['hba1c']}%
            - الأدوية الحالية النشطة في ملفه: {p_data['selected_drugs']}
            - مؤشر مقاومة الإنسولين الحالية HOMA-IR: {round(calc_homa, 2)}
            
            أعطِ تقريراً استراتيجياً صارماً من 4 نقاط مقسمة بوضوح:
            1. التحليل البصري الدقيق (مكونات الوجبة بالعين الذكية ونسبة النشويات، أو قراءة الـ OCR لعلب الأدوية/الروشتات بدقة 100%).
            2. التعديل الفوري والإلزامي (ما يجب حذفه لحماية الخلية ومنع الـ Glucose Spike بناءً على حالته الكلوية والأيضية).
            3. بروتوكول التطهير الخلوي (الترتيب الدقيق لتناول الوجبة، وتوقيت الأدوية المكتشفة بالصورة والربط بينها).
            4. المكملات والمقاصة التغذوية المطلوبة لتعويض النقص الخلوي الناتج عن تداخل الأدوية الموصوفة لديه.
            """
            res = analyze_with_gemini(uploaded_files, meal_prompt)
            st.markdown("<h4>📋 التقرير الطبي الصارم والتحليل المتكامل للمنظومة:</h4>", unsafe_allow_html=True)
            st.write(res)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size:10px; opacity:0.5; color:#ffffff !important;">CellRevive AI v6.5 - Premium Subscription Engine Edition 2026</div>', unsafe_allow_html=True)
