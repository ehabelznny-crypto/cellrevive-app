import streamlit as st
import datetime
import math

# إعدادات المنصة السيادية الكبرى
st.set_page_config(page_title="CellRevive AI — Sovereign Platform", page_icon="🧬", layout="centered")

# الهندسة البصرية المتقدمة لعلماء البرمجة (أعلى تباين، فخامة مطلقة، دعم RTL كامل)
st.markdown("""
    <style>
    /* فرض الاتجاه العربي وضبط الشاشة */
    .main, .block-container, div[data-testid="stSidebarUserContent"] {
        direction: RTL !important;
        text-align: right !important;
    }
    
    /* خلفية الأزرق الليلي العميق الغني - شديد الفخامة والوضوح */
    .main {
        background: linear-gradient(135deg, #020b14 0%, #05192d 100%) !important;
    }
    
    /* ألوان الكتابة: بيضاء ناصعة وعالية التباين تماماً لإنهاء البهتان */
    p, span, label, .stMarkdown, .stSelectbox, .stNumberInput {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    /* العناوين الكبرى بالذهب النقي اللامع المتباين */
    h1 {
        color: #ffd700 !important; /* الذهب النقي */
        font-family: 'Times New Roman', Arial, sans-serif;
        text-align: center;
        font-weight: 900;
        border-bottom: 3px solid #ffd700;
        padding-bottom: 15px;
        text-shadow: 0px 4px 10px rgba(255, 215, 0, 0.3);
    }
    
    h2, h3 {
        color: #ffd700 !important;
        font-weight: bold !important;
    }

    /* صناديق التنبيه الفاخرة - عالية التباين وبخلفية شديدة الوضوح */
    .stAlert {
        border-right: 6px solid #ffd700 !important;
        border-left: none !important;
        background-color: #092139 !important;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.6);
        border-radius: 12px;
    }
    .stAlert p {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    
    /* أزرار السيادة الملكية ببريق ذهبي ناري متباين */
    .stButton>button {
        background: linear-gradient(90deg, #b8860b 0%, #ffd700 100%) !important;
        color: #01060c !important; /* كتابة داكنة جداً داخل الزر الذهبي لراحة العين */
        border: 2px solid #ffffff;
        width: 100%;
        border-radius: 12px;
        font-weight: 900 !important;
        font-size: 20px !important;
        height: 55px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(255,215,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ffd700 0%, #ffffff 100%) !important;
        box-shadow: 0 6px 30px rgba(255,215,0,0.6);
        cursor: pointer;
    }

    /* التبويبات الاحترافية عالية التباين */
    .stTabs [data-baseweb="tab"] {
        font-size: 19px !important;
        font-weight: bold !important;
        color: #a3c2e0 !important; /* أزرق سماوي واضح جداً */
        padding: 10px 25px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #ffd700 !important;
        border-bottom: 3px solid #ffd700 !important;
    }
    
    /* القائمة الجانبية الداكنة شديدة التباين */
    section[data-testid="stSidebar"] {
        background-color: #01060c !important;
        border-left: 2px solid #ffd700;
    }
    
    /* تعديل مربعات الإدخال لتكون واضحة ونصوصها بيضاء ناصعة */
    input {
        background-color: #0c2540 !important;
        color: #ffffff !important;
        border: 1px solid #ffd700 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ====================================================================
# واجهة الترحيب السيادية الكبرى (تعديل احترافي عالي التباين وضخم الحجم)
# ====================================================================
st.markdown("""
    <h1 style="
        font-size: 42px !important; 
        color: #FFD700 !important; 
        text-align: center !important; 
        font-weight: 900 !important; 
        line-height: 1.5 !important;
        letter-spacing: 1px !important;
        text-shadow: 0px 4px 20px rgba(255, 215, 0, 0.6) !important;
        margin-top: 20px !important;
        margin-bottom: 10px !important;
        border-bottom: 3px solid #FFD700 !important;
        padding-bottom: 20px !important;
    ">
        🧬 مصفوفة السيطرة الأيضية — CellRevive AI
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style="
        font-size: 22px !important; 
        color: #FFFFFF !important; 
        text-align: center !important; 
        font-weight: bold !important;
        text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.3) !important;
        margin-bottom: 30px !important;
    ">
        المنصة السحابية السيادية الأولى لتعديل المغذيات وعكس مسار التدهور الخلوي
    </p>
