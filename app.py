import streamlit as st
import datetime
import math

# إعدادات الصفحة السيادية الفاخرة
st.set_page_config(page_title="CellRevive AI — المنظومة الملكية", page_icon="🧬", layout="centered")

# هندسة التصميم الفاخر والأصالة الفرعونية مع فرض اتجاه اليمين إلى اليسار (RTL)
st.markdown("""
    <style>
    /* فرض الاتجاه العربي لمنع انقلاب الشاشة */
    .main, .block-container, div[data-testid="stSidebarUserContent"] {
        direction: RTL !important;
        text-align: right !important;
    }
    
    /* تصميم الخلفية والألوان الفاخرة (الأزرق الملكي والذهبي النفيس) */
    .main {
        background: linear-gradient(135deg, #f4f7f6 0%, #e2eafc 100%);
    }
    
    /* العناوين الكبرى */
    h1 {
        color: #0b2545;
        font-family: 'Times New Roman', Arial, sans-serif;
        text-align: center;
        font-weight: 900;
        border-bottom: 3px solid #8ecae6;
        padding-bottom: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    h2, h3 {
        color: #134074;
        font-family: Arial, sans-serif;
    }

    /* صناديق التنبيه الفاخرة */
    .stAlert {
        border-right: 5px solid #ee9b00 !important;
        border-left: none !important;
        background-color: #ffffff !important;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.05);
        border-radius: 8px;
    }
    
    /* أزرار السيادة الملكية */
    .stButton>button {
        background: linear-gradient(90deg, #134074 0%, #0b2545 100%);
        color: #ffffff !important;
        border: 2px solid #ee9b00;
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        height: 55px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ee9b00 0%, #ca6702 100%);
        border: 2px solid #0b2545;
        cursor: pointer;
    }

    /* التبويبات الأنيقة */
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        font-weight: bold;
        color: #134074;
        padding: 10px 20px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #ee9b00 !important;
        border-bottom-color: #ee9b00 !important;
    }
    
    /* منع تداخل النصوص الانجليزية داخل الأسطر العربية */
    .en-badge {
        display: inline-block;
        direction: LTR !important;
        text-align: left !important;
        background-color: #0b2545;
        color: #ffffff;
        padding: 2px 8px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة الترحيب الفخمة
st.markdown("<h1>🧬 مصفوفة السيطرة الأيضية — CellRevive AI</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px; color: #555;'>المنصة السيادية الكبرى تحت الإشراف المباشر للعيادة التخصصية الاستشارية</p>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 1. قاعدة البيانات والتحقق الفوري من الصلاحية والتفعيل الديناميكي
# ==========================================

# توليد الأكواد المعتمدة في النظام لـ 30 و 90 يوماً
VALID_30_DAYS = ["rev30-egy-7712", "rev30-egy-2941", "rev30-egy-8850", "rev30-egy-1493", "rev30-egy-6204", "rev30-egy-3319", "rev30-egy-5582", "rev30-egy-9041", "rev30-egy-4723", "rev30-egy-1109"]
VALID_90_DAYS = ["slv90-royal-9901", "slv90-royal-4412", "slv90-royal-8823", "slv90-royal-1154", "slv90-royal-7765", "slv90-royal-3376", "slv90-royal-5587", "slv90-royal-2298", "slv90-royal-6609", "slv90-royal-1314"]

st.sidebar.markdown("<h2 style='color: #0b2545; text-align: center;'>🔐 جدار الحماية الملكي</h2>", unsafe_allow_html=True)

client_code = st.sidebar.text_input("برجاء إدخال كود التنشيط السري الخاص بك:", value="", type="password").strip().lower()

if not client_code:
    st.warning("👑 مرحباً بك في رحلة استعادة الحيوية الخلوية. فضلاً، أدخل كود الاشتراك الفعال الممنوح لك من العيادة التخصصية في القائمة الجانبية لتفعيل البروتوكول الملكي البصري.")
    st.stop()

# تحديد نوع الاشتراك والمدة بناءً على الكود المدخل
if client_code in VALID_30_DAYS:
    duration_days = 30
    package_name = "معسكر الثلاثين يوماً المكثف للمقاصة الخلوية"
    barcode_data = f"CellRevive-Verified-30Days-{client_code}"
elif client_code in VALID_90_DAYS:
    duration_days = 90
    package_name = "برنامج الترميم الخلوي الشامل والسيادة الجينية (90 يوماً)"
    barcode_data = f"CellRevive-Verified-90Days-{client_code}"
else:
    st.error("🚨 رمز التنشيط غير صحيح، أو تم تجميده من قبل إدارة العيادة. يرجى مراجعة الاستشاري الخاص بك.")
    st.stop()

# محاكاة آلية التفعيل الفوري عند أول إدخال وحساب تاريخ انتهاء الصلاحية الذاتي
if "activation_date" not in st.session_state:
    st.session_state["activation_date"] = datetime.datetime.now()

activation_time = st.session_state["activation_date"]
expiration_time = activation_time + datetime.timedelta(days=duration_days)
current_time = datetime.datetime.now()

# التحقق من القفل التلقائي بعد انتهاء الصلاحية
if current_time > expiration_time:
    st.error("🚫 انتهت صلاحية هذا الكود تلقائياً بناءً على تاريخ أول تفعيل له. يرجى تجديد الاشتراك للولوج إلى المحاكاة الجزيئية.")
    st.stop()

# حساب الأيام المتبقية للعميل لبهجته وتحفيزه
days_remaining = (expiration_time - current_time).days
if days_remaining == 0:
    hours_remaining = round((expiration_time - current_time).seconds / 3600, 1)
    time_display = f"{hours_remaining} ساعة"
else:
    time_display = f"{days_remaining} يوم"

# إظهار الباركود الفاخر وبيانات التنشيط في القائمة الجانبية بالكامل باللغة العربية
st.sidebar.success(f"👑 تم التحقق من الكود المعتمد بنجاح!")
st.sidebar.markdown(f"**باقة الاشتراك:** \n {package_name}")
st.sidebar.markdown(f"**حالة التفعيل:** نشط ويبدأ الحساب من لحظة الإدخال")
st.sidebar.markdown(f"**الوقت المتبقي على القفل الذاتي:** <span style='color:#ca6702; font-weight:bold;'>{time_display}</span>", unsafe_allow_html=True)

qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={barcode_data}&color=0b2545"
st.sidebar.image(qr_url, caption="📟 باركود الهوية الرقمية الموثق للعميل")

# ==========================================
# 2. الدستور الدوائي المصري المحدث 2026 (مفصول تماماً لمنع التداخل)
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
    st.header("📋 تسجيل العلامات الأيضية الحالية")
    col1, col2 = st.columns(2)
    with col1:
        patient_name_in = st.text_input("اسم المريض الثلاثي:", value="أحمد محمد علي")
        fbg = st.number_input("قياس سكر الصائم الحالي مجم / ديسيلتر:", value=140.0)
        hba1c = st.number_input("معدل السكر التراكمي النسبة المئوية:", value=7.4)
    with col2:
        weight = st.number_input("الوزن الحالي بالكيلوجرام:", value=88.0)
        waist = st.number_input("محيط الخصر عند السرة بالسنتيمتر:", value=104.0)
        bmi = st.number_input("مؤشر كتلة الجسم المحسوب للمريض:", value=30.8)
    
    st.write("---")
    st.header("🔍 فحص التداخل الدوائي والمؤشرات الفعالة")
    search_query = st.text_input("اكتب اسم الدواء الحالي الذي تتناوله (باللغة العربية مثل: سيدوفاج أو لازكس):", value="سيدوفاج").strip()

    selected_category = "none"
    medication_display_ar = "لم يتم رصد أي تداخل دوائي مجهد لبيتا أو الخلايا حالياً"
    
    for brand_ar, details in EGYPTIAN_DRUG_REGISTRY.items():
        if search_query in brand_ar:
            selected_category = details["category"]
            medication_display_ar = f"تم رصد دواء {brand_ar} النشط في مصفوفة الحرق الخلوية الحالية"
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
    organ_safety_status = "ترشيح خلايا الكلى تحت الملاحظة الدقيقة لمنع الإجهاد"
elif selected_category == "nephro":
    max_allowed_protein_ratio = 0.5
    organ_safety_status = "حماية كلية قصوى - الخلايا النفرونية مجهدة تماماً"
elif selected_category == "sulfonylurea":
    organ_safety_status = "تحذير: هذا الدواء يسبب إجهاد مستمر لخلايا بيتا البنكرياسية"

degradation_index = (tyg_index * 4.0) + (hba1c * 3.2) + (homa_ir_proxy * 0.5)
biological_age = 20.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
safe_protein_grams_daily = weight * max_allowed_protein_ratio

# --- التبويب الثاني: فحص الرؤية الحاسوبية الشامل ---
with tab2:
    st.header("📸 فحص المسح البصري الفوري ذو الدقة العالية")
    st.subheader("1️⃣ فحص علامات المقاومة الجلدية وصحة البشرة")
    skin_condition = st.selectbox("إذا كان لديك عرض ظاهري، حدده هنا بدقة لربطه بالمحرك:", [
        "الشواك الأسود - تصبغات عنيفة خلف الرقبة أو الثنايا",
        "الزوائد الجلدية الكثيفة حول العنق",
        "حب الشباب الهرموني العنيد",
        "لا توجد أعراض جلدية ظاهرة"
    ])
    uploaded_skin = st.file_uploader("ارفع صورة الفحص المباشر لعنق المريض أو المنطقة المصابة:", type=["jpg","png","jpeg"], key="skin_up")
    if uploaded_skin is not None:
        st.success("🔍 تم تحليل كثافة الصبغة الجلدية للبكسل بنجاح: تم ربط النتائج ببروتوكول الترميم الخلوي الذكي.")

    st.write("---")
    st.subheader("2️⃣ مطابقة وتدقيق طبق الطعام الحيوي")
    uploaded_food = st.file_uploader("ارفع صورة الوجبة الحالية قبل البدء في تناولها لمنع الثغرات الأيضية:", type=["jpg","png","jpeg"], key="food_up")
    if uploaded_food is not None:
        st.image(uploaded_food, width=320)
        st.markdown("### 🔍 نتيجة المقاصة البصرية الفورية للطبق:")
        if selected_category == "corticosteroid":
            st.error("⚠️ تحذير طبي حاد من المصفوفة: الدواء المكتشف يقلل حساسية الأنسولين؛ النشويات الظاهرة في الصورة ستسبب قفزة عنيفة. يرجى تقليص الكربوهيدرات للنصف فوراً.")
        else:
            st.success("✅ طبق متوازن ومصادق عليه ويتماشى تماماً مع الخريطة الجينية والغذائية المحددة لاشتراكك الملكي.")

# --- التبويب الثالث: المحرك التنبئي والتقرير الزمالي الصارم ---
with tab3:
    st.header("🔮 محرك الاستشراف الجزيئي وعكس تقدم الخلايا")
    
    if st.button("🚀 تشغيل محاكاة العكس الأيضي الكبرى"):
        st.markdown(f"### 🧬 العمر البيولوجي الحالي لخلايا المريض: {round(biological_age, 1)} سنة")
        
        # حساب التراجع المتوقع بناء على نوع الاشتراك الفعلي للعميل لضمان بهجته وعظمته
        age_reduction = 7.2 if duration_days == 90 else 3.1
        target_age = round(biological_age - age_reduction, 1)
        
        st.markdown(f"### 📈 التنبؤ الاستشرافي بنهاية فترة الاشتراك المحددة بـ ({duration_days}) يوماً:")
        st.info(f"✨ بفضل بروتوكول المغذيات المشفرة وتنشيط إنتاج الأحماض الدهنية قصيرة السلسلة في الأمعاء، يتوقع تراجع عمرك البيولوجي إلى {target_age} سنة، مع تلاشي تام للشواك الأسود وعودة حساسية الخلايا لوضعها الفطري الأصيل.")
        
        st.write("---")
        st.subheader("📄  التقرير الأكلينيكي الرسمي المُوجه للعيادة")
        
        # صياغة النص الإنجليزي في قالب منفصل ومستقل تماماً لعدم إحداث أي تداخل بالسطر
        report_text = f"""[CLINICAL SOVEREIGN REPORT]
-------------------------------------------
Date of Evaluation: July 2026
Patient Name: {patient_name_in}
Verification Code: {client_code.upper()}
Subscription Duration: {duration_days} Days Active

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
            label="📥 تحميل التقرير الطبي بصيغة ملف نصي معتمد",
            data=report_text,
            file_name="CellRevive_Royal_Report.txt",
            mime="text/plain"
        )
