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
# 1️⃣ الإعدادات المتقدمة والواجهة الفاخرة (2026 Global Luxury Multi-Lang Design)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Living Engine",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# نظام التدويل واختيار اللغة (خطوة أساسية نحو العالمية)
lang = st.sidebar.selectbox("🌐 Language / اللغة", ["العربية", "English"])

GEMINI_API_KEY = st.sidebar.text_input("Gemini API Key", type="password", value="")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# تحديد اتجاه الواجهة بناءً على اللغة
dir_css = "rtl" if lang == "العربية" else "ltr"
align_css = "right" if lang == "العربية" else "left"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #040d1a; color: #ffffff !important; }}
    [data-testid="stMainBlockContainer"] {{ direction: {dir_css} !important; text-align: {align_css} !important; }}
    .premium-card {{
        background: linear-gradient(145deg, #0a1f38, #07162c);
        border: 1px solid #d4af37;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }}
    .emergency-card {{
        background: linear-gradient(145deg, #4a0d0d, #2a0505);
        border: 2px solid #ff4b4b;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.4);
    }}
    @keyframes pulse {{
        0% {{ border-color: #ff4b4b; }}
        50% {{ border-color: #aa1111; }}
        100% {{ border-color: #ff4b4b; }}
    }}
    .main-title {{ color: #d4af37; text-align: center; font-size: 28px; font-weight: bold; text-shadow: 2px 2px 4px #000; }}
    .sub-title {{ color: #ffffff; text-align: center; font-size: 16px; margin-bottom: 30px; opacity: 0.9; }}
    label, p, span {{ color: #ffffff !important; font-weight: 500 !important; }}
    .stButton>button {{
        background: linear-gradient(90deg, #d4af37, #aa8422);
        color: #040d1a !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        height: 3em;
        width: 100%;
        border: none;
    }}
    .metric-box {{ border-right: 3px solid #d4af37; padding-right: 15px; margin: 10px 0; }}
    </style>
""", unsafe_allow_html=True)

# دالة سيادية لمنع كوارث التحويل الرقمي عند قراءة البيانات الفارغة
def safe_float(val, default=0.0):
    try:
        return float(val) if val is not None else default
    except (ValueError, TypeError):
        return default

# ==============================================================================
# 2️⃣ إدارة قاعدة البيانات الدائمة والمجانية (SQLite Database Engine)
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
            severity_score REAL DEFAULT 5.0,
            skin_analysis TEXT DEFAULT '',
            selected_drugs TEXT DEFAULT ''
        )
    """)
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN ppbg REAL DEFAULT 140.0")
    except sqlite3.OperationalError: pass
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN rbg REAL DEFAULT 120.0")
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
    cursor.execute("SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs FROM patients WHERE patient_code = ?", (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': safe_float(row[0], 120.0), 
            'ppbg': safe_float(row[1], 140.0), 
            'rbg': safe_float(row[2], 120.0), 
            'hba1c': safe_float(row[3], 6.5), 
            'weight': safe_float(row[4], 80.0), 
            'waist': safe_float(row[5], 100.0),
            'severity_score': safe_float(row[6], 5.0), 
            'skin_analysis': row[7] if row[7] else 'No Analysis / لم يتم الفحص', 
            'selected_drugs': row[8] if row[8] else ''
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, safe_float(data['fbg']), safe_float(data['ppbg']), safe_float(data['rbg']), safe_float(data['hba1c']), safe_float(data['weight']), safe_float(data['waist']), safe_float(data['severity_score']), data['skin_analysis'], data['selected_drugs']))
    conn.commit()
    conn.close()

def log_glucose(code, g_type, value):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO glucose_logs (patient_code, reading_time, reading_type, reading_value)
        VALUES (?, ?, ?, ?)
    """, (code, datetime.now().strftime('%Y-%m-%d %H:%M'), g_type, safe_float(value)))
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
# 3️⃣ الدليل الاستراتيجي للأدوية المصرية
# ==============================================================================
EGYPTIAN_DRUG_DB = {
    "Cidophage (سيدوفاج)": {"supp": "Methyl B12", "reason": "استنزاف امتصاص فيتامين ب12 على المدى الطويل وتضرر الأعصاب"},
    "Glucophage (جلوكوفاج)": {"supp": "Methyl B12", "reason": "سوء امتصاص فيتامين ب12 الممتد وتأثر الميتوكوندريا"},
    "Deltacortril (ديلتاكورتريل)": {"supp": "Potassium & Magnesium", "reason": "احتباس الصوديوم وهدم الكتلة العضلية"},
    "Lasix (لازكس)": {"supp": "Thiamine (B1) & Potassium", "reason": "تفريغ الميتوكوندريا من المعادن الأساسية"},
    "Lipitor (ليبيتور)": {"supp": "CoQ10 (200mg)", "reason": "تثبيط إنتاج طاقة الخلية واستنزاف ميتوكوندريا العضلات"},
    "Ator (آتور)": {"supp": "CoQ10 (200mg)", "reason": "استنزاف إنزيم الطاقة الميتوكوندري الحرج"},
    "Crestor (كريستور)": {"supp": "CoQ10 + Vitamin D3", "reason": "تثبيط إنزيم الكبد وتعب العضلات الأيضي"},
    "Forxiga (فورسيجا)": {"supp": "Electrolytes Protocol", "reason": "طرد السكر عن طريق البول ومخاطر الجفاف"},
    "Jardiance (جاردينس)": {"supp": "Electrolytes & High Hydration", "reason": "إدرار السكر الكلوي واستنزاف السوائل"},
    "Mounjaro (مونجارو)": {"supp": "Essential Amino Acids", "reason": "تبديد ونقص الكتلة العضلية السريع نتيجة سد الشهية المفرط"},
    "Ozempic (أوزمبيك)": {"supp": "Digestive Enzymes & Amino Acids", "reason": "بطء حركة المعدة الشديد والحاجة لدعم الهضم"},
    "Victoza (فيكتوزا)": {"supp": "Pancreatic & Muscle Support", "reason": "تحفيز البنكرياس المستمر والحاجة للمقاصة الجينية"},
    "Concor (كونكور)": {"supp": "CoQ10 & Melatonin", "reason": "تقليل إنتاج الميلاتونين الليلي وتثبيط طاقة بيتا"},
    "Exforge (إكسفورج)": {"supp": "Zinc & Ginkgo Biloba", "reason": "تأثير على توسعة الأوعية والحاجة لحماية المغذيات"},
    "Amaryl (أماريل)": {"supp": "Alpha-Lipoic Acid", "reason": "عصر البنكرياس المستمر والحاجة لحماية الأعصاب"}
}

# ==============================================================================
# 4️⃣ محرك الرؤية الحاسوبية (Vision AI Engine)
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ Please enter Gemini API Key in the sidebar / يرجى إدخال مفتاح API."
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        content = [prompt]
        for img in images:
            content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def extract_severity_score(text):
    match = re.search(r'(?:score|الدرجة|الحدة|مستوى)[:\s\-]*([0-9\.]+)', text, re.IGNORECASE)
    if match:
        try: return min(max(float(match.group(1)), 1.0), 10.0)
        except: pass
    return 5.0

def check_emergency_status(value, context_phrase=""):
    value = safe_float(value)
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 Critical Alert / إنذار طوارئ حرج: {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>[CRITICAL] ({context_phrase})</b> Glucose level is dangerous. Action required immediately. Seek medical emergency or contact Dr. Ehab.
                        <br><b>[تحذير حرج جداً] ({context_phrase}):</b> هبوط حاد. يرجى مراجعة العيادة أو التوجه لقسم الطوارئ فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 Critical Alert / إنذار طوارئ حرج: {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>[CRITICAL] ({context_phrase})</b> Severe Hyperglycemia detected. Risk of DKA. Seek emergency hospital assistance immediately.
                        <br><b>[تحذير حرج جداً] ({context_phrase}):</b> ارتفاع مفرط وخطر الحماض الكيتوني. يرجى التوجه للمستشفى فوراً!
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 5️⃣ بوابة العبور الآمنة
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
VALID_PATIENT_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div class="main-title">🧬 CELLREVIVE AI • Global Hub</div>', unsafe_allow_html=True)
    input_code = st.text_input("Enter your access code / أدخل كود الوصول الرقمي:", type="password")
    if st.button("Connect Security Protocol / تفعيل الاتصال المشفر"):
        if input_code == MASTER_CODE:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "doctor", MASTER_CODE
            st.rerun()
        elif input_code in VALID_PATIENT_CODES:
            st.session_state.is_auth, st.session_state.role, st.session_state.auth_code = True, "patient", input_code
            st.rerun()
        else:
            st.error("Invalid Code / الكود غير صحيح")
    st.stop()

current_code = st.session_state.auth_code
p_data = get_patient_data(current_code) or {
    'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
    'severity_score': 5.0, 'skin_analysis': 'No Analysis', 'selected_drugs': ''
}

# ==============================================================================
# 6️⃣ واجهة الطبيب (د. إيهاب حشمت)
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown('<div class="main-title">🧬 CellRevive AI - Doctor Sovereign Command</div>', unsafe_allow_html=True)
    target_patient = st.selectbox("Select Patient Code / اختر كود المريض:", VALID_PATIENT_CODES)
    
    # إصلاح ثغرة استدعاء بيانات المريض المستهدف بأمان كامل
    current_p_data = get_patient_data(target_patient) or {
        'fbg': 120.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 6.8, 'weight': 80.0, 'waist': 100.0,
        'severity_score': 5.0, 'skin_analysis': 'No Analysis', 'selected_drugs': ''
    }
    
    with st.expander("📝 Metabolic & Biomarker Setup / تأسيس المؤشرات الأيضية", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("FBG (mg/dL):", value=safe_float(current_p_data['fbg'], 120.0))
            mod_ppbg = st.number_input("2h PPBG (mg/dL):", value=safe_float(current_p_data['ppbg'], 140.0))
            mod_rbg = st.number_input("RBG (mg/dL):", value=safe_float(current_p_data['rbg'], 120.0))
        with col2:
            mod_hba1c = st.number_input("HbA1c (%):", value=safe_float(current_p_data['hba1c'], 6.5))
            mod_weight = st.number_input("Weight (kg):", value=safe_float(current_p_data['weight'], 80.0))
            mod_waist = st.number_input("Waist (cm):", value=safe_float(current_p_data['waist'], 100.0))

    with st.expander("💊 Medication Protocol / بروتوكول الأدوية"):
        raw_drugs = current_p_data.get('selected_drugs', '')
        saved_drugs_list = [d.strip() for d in raw_drugs.split(',') if d.strip()] if raw_drugs else []
        mod_drugs = st.multiselect("Select Drugs:", list(EGYPTIAN_DRUG_DB.keys()), default=[d for d in saved_drugs_list if d in EGYPTIAN_DRUG_DB])

    if st.button("💾 Permanent Sync to Database / حفظ وتثبيت دائم"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': current_p_data['severity_score'], 'skin_analysis': current_p_data['skin_analysis'],
            'selected_drugs': ",".join(mod_drugs)
        }
        save_patient_data(target_patient, updated_data)
        st.success("Synced Successfully / تم الحفظ بنجاح")

# ==============================================================================
# 7️⃣ واجهة المريض الفاخرة + التحليلات البيانية العالمية (Plotly Metrics Hub)
# ==============================================================================
if st.session_state.role == "patient":
    st.markdown('<div class="main-title">🧬 CELLREVIVE AI • Living Engine Hub</div>', unsafe_allow_html=True)
    
    check_emergency_status(p_data['fbg'], "Baseline FBG")
    check_emergency_status(p_data['ppbg'], "Baseline PPBG")
    check_emergency_status(p_data['rbg'], "Baseline RBG")
    
    # 📈 لوحة التحليلات البيانية التفاعلية العالمية
    st.markdown('<div class="premium-card"><h3>📈 Advanced Metabolic Analytics / المنحنى الأيضي التفاعلي</h3>', unsafe_allow_html=True)
    raw_logs = get_all_glucose_logs(current_code)
    if raw_logs:
        df = pd.DataFrame(raw_logs, columns=["Time", "Type", "Value"])
        fig = px.line(df, x="Time", y="Value", color="Type", title="Glucose Fluctuations & Trends", markers=True)
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No logged data available for chart analytics yet. / لا توجد قراءات مسجلة لعرضها بيانياً بعد.")
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("📊 Log Glucose Instantly / تسجيل فوري للقياسات الحالية", expanded=False):
        col_g1, col_g2 = st.columns(2)
        with col_g1: g_type = st.selectbox("Timing / التوقيت:", ["Fasting (صائم)", "Post-Prandial (فاطر بعد ساعتين)", "Random (عشوائي)"])
        with col_g2: g_val = st.number_input("Value (mg/dL):", value=0.0, step=1.0)
            
        if st.button("📝 Secure Log / تدوين آمن"):
            if g_val > 0:
                log_glucose(current_code, g_type, g_val)
                
                # تحديث فوري للمستودع لربط القراءات الحالية بمحرك الـ AI مباشرة ومنع تجميد البيانات
                temp_p_data = get_patient_data(current_code) or p_data
                if "Fasting" in g_type or "صائم" in g_type: temp_p_data['fbg'] = g_val
                elif "Post-Prandial" in g_type or "فاطر" in g_type: temp_p_data['ppbg'] = g_val
                else: temp_p_data['rbg'] = g_val
                
                save_patient_data(current_code, temp_p_data)
                st.success("Saved / تم الحفظ")
                st.rerun()

    # 🥗 مختبر فحص وتطهير الوجبات الأيضي
    st.markdown('<div class="premium-card"><h3>🥗 Photo-Nutrient AI Scan / فحص وتطهير الوجبات الحية</h3>', unsafe_allow_html=True)
    uploaded_meal = st.file_uploader("Scan Meal Photo / ارفع صورة الطبق:", type=['jpg','png','jpeg'])
    if uploaded_meal and st.button("🚀 Analyze & Cleanse / تطهير الوجبة سيادياً"):
        with st.spinner("Invoking Vision Core Engine..."):
            meal_prompt = f"""
            Analyze this meal image for a patient with Insulin Resistance based on these precise parameters:
            - Fasting Glucose: {p_data['fbg']} mg/dL
            - 2h Post-Prandial Glucose: {p_data['ppbg']} mg/dL
            - Current HbA1c: {p_data['hba1c']}%
            - Active Medication Protocol: {p_data['selected_drugs']}
            
            Provide explicit modification steps and clinical biochemical logic in {'Arabic' if lang == 'العربية' else 'English'}.
            """
            res = analyze_with_gemini([uploaded_meal], meal_prompt)
            st.write(res)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size:10px; opacity:0.5; color:#ffffff !important;">CellRevive AI v4.0 - Enterprise Sovereign Edition 2026</div>', unsafe_allow_html=True)