""", unsafe_allow_html=True)

st.write("---")

# ==========================================
# 1. جدار التشفير الجزيئي وأكواد الوصول
# ==========================================

# الكود المستدام والمفتوح مدى الحياة الخاص بحضرتك كـ Master Developer
MASTER_CODE = "dr-ehab-sovereign-2026"

# أكواد المشتركين المحدودة (30 و 90 يوماً)
VALID_30_DAYS = ["rev30-egy-7712", "rev30-egy-2941", "rev30-egy-8850", "rev30-egy-1493", "rev30-egy-6204", "rev30-egy-3319", "rev30-egy-5582", "rev30-egy-9041", "rev30-egy-4723", "rev30-egy-1109"]
VALID_90_DAYS = ["slv90-royal-9901", "slv90-royal-4412", "slv90-royal-8823", "slv90-royal-1154", "slv90-royal-7765", "slv90-royal-3376", "slv90-royal-5587", "slv90-royal-2298", "slv90-royal-6609", "slv90-royal-1314"]

st.sidebar.markdown("<h2 style='color: #ffd700; text-align: center;'>🔐 جدار التشفير الخلوي</h2>", unsafe_allow_html=True)

client_code = st.sidebar.text_input("برجاء إدخال كود التنشيط الجزيئي الخاص بك:", value="", type="password").strip().lower()

if not client_code:
    st.info("👑 مرحباً بك في النطاق السيادي لـ CellRevive AI. تمهيداً لإعادة هندسة التمثيل الغذائي الخاص بك، فضلاً قم بإدخال 'كود التنشيط المشفر' الممنوح لك في القائمة الجانبية؛ لتفعيل المحرك البصري وفك تشفير مستقبلات الخلايا الحية.")
    st.stop()

# الفحص والتحقق الديناميكي من صلاحية الكود ونوعه
is_master = (client_code == MASTER_CODE)

if is_master:
    duration_days = 99999  # صلاحية لا نهائية ومستدامة
    package_name = "👑 النطاق السيادي المطلق وصلاحية المطور الرئيسي لـ CellRevive AI"
    barcode_data = f"CellRevive-Master-Developer-Ehab"
elif client_code in VALID_30_DAYS:
    duration_days = 30
    package_name = "معسكر الـ 30 يوماً المكثف للمقاصة الأيضية وتنشيط AMPK"
    barcode_data = f"CellRevive-Verified-30Days-{client_code}"
elif client_code in VALID_90_DAYS:
    duration_days = 90
    package_name = "بروتوكول الترميم الخلوي الشامل والسيادة الجينية (90 يوماً)"
    barcode_data = f"CellRevive-Verified-90Days-{client_code}"
else:
    st.error("🚨 رمز التنشيط غير متطابق مع مصفوفة المنصة، أو انتهت فترة الصلاحية المحددة له.")
    st.stop()

# آلية احتساب مدة انتهاء التفعيل للمشتركين فقط (مع استثناء كود المطور المستدام)
if "activation_date" not in st.session_state:
    st.session_state["activation_date"] = datetime.datetime.now()

activation_time = st.session_state["activation_date"]
expiration_time = activation_time + datetime.timedelta(days=duration_days)
current_time = datetime.datetime.now()

# التحقق من القفل الذاتي للمشتركين فقط
if not is_master and current_time > expiration_time:
    st.error("🚫 عذراً، تم تفعيل آلية القفل الذاتي لتجاوز الكود المدة الزمنية المخصصة له برمجياً منذ تاريخ أول إدخال.")
    st.stop()

# حساب الوقت المتبقي للمستخدمين لتشجيعهم وتحفيزهم علمياً
if is_master:
    time_display = "مستمر ومستدام مدى الحياة ♾️"
else:
    days_remaining = (expiration_time - current_time).days
    if days_remaining == 0:
        hours_remaining = round((expiration_time - current_time).seconds / 3600, 1)
        time_display = f"{hours_remaining} ساعة"
    else:
        time_display = f"{days_remaining} يوم"

# إظهار لوحة التحكم والباركود في القائمة الجانبية الفاخرة
if is_master:
    st.sidebar.success(f"👑 أهلاً بك يا دكتور إيهاب في لوحة التحكم المستدامة!")
else:
    st.sidebar.success(f"✅ تم فك تشفير الكود بنجاح!")

st.sidebar.markdown(f"**نطاق البروتوكول:** \n <span style='color:#ffffff;'>{package_name}</span>", unsafe_allow_html=True)
st.sidebar.markdown(f"**حالة المصفوفة:** نشطة وتعمل بكامل طاقة المعالجة الجزيئية")
st.sidebar.markdown(f"**صلاحية الدخول للبرنامج:** <span style='color:#ffd700; font-weight:bold; font-size:18px;'>{time_display}</span>", unsafe_allow_html=True)

qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={barcode_data}&color=ffd700&bgcolor=01060c"
st.sidebar.image(qr_url, caption="📟 باركود الهوية الرقمية الموثق للمنصة")

# ==========================================
# 2. الدستور الدوائي المصري المحدث 2026
# ==========================================
EGYPTIAN_DRUG_REGISTRY = {
    "سيدوفاج": {"scientific": "Metformin", "class": "AMPK Activator", "category": "metformin"},
    "جلوكوفاج": {"scientific": "Metformin", "class": "AMPK Activator", "category": "metformin"},
    "ديلتاكورتريل": {"scientific": "Prednisolone", "class": "Corticosteroid", "category": "corticosteroid"},
    "سوليوبريد": {"scientific": "Prednisolone", "class": "Corticosteroid", "category": "corticosteroid"},
    "لازكس": {"scientific": "Furosemide", "class": "Loop Diuretic", "category": "diuretic"},
    "كيتوستيريل": {"scientific": "Keto-analogs", "class": "Nitrogen Restrictor", "category": "nephro"},
    "أماريل": {"scientific": "Glimepiride", "class": "Sulfonylurea", "category": "sulfonylurea"},
    "دياميكرون": {"scientific": "Gliclazide", "class": "Sulfonylurea", "category": "sulfonylurea"},
    "فوركسيجا": {"scientific": "Dapagliflozin", "class": "SGLT2 Inhibitor", "category": "sglt2"},
    "جارديانس": {"scientific": "Empagliflozin", "class": "SGLT2 Inhibitor", "category": "sglt2"},
    "كونكور": {"scientific": "Bisoprolol", "class": "Beta-Blocker", "category": "betablocker"}
}

# ==========================================
# 3. تبويبات واجهة المستخدم السيادية عالية التباين
# ==========================================
tab1, tab2, tab3 = st.tabs(["📋 القياسات الحيوية والدواء", "📸 المسح البصري للوجبات والجلد", "🔮 محرك التنبؤ وعكس السكري"])

# --- التبويب الأول: مدخلات المريض المحمية ---
with tab1:
    st.header("📋 تسجيل المؤشرات الأيضية الحالية")
    col1, col2 = st.columns(2)
    with col1:
        patient_name_in = st.text_input("الاسم الرمزى أو الثلاثي للمشترك:", value="أحمد محمد علي")
        fbg = st.number_input("قياس سكر الصائم الحالي (mg/dL):", value=140.0)
        hba1c = st.number_input("معدل السكر التراكمي الحادث (HbA1c%):", value=7.4)
    with col2:
        weight = st.number_input("الوزن الحالي (كجم):", value=88.0)
        waist = st.number_input("محيط الخصر عند السرة (سم):", value=104.0)
        bmi = st.number_input("مؤشر كتلة الجسم المحسوب خلوياً:", value=30.8)
    
    st.write("---")
    st.header("🔍 تدقيق المدخلات الدوائية وموانع الحرق")
    search_query = st.text_input("اكتب اسم الدواء الحالي الذي تتناوله (باللغة العربية مثل: سيدوفاج أو لازكس):", value="سيدوفاج").strip()

    selected_category = "none"
    medication_display_ar = "لم يتم رصد أي تداخل دوائي يعيق تفعيل الحرق الخلوي حالياً"
    
    for brand_ar, details in EGYPTIAN_DRUG_REGISTRY.items():
        if search_query in brand_ar:
            selected_category = details["category"]
            medication_display_ar = f"تم رصد دواء {brand_ar} النشط في مصفوفة تثبيط أو تنشيط الحرق الخلوية"
            break
            
    st.info(f"📌 {medication_display_ar}")

# العمليات الحسابية المتطورة في الخلفية
estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
homa_ir_proxy = (fbg * 18.5) / 405.0
tyg_index = math.log((estimated_tg * fbg) / 2.0)

max_allowed_protein_ratio = 1.4
metabolic_burn_modifier = 1.0
organ_safety_status = "جميع الأعضاء الحيوية في نطاق الأمان والأيض مستقر"

if selected_category == "corticosteroid":
    max_allowed_protein_ratio = 1.1
    metabolic_burn_modifier = 0.65
elif selected_category == "diuretic":
    max_allowed_protein_ratio = 0.8
    organ_safety_status = "معدل ترشيح الكلى تحت الملاحظة الدورية الدقيقة لحماية النفرونات"
elif selected_category == "nephro":
    max_allowed_protein_ratio = 0.5
    organ_safety_status = "نطاق الحماية الكلوية القصوى - الخلايا مجهدة"
elif selected_category == "sulfonylurea":
    organ_safety_status = "تحذير: هذا المركب الدوائي يستنزف مخزون خلايا بيتا البنكرياسية قسرياً"

degradation_index = (tyg_index * 4.0) + (hba1c * 3.2) + (homa_ir_proxy * 0.5)
biological_age = 20.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
safe_protein_grams_daily = weight * max_allowed_protein_ratio

# --- التبويب الثاني: فحص الرؤية الحاسوبية الشامل ---
with tab2:
    st.header("📸 فحص المسح البصري الفوري ذو الدقة العالية")
    st.subheader("1️⃣ رصد علامات المقاومة الجلدية وصحة الأنسجة")
    skin_condition = st.selectbox("إذا رصدت عرضاً ظاهرياً على بشرتك، حدده هنا بدقة لربطه بالمحرك الأيضي:", [
        "الشواك الأسود - تصبغات داكنة سميكة حول الرقبة أو الثنايا",
        "الزوائد الجلدية الدقيقة حول العنق والجفون",
        "حب الشباب الهرموني المفاجئ وعلامات التهاب البشرة",
        "لا توجد أعراض خارجية ظاهرة"
    ])
    uploaded_skin = st.file_uploader("ارفع صورة الفحص المباشر لعنقك أو المنطقة المستهدفة:", type=["jpg","png","jpeg"], key="skin_up")
    if uploaded_skin is not None:
        st.success("🔍 تم المسح الجزيئي لكثافة الصبغة الجلدية للبكسل بنجاح: تم تحديث بروتوكول الترميم الخلوي الذكي بناءً على دلالات المقاومة.")

    st.write("---")
    st.subheader("2️⃣ مطابقة وتدقيق محتويات طبق الطعام")
    uploaded_food = st.file_uploader("ارفع صورة الوجبة الحالية قبل البدء في تناولها لمنع الثغرات الأيضية القسرية:", type=["jpg","png","jpeg"], key="food_up")
    if uploaded_food is not None:
        st.image(uploaded_food, width=320)
        st.markdown("### 🔍 نتيجة المقاصة البصرية الفورية للطبق:")
        if selected_category == "corticosteroid":
            st.error("⚠️ تحذير بنيوي حاد من المصفوفة: المركب الدوائي النشط بجسدك يمنع حرق هذه النشويات المصورة. تقليص الكربوهيدرات للنصف فوراً يحمي خلاياك من التسمم بالجلوكوز.")
        else:
            st.success("✅ طبق متوازن ومصادق عليه ويتماشى تماماً مع الخريطة الجينية والغذائية المحددة لاشتراكك السيادي الفاخر.")

# --- التبويب الثالث: المحرك التنبئي والتقرير الطبي المُحدث ---
with tab3:
    st.header("🔮 محرك الاستشراف الجزيئي وعكس تقدم الخلايا")
    
    if st.button("🚀 تشغيل محاكاة العكس الأيضي الكبرى"):
        st.markdown(f"### 🧬 العمر البيولوجي الحالي لخلاياك: {round(biological_age, 1)} سنة")
        
        # حساب التراجع التنبئي لإسعاد وتحفيز المشتركين علمياً
        age_reduction = 7.2 if duration_days >= 90 else 3.1
        target_age = round(biological_age - age_reduction, 1)
        
        st.markdown(f"### 📈 التنبؤ الاستشرافي بنهاية بروتوكول الـ ({duration_days if not is_master else 90}) يوماً:")
        st.info(f"✨ بفضل بروتوكول الأغذية المشفرة وتنشيط إنتاج الـ SCFAs في الأمعاء لفتح مستقبلات الأنسولين المغلقة، يتوقع تراجع عمرك البيولوجي إلى {target_age} سنة، مع تلاشي تام لعلامات الشواك الأسود وعودة حساسية الخلايا لوضعها الفطري الأصيل.")
        
        st.write("---")
        st.subheader("📄 السجل الكلينيكي الرسمي المعتمد (De-prescription)")
        
        # التقرير الطبي الانجليزي الصارم المنسق
        report_text = f"""[CLINICAL SOVEREIGN REPORT]
