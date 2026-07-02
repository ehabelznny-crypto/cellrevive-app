import streamlit as st
import sqlite3
import math
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import io
import re

# ==============================================================================
# 1️⃣ الإعدادات المتقدمة والواجهة الفاخرة (2026 Luxury RTL Design)
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Living Engine",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# إعداد مفتاح API ديناميكياً من الشريط الجانبي
GEMINI_API_KEY = st.sidebar.text_input("Gemini API Key", type="password", value="")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# تصميم CSS الاحترافي - RTL ودعم إنذارات الطوارئ والواجهة الفاخرة لعام 2026
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
    .ai-badge { background: #d4af37; color: #040d1a; padding: 2px 8px; border-radius: 5px; font-size: 12px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2️⃣ تهيئة وإدارة قاعدة البيانات الدائمة والمجانية (SQLite Database Engine)
# ==============================================================================
def init_db():
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    
    # إنشاء جدول المرضى الأساسي إن لم يكن موجوداً بالبنية الأساسية
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
    
    # ترقية تلقائية آمنة لقواعد البيانات القديمة لإضافة الأعمدة الجديدة فوراً من دون فقدان البيانات
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN ppbg REAL DEFAULT 140.0")
    except sqlite3.OperationalError:
        pass  # العمود مضاف مسبقاً، تخطى بأمان
        
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN rbg REAL DEFAULT 120.0")
    except sqlite3.OperationalError:
        pass  # العمود مضاف مسبقاً، تخطى بأمان

    # إنشاء جدول سجلات السكر الفورية المحدث
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

# تشغيل تهيئة قاعدة البيانات تلقائياً
init_db()

def get_patient_data(code):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("SELECT fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs FROM patients WHERE patient_code = ?", (code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'fbg': row[0], 'ppbg': row[1], 'rbg': row[2], 'hba1c': row[3], 'weight': row[4], 'waist': row[5],
            'severity_score': row[6], 'skin_analysis': row[7], 'selected_drugs': row[8]
        }
    return None

def save_patient_data(code, data):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO patients (patient_code, fbg, ppbg, rbg, hba1c, weight, waist, severity_score, skin_analysis, selected_drugs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (code, data['fbg'], data['ppbg'], data['rbg'], data['hba1c'], data['weight'], data['waist'], data['severity_score'], data['skin_analysis'], data['selected_drugs']))
    conn.commit()
    conn.close()

def log_glucose(code, g_type, value):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO glucose_logs (patient_code, reading_time, reading_type, reading_value)
        VALUES (?, ?, ?, ?)
    """, (code, datetime.now().strftime('%Y-%m-%d %H:%M'), g_type, value))
    conn.commit()
    conn.close()

def get_glucose_logs(code):
    conn = sqlite3.connect('cellrevive_sovereign.db')
    cursor = conn.cursor()
    cursor.execute("SELECT reading_time, reading_type, reading_value FROM glucose_logs WHERE patient_code = ? ORDER BY id DESC LIMIT 5", (code,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==============================================================================
# 3️⃣ الدليل السيادي والدستور الاستراتيجي للأدوية المصرية
# ==============================================================================
EGYPTIAN_DRUG_DB = {
    "Cidophage (سيدوفاج)": {"supp": "Methyl B12 (ميثيل ب12)", "reason": "استنزاف امتصاص فيتامين ب12 على المدى الطويل وتضرر الأعصاب الطرفية"},
    "Glucophage (جلوكوفاج)": {"supp": "Methyl B12 (ميثيل ب12)", "reason": "سوء امتصاص فيتامين ب12 الممتد وتأثر الميتوكوندريا"},
    "Deltacortril (ديلتاكورتريل)": {"supp": "Potassium & Magnesium (بوتاسيوم وماغنسيوم)", "reason": "احتباس الصوديوم، هدم الكتلة العضلية الحيوية، ورفع مقاومة الإنسولين"},
    "Lasix (لازكس)": {"supp": "Thiamine (B1) & Potassium (ثيامين ب1 وبوتاسيوم)", "reason": "غسيل وتفريغ الميتوكوندريا من المعادن الأساسية ومستنفذات الطاقة الحيوية"},
    "Lipitor (ليبيتور)": {"supp": "CoQ10 (200mg) (إنزيم كيو 10)", "reason": "تثبيط إنتاج طاقة الخلية واستنزاف ميتوكوندريا العضلات والقلب"},
    "Ator (آتور)": {"supp": "CoQ10 (200mg)", "reason": "استنزاف إنزيم الطاقة الميتوكوندري الحرج"},
    "Crestor (كريستور)": {"supp": "CoQ10 + Vitamin D3", "reason": "تثبيط إنزيم الكبد وتعب العضلات الأيضي"},
    "Forxiga (فورسيجا)": {"supp": "Electrolytes & Hydration Protocol", "reason": "طرد السكر عن طريق البول ومخاطر الجفاف الميكروبي وفقد الأملاح"},
    "Jardiance (جاردينس)": {"supp": "Electrolytes & High Hydration", "reason": "إدرار السكر الكلوي واستنزاف السوائل الخلوية"},
    "Mounjaro (مونجارو)": {"supp": "Essential Amino Acids & Bio-Protein", "reason": "تبديد ونقص الكتلة العضلية السريع نتيجة سد الشهية المفرط"},
    "Ozempic (أوزمبيك)": {"supp": "Digestive Enzymes & Amino Acids", "reason": "بطء حركة المعدة الشديد والحاجة لدعم الهضم وبناء العضلات"},
    "Victoza (فيكتوزا)": {"supp": "Pancreatic & Muscle Support", "reason": "تحفيز البنكرياس المستمر والحاجة للمقاصة الجينية للأنسجة"},
    "Concor (كونكور)": {"supp": "CoQ10 & Melatonin", "reason": "تقليل إنتاج الميلاتونين الليلي وتثبيط طاقة بيتا الخلوية"},
    "Exforge (إكسفورج)": {"supp": "Zinc & Ginkgo Biloba", "reason": "تأثير على توسعة الأوعية والحاجة لحماية المغذيات الدقيقة في الشرايين"},
    "Amaryl (أماريل)": {"supp": "Alpha-Lipoic Acid (ألفا ليبويك أسيد)", "reason": "عصر البنكرياس المستمر والحاجة لحماية الأعصاب من الإجهاد التأكسدي"}
}

# ==============================================================================
# 4️⃣ محرك الرؤية الحاسوبية (Vision AI Engine) والمستخلص الرقمي
# ==============================================================================
def analyze_with_gemini(images, prompt):
    if not GEMINI_API_KEY:
        return "⚠️ يرجى إدخال مفتاح API في الشاشة الجانبية لتفعيل نظام الرؤية الحية."
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        content = [prompt]
        for img in images:
            content.append(Image.open(img))
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال بسيرفر الذكاء الاصطناعي: {str(e)}"

def extract_severity_score(text):
    match = re.search(r'(?:score|الدرجة|الحدة|مستوى)[:\s\-]*([0-9\.]+)', text, re.IGNORECASE)
    if match:
        try:
            score = float(match.group(1))
            return min(max(score, 1.0), 10.0)
        except:
            pass
    return 5.0

# دالة مخصصة لمراقبة مستويات الخطر وإطلاق الإنذارات الطبية الفورية
def check_emergency_status(value, context_phrase=""):
    if value > 0:
        if value < 70.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إشارة تحذيرية سيادية خطيرة (هبوط حاد في السكر): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه حرج جداً ({context_phrase}):</b> تم رصد هبوط حاد بمستوى السكر تحت النطاق الآمن. يرجى تناول كربوهيدرات سريعة الامتصاص فوراً ومراجعة الدكتور إيهاب حشمت أو التوجه إلى قسم الطوارئ بالمستشفى دون أي تأخير منعاً لغيبوبة نقص السكر!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        elif value > 300.0:
            st.markdown(f"""
                <div class="emergency-card">
                    <h3 style="color:#ff4b4b; margin:0 0 10px 0;">🚨 إشارة تحذيرية سيادية خطيرة (ارتفاع مفرط وحاد): {value} mg/dL</h3>
                    <p style="color:#ffffff !important; font-size:15px; margin:0;">
                        <b>تنبيه حرج جداً ({context_phrase}):</b> مستوى السكر يتجاوز الحد الحرج الآمن للخلية الحية. أنت في دائرة خطر الحماض الكيتوني أو متلازمة الارتفاع الأسموزي. يجب مراجعة الطبيب المعالج فوراً أو الانتقال فوراً إلى طوارئ المستشفى لضبط الجرعات وإنقاذ الموقف خلوياً!
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 5️⃣ بوابة العبور الرقمية - التحقق والربط التلقائي بالكود
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
VALID_PATIENT_CODES = ["CR-PATIENT-77", "CR-PATIENT-99", "CR-PATIENT-101", "CR-SOHAG-2026"]

if 'auth_code' not in st.session_state: st.session_state.auth_code = ""
if 'is_auth' not in st.session_state: st.session_state.is_auth = False
if 'role' not in st.session_state: st.session_state.role = None

if not st.session_state.is_auth:
    st.markdown('<div class="main-title">🧬 CELLREVIVE AI • بوابـة العبـور السياديـة</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">المنظومة العالمية للترميم الخلوي وعكس الأمراض الأيضية - 2026</div>', unsafe_allow_html=True)
    
    with st.container():
        input_code = st.text_input("أدخل كود الوصول الرقمي الخاص بك (المحفوظ على موبايلك):", type="password")
        if st.button("تفعيل الاتصال الآمن والمشفر"):
            if input_code == MASTER_CODE:
                st.session_state.is_auth = True
                st.session_state.role = "doctor"
                st.session_state.auth_code = MASTER_CODE
                st.success("أهلاً بك يا دكتور إيهاب في القيادة السيادية للمنظومة الحية.")
                st.rerun()
            elif input_code in VALID_PATIENT_CODES:
                st.session_state.is_auth = True
                st.session_state.role = "patient"
                st.session_state.auth_code = input_code
                st.success("تم التحقق من الكود بنجاح. جاري استدعاء ملفك الطبي الآمن...")
                st.rerun()
            else:
                st.error("الكود غير صحيح أو منتهي الصلاحية. يرجى مراجعة العيادة.")
    st.stop()

# ==============================================================================
# 6️⃣ استدعاء البيانات وحماية المنظومة من الفقدان التصفيري
# ==============================================================================
current_code = st.session_state.auth_code
p_data = get_patient_data(current_code)
if not p_data:
    p_data = {
        'fbg': 130.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 7.2, 'weight': 85.0, 'waist': 105.0,
        'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': ''
    }
    if st.session_state.role == "patient":
        save_patient_data(current_code, p_data)

# ==============================================================================
# 7️⃣ لوحة تحكم الطبيب المعالج (د. إيهاب حشمت) لإدخال وتأسيس الثوابت
# ==============================================================================
if st.session_state.role == "doctor":
    st.markdown(f'<div style="text-align:left; color:#d4af37; font-size:12px;">لوحة تحكم الطبيب العليا المعالج الحية</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">إدارة وتأسيس ملفات المرضى الاستراتيجية</div>', unsafe_allow_html=True)
    
    target_patient = st.selectbox("اختر كود المريض لتأسيس أو مراجعة بياناته الحيوية:", VALID_PATIENT_CODES)
    current_p_data = get_patient_data(target_patient) or {
        'fbg': 120.0, 'ppbg': 140.0, 'rbg': 120.0, 'hba1c': 6.8, 'weight': 80.0, 'waist': 100.0,
        'severity_score': 5.0, 'skin_analysis': 'لم يتم الفحص بعد', 'selected_drugs': ''
    }
    
    with st.expander("📝 تأسيس المؤشرات الحيوية والمخبرية الصارمة للمريض", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            mod_fbg = st.number_input("سكر صائم أساسي (mg/dL):", value=float(current_p_data['fbg']))
            mod_ppbg = st.number_input("سكر فاطر بعد ساعتين أساسي (mg/dL):", value=float(current_p_data['ppbg']))
            mod_rbg = st.number_input("سكر عشوائي أساسي (mg/dL):", value=float(current_p_data['rbg']))
        with col2:
            mod_hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=float(current_p_data['hba1c']))
            mod_weight = st.number_input("الوزن (كجم):", value=float(current_p_data['weight']))
            mod_waist = st.number_input("محيط الخصر (سم):", value=float(current_p_data['waist']))
        
        # تفعيل الرصد والإنذار الفوري داخل لوحة الطبيب أثناء الإدخال
        check_emergency_status(mod_fbg, "سكر صائم للمريض")
        check_emergency_status(mod_ppbg, "سكر فاطر للمريض")
        check_emergency_status(mod_rbg, "سكر عشوائي للمريض")
            
    with st.expander("💊 تعيين بروتوكول الأدوية المصرية الحالية للمريض", expanded=False):
        saved_drugs_list = current_p_data['selected_drugs'].split(',') if current_p_data['selected_drugs'] else []
        mod_drugs = st.multiselect("اختر الأدوية من الدستور المصري الحالي:", list(EGYPTIAN_DRUG_DB.keys()), default=[d for d in saved_drugs_list if d in EGYPTIAN_DRUG_DB])
        
    with st.expander("📸 فحص بصمة الجلد نسيجياً وتحديد درجة المقاومة ديناميكياً", expanded=False):
        uploaded_skin = st.file_uploader("ارفع صور العلامات الجلدية (الرقبة، الإبط):", type=['jpg','png','jpeg'], key="doc_skin")
        mod_severity = current_p_data['severity_score']
        mod_skin_analysis = current_p_data['skin_analysis']
        if uploaded_skin and st.button("تحليل البصمة النسيجية واستخلاص النتيجة حياً"):
            with st.spinner("يجري تحليل الذكاء الاصطناعي الأيضي للجلد عبر Gemini 2.5..."):
                prompt = """بصفتك خبير صيدلة جينية وطب جلدية أيضي، حلل صور الجلد المرفقة لعلامات الشواك الأسود والزوائد الجلدية. 
                أعط تقريراً باللغة العربية واكتب في نهاية النص بوضوح: 'Severity Score: X' حيث X رقم حقيقي من 1 إلى 10 يعبر عن حدة مقاومة الإنسولين."""
                mod_skin_analysis = analyze_with_gemini([uploaded_skin], prompt)
                mod_severity = extract_severity_score(mod_skin_analysis)
                st.markdown(f"<b>مستوى المقاومة المستخلص ديناميكياً: {mod_severity} / 10</b>", unsafe_allow_html=True)
                st.write(mod_skin_analysis)
                
    if st.button("💾 حفظ وتثبيت ملف المريض بشكل permanent في قاعدة البيانات"):
        updated_data = {
            'fbg': mod_fbg, 'ppbg': mod_ppbg, 'rbg': mod_rbg, 'hba1c': mod_hba1c, 'weight': mod_weight, 'waist': mod_waist,
            'severity_score': mod_severity, 'skin_analysis': mod_skin_analysis,
            'selected_drugs': ",".join(mod_drugs)
        }
        save_patient_data(target_patient, updated_data)
        st.success(f"تم حفظ وتشفير ملف المريض {target_patient} بنجاح دون أي خلل برمجي.")

# ==============================================================================
# 8️⃣ واجهة المريض السريعة والذكية - تجربة تناول الوجبة بكبسة زر واحدة مع الإنذار
# ==============================================================================
if st.session_state.role == "patient":
    st.markdown(f'<div style="text-align:left; color:#d4af37; font-size:12px;">مرحباً بك • كود الوصول الآمن: {current_code}</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">🧬 منظومة المتابعة الفورية للترميم الخلوي</div>', unsafe_allow_html=True)
    
    # استعراض إنذار فوري للمريض بناءً على آخر ثوابت مخزنة في ملفه قبل تصفح الأقسام
    check_emergency_status(p_data['fbg'], "آخر قراءة سكر صائم مسجلة")
    check_emergency_status(p_data['ppbg'], "آخر قراءة سكر فاطر مسجلة")
    check_emergency_status(p_data['rbg'], "آخر قراءة سكر عشوائي مسجلة")

    with st.expander("📊 سجل متابعة السكر الفورية (صائم / فاطر / عشوائي)", expanded=False):
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            g_type = st.selectbox("نوع وتوقيت القياس الحالي الآن:", ["سكر صائم", "سكر فاطر (بعد ساعتين)", "سكر عشوائي (غير مرتبط بوجبة)"])
        with col_g2:
            g_val = st.number_input("قراءة السكر المقاسة بالجهاز (mg/dL):", value=0.0, step=1.0)
            
        if st.button("📝 تسجيل القراءة فوراً في السجل الدائم"):
            if g_val > 0:
                log_glucose(current_code, g_type, g_val)
                # تحديث القيمة الحية في جدول المريض فوراً لضمان الاستمرارية وعمل محرك الطوارئ
                temp_p_data = get_patient_data(current_code)
                if g_type == "سكر صائم": temp_p_data['fbg'] = g_val
                elif g_type == "سكر فاطر (بعد ساعتين)": temp_p_data['ppbg'] = g_val
                else: temp_p_data['rbg'] = g_val
                save_patient_data(current_code, temp_p_data)
                st.success("تم تدوين القراءة بنجاح في ملفك الطبي الدائم.")
                st.rerun()
            else:
                st.warning("يرجى إدخال قراءة صحيحة.")
                
        # عرض شاشة فحص الطوارئ اللحظية بعد الإدخال مباشرة لضمان سلامة المريض
        check_emergency_status(g_val, f"القراءة المدخلة حالياً كـ {g_type}")
                
        logs = get_glucose_logs(current_code)
        if logs:
            st.markdown("<b>آخر 5 قراءات محفوظة للرجوع إليها خلوياً:</b>", unsafe_allow_html=True)
            for l in logs:
                st.caption(f"📅 {l[0]} | {l[1]}: {l[2]} mg/dL")

    st.markdown('<div class="premium-card"><h3>🥗 مختبر فحص وتطهير الوجبات الأيضي الفوري</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color:#e0e0e0 !important;">كل ما عليك فعله هو التقاط صورة لوجبتك الحالية الآن، وسيقوم محرك الترميم الخلوي بضبطها فوراً بناءً على حالتك الصحية ومستويات السكر المحفوظة لدينا.</p>', unsafe_allow_html=True)
    
    uploaded_meal = st.file_uploader("📸 التقط أو ارفع صورة وجبتك الحالية هنا:", type=['jpg','png','jpeg'])
    
    if uploaded_meal and st.button("🚀 تحليل وتطهير الوجبة لسلامة خلاياي بدقة سيادية"):
        with st.spinner("يجري استدعاء تاريخك الطبي وتحليل مكونات الطبق هندسياً..."):
            
            saved_drugs = p_data['selected_drugs']
            homa_ir = (p_data['fbg'] * 25) / 405
            
            meal_prompt = f"""
            بصفتك كبير مستشاري الطب الأيضي والترميم الخلوي، وبناءً على البيانات الطبية المحفوظة والدائمة للمريض التالي:
            - السكر الصائم الأساسي الحالي: {p_data['fbg']} mg/dL
            - السكر الفاطر بعد ساعتين الحركي: {p_data['ppbg']} mg/dL
            - السكر العشوائي الأخير: {p_data['rbg']} mg/dL
            - السكر التراكمي (HbA1c): {p_data['hba1c']}%
            - مؤشر مقاومة الإنسولين التقريبي (HOMA-IR): {round(homa_ir, 2)}
            - الأدوية المصرية المستهلكة: {saved_drugs}
            - درجة حدة المقاومة الجلدية نسيجياً (Severity Score): {p_data['severity_score']}/10
            
            حلل صورة الوجبة المرفقة بدقة متناهية وسيادية وقدم تقريراً فورياً يحتوي على:
            1. المكونات المرصودة بدقة وحجم النشويات والبروتينات بالوحدات المنزلية.
            2. التعديل الإجباري والفوري اللازم على هذه الوجبة (ما يجب حذفه، استبداله، أو تقليله) لتتلاءم 100% مع مقاومة الإنسولين ومستويات السكر المقاسة لديه وحماية خلاياه من قفزات الجلوكوز.
            3. بروتوكول التطهير الحيوي (مثل خل التفاح العضوي، ترتيب تناول الطعام الحاسم) لضمان عدم حدوث قفزة سكر حادة (Glucose Spike).
            4. تنبيه خاص بالمقاصة الدوائية والمكملات بناءً على أدويته المحفوظة في قاعدة بيانات المنصة لتعويض استنزاف الميتوكوندريا.
            
            الرد باللغة العربية بأسلوب طبي صارم، واثق، وسيادي.
            """
            
            meal_analysis_result = analyze_with_gemini([uploaded_meal], meal_prompt)
            
            st.markdown("<h4>📋 التقرير الفوري وتظبيط الوجبة السيادي:</h4>", unsafe_allow_html=True)
            st.write(meal_analysis_result)
            
            final_report_text = f"""
            تقرير منظومة CELLREVIVE AI للوجبات والمتابعة
            ------------------------------------------
            كود المريض: {current_code}
            تاريخ الفحص الحركي: {datetime.now().strftime('%Y-%m-%d %H:%M')}
            المؤشرات الثابتة والمسجلة في الملف:
            - السكر الصائم: {p_data['fbg']} mg/dL | الفاطر: {p_data['ppbg']} mg/dL | العشوائي: {p_data['rbg']} mg/dL
            - التراكمي: {p_data['hba1c']}%
            - الأدوية المستعملة: {saved_drugs}
            
            توجيهات تظبيط الوجبة الحالية الحية للتطهير الخلوي:
            {meal_analysis_result}
            ==========================================
            """
            st.download_button("📥 تحميل وتصدير هذا التقرير لإرساله للطبيب المعالج", final_report_text, file_name=f"CellRevive_Meal_Report_{current_code}.txt")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size:10px; opacity:0.5; color:#ffffff !important;">CellRevive AI Sovereign Engine v3.5 - 2026 Free & Protected Database System</div>', unsafe_allow_html=True)
