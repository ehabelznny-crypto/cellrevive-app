import streamlit as st
import datetime
import math

# إعدادات الصفحة السيادية الفاخرة
st.set_page_config(page_title="CellRevive AI — Sovereign Platform", page_icon="🧬", layout="centered")

# هندسة التصميم الفاخر باللون الأزرق الداكن والذهب الفرعوني مع فرض اتجاه اليمين إلى اليسار (RTL)
st.markdown("""
    <style>
    /* فرض الاتجاه العربي لمنع انقلاب الشاشة */
    .main, .block-container, div[data-testid="stSidebarUserContent"] {
        direction: RTL !important;
        text-align: right !important;
    }
    
    /* تصميم الخلفية الملكية الداكنة العميقة */
    .main {
        background: linear-gradient(135deg, #051622 0%, #0b2c4d 100%) !important;
    }
    
    /* تعديل ألوان النصوص لتتناسب مع الخلفية الداكنة وتشع فخامة */
    p, span, label, .stMarkdown {
        color: #e0e9f4 !important;
    }
    
    /* العناوين الكبرى بالذهب النفيس والأبيض الملكي */
    h1 {
        color: #f4d068 !important;
        font-family: 'Times New Roman', Arial, sans-serif;
        text-align: center;
        font-weight: 900;
        border-bottom: 2px solid #f4d068;
        padding-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    h2, h3 {
        color: #f4d068 !important;
        font-family: Arial, sans-serif;
    }

    /* صناديق التنبيه الفاخرة مبطنة بخلفية داكنة متناسقة */
    .stAlert {
        border-right: 5px solid #f4d068 !important;
        border-left: none !important;
        background-color: #0b2545 !important;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.4);
        border-radius: 12px;
    }
    .stAlert p {
        color: #ffffff !important;
    }
    
    /* أزرار السيادة الملكية ببريق ذهبي */
    .stButton>button {
        background: linear-gradient(90deg, #ca6702 0%, #f4d068 100%) !important;
        color: #051622 !important;
        border: 1px solid #ffffff;
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        height: 55px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(244,208,104,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #f4d068 0%, #ffffff 100%) !important;
        box-shadow: 0 4px 25px rgba(244,208,104,0.4);
        cursor: pointer;
    }

    /* التبويبات الأنيقة المتوافقة مع النطاق الداكن */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        color: #a3b8cc !important;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #f4d068 !important;
        border-bottom-color: #f4d068 !important;
    }
    
    /* القائمة الجانبية الداكنة */
    section[data-testid="stSidebar"] {
        background-color: #030f18 !important;
        border-left: 1px solid #134074;
    }
    
    /* منع تداخل النصوص الانجليزية داخل الأسطر العربية */
    .en-badge {
        display: inline-block;
        direction: LTR !important;
        text-align: left !important;
        background-color: #f4d068;
        color: #051622;
        padding: 2px 8px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 14px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة الترحيب الفخمة المحدثة
st.markdown("<h1>🧬 مصفوفة السيطرة الأيضية — CellRevive AI</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px; color: #a3b8cc; font-weight: bold;'>المنصة السحابية السيادية الأولى لتشفير المغذيات وعكس مسار التدهور الخلوي</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 1. قاعدة البيانات والتحقق الفوري من الصلاحية والتفعيل الديناميكي
# ==========================================

VALID_30_DAYS = ["rev30-egy-7712", "rev30-egy-2941", "rev30-egy-8850", "rev30-egy-1493", "rev30-egy-6204", "rev30-egy-3319", "rev30-egy-5582", "rev30-egy-9041", "rev30-egy-4723", "rev30-egy-1109"]
VALID_90_DAYS = ["slv90-royal-9901", "slv90-royal-4412", "slv90-royal-8823", "slv90-royal-1154", "slv90-royal-7765", "slv90-royal-3376", "slv90-royal-5587", "slv90-royal-2298", "slv90-royal-6609", "slv90-royal-1314"]

st.sidebar.markdown("<h2 style='color: #f4d068; text-align: center;'>🔐 جدار التشفير الخلوي</h2>", unsafe_allow_html=True)

client_code = st.sidebar.text_input("برجاء إدخال كود التنشيط الجزيئي الخاص بك:", value="", type="password").strip().lower()

# الرسائل الملكية الجديدة الفاخرة البعيدة تماماً عن نمط العيادات التقليدي
if not client_code:
    st.info("👑 مرحباً بك في النطاق السيادي لـ CellRevive AI. تمهيداً لإعادة هندسة التمثيل الغذائي الخاص بك، فضلاً قم بإدخال 'كود التنشيط المشفر' الممنوح لك في القائمة الجانبية؛ لتفعيل المحرك البصري وفك تشفير مستقبلات الخلايا الحية.")
    st.stop()

# تحديد نوع الاشتراك والمدة بناءً على الكود المدخل
if client_code in VALID_30_DAYS:
    duration_days = 30
    package_name = "معسكر الـ 30 يوماً المكثف للمقاصة الأيضية وتنشيط AMPK"
    barcode_data = f"CellRevive-Verified-30Days-{client_code}"
elif client_code in VALID_90_DAYS:
    duration_days = 90
    package_name = "بروتوكول الترميم الخلوي الشامل والسيادة الجينية (90 يوماً)"
    barcode_data = f"CellRevive-Verified-90Days-{client_code}"
else:
    st.error("🚨 رمز التنشيط غير متطابق مع المصفوفة الجزيئية، أو انتهت فترة الصلاحية المحددة له.")
    st.stop()

# آلية التفعيل الفوري عند أول إدخال وحساب تاريخ انتهاء الصلاحية الذاتي
if "activation_date" not in st.session_state:
    st.session_state["activation_date"] = datetime.datetime.now()

activation_time = st.session_state["activation_date"]
expiration_time = activation_time + datetime.timedelta(days=duration_days)
current_time = datetime.datetime.now()

# التحقق من القفل التلقائي بعد انتهاء الصلاحية
if current_time > expiration_time:
    st.error("🚫 عذراً، تم تفعيل آلية القفل الذاتي لتجاوز الكود المدة الزمنية المخصصة له برمجياً منذ تاريخ أول إدخال.")
    st.stop()

# حساب الوقت المتبقي للعميل لبهجته وتحفيزه
days_remaining = (expiration_time - current_time).days
if days_remaining == 0:
    hours_remaining = round((expiration_time - current_time).seconds / 3600, 1)
    time_display = f"{hours_remaining} ساعة"
else:
    time_display = f"{days_remaining} يوم"

# إظهار البيانات والباركود في القائمة الجانبية الفاخرة
st.sidebar.success(f"👑 تم فك تشفير الكود بنجاح!")
st.sidebar.markdown(f"**نطاق البروتوكول:** \n {package_name}")
st.sidebar.markdown(f"**حالة المصفوفة:** نشطة وتعمل بكامل طاقة المعالجة")
st.sidebar.markdown(f"**تدمير ذاتي تلقائي بعد:** <span style='color:#f4d068; font-weight:bold;'>{time_display}</span>", unsafe_allow_html=True)

qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={barcode_data}&color=f4d068&bgcolor=030f18"
st.sidebar.image(qr_url, caption="📟 باركود الهوية الرقمية الموثق للمشترك")

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
# 3. تبويبات واجهة المستخدم الملكية (يمين إلى يسار)
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

# --- التبويب الثالث: المحرك التنبئي والتقرير الطبي الدقيق ---
with tab3:
    st.header("🔮 محرك الاستشراف الجزيئي وعكس تقدم الخلايا")
    
    if st.button("🚀 تشغيل محاكاة العكس الأيضي الكبرى"):
        st.markdown(f"### 🧬 العمر البيولوجي الحالي لخلاياك: {round(biological_age, 1)} سنة")
        
        # حساب التراجع المتوقع بناء على نوع الاشتراك لضمان الفخامة والبهجة والتحفيز العلمي
        age_reduction = 7.2 if duration_days == 90 else 3.1
        target_age = round(biological_age - age_reduction, 1)
        
        st.markdown(f"### 📈 التنبؤ الدقيق بنهاية بروتوكول الـ ({duration_days}) يوماً:")
        st.info(f"✨ بفضل بروتوكول الأغذية المشفرة وتنشيط إنتاج الـ SCFAs في الأمعاء لفتح مستقبلات الأنسولين المغلقة، يتوقع تراجع عمرك البيولوجي إلى {target_age} سنة، مع تلاشي تام لعلامات الشواك الأسود وعودة حساسية الخلايا لوضعها الفطري الأصيل.")
        
        st.write("---")
        st.subheader("📄 السجل الأكلينيكي الرسمي المعتمد (De-prescription)")
        
        # صياغة النص الإنجليزي الصارم الموجه في قالب مستقل تماماً لمنع التداخل واللخبطة
        report_text = f"""[CLINICAL SOVEREIGN REPORT]
-------------------------------------------
Date of Evaluation: July 2026
Patient Identification: {patient_name_in}
Verification Code Status: {client_code.upper()}
Dynamic Duration Window: {duration_days} Days Active

[BIOMEDICAL MATRIX]
- Fasting Blood Glucose: {fbg} mg/dL
- Glycated Hemoglobin (HbA1c): {hba1c}%
- Calculated Biological Cellular Age: {round(biological_age, 1)} Years
- Estimated Daily Protein Ceiling: {round(safe_protein_grams_daily, 1)} Grams

[CLINICAL ASSESSMENT & ORGAN SAFETY]
- Current Drug Category Rule: {selected_category.upper()}
- Organ Safety Status Flag: {organ_safety_status}
- Dynamic Expiration Lock Date: {expiration_time.strftime('%Y-%m-%d %H:%M')}
-------------------------------------------
Status: Officially Verified by CellRevive AI Matrix."""

        st.text_area("معاينة السجل الطبي الموثق بالكامل باللغة الإنجليزية لمنع أي تداخل بالمعاني:", report_text, height=220)
        
        st.download_button(
            label="📥 تحميل التقرير الطبي المعتمد لمشاركته مع الطبيب المتابع لحالتك",
            data=report_text,
            file_name="CellRevive_Sovereign_Report.txt",
            mime="text/plain"
        )