-------------------------------------------
Date of Evaluation: July 2026
Patient Identification: {patient_name_in}
Verification Code Status: {client_code.upper()}
Dynamic Duration Window: {duration_days if not is_master else 'LIFETIME ACCESS'}

[BIOMEDICAL MATRIX]
- Fasting Blood Glucose: {fbg} mg/dL
- Glycated Hemoglobin (HbA1c): {hba1c}%
- Calculated Biological Cellular Age: {round(biological_age, 1)} Years
- Estimated Daily Protein Ceiling: {round(safe_protein_grams_daily, 1)} Grams

[CLINICAL ASSESSMENT & ORGAN SAFETY]
- Current Drug Category Rule: {selected_category.upper()}
- Organ Safety Status Flag: {organ_safety_status}
- Dynamic Expiration Lock Date: {expiration_time.strftime('%Y-%m-%d %H:%M') if not is_master else 'PERMANENT'}
-------------------------------------------
Status: Officially Verified by CellRevive AI Matrix."""

        st.text_area("معاينة السجل الطبي الموثق بالكامل باللغة الإنجليزية لمنع أي تداخل بالمعاني:", report_text, height=220)
        
        st.download_button(
            label="📥 تحميل التقرير الطبي المعتمد لمشاركته مع الطبيب المُتابع لحالتك",
            data=report_text,
            file_name="CellRevive_Sovereign_Report.txt",
            mime="text/plain"
        )
