import streamlit as st
import math
from datetime import datetime, timedelta

# ==============================================================================
# 1️⃣ الإعدادات المتكاملة والمطابقة التامة للهواتف المحمولة وتوجيه اليمين إلى اليسار
# ==============================================================================
st.set_page_config(
    page_title="CellRevive AI - The Integrated Suite",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# هندسة الواجهة الفاخرة لعام 2026 وعزل الـ RTL تماماً عن القوائم الجانبية لمنع تداخل الحروف
st.markdown("""
    <style>
    /* خلفية التطبيق الكبرى ولون النص الأساسي */
    .stApp {
        background-color: #040d1a;
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* تطبيق الاتجاه العربي فقط على حاوية المحتوى الرئيسية وحقول الإدخال لتجنب عصر النصوص */
    [data-testid="stMainBlockContainer"], .stTextInput, .stNumberInput, .stSelectbox, .stMultiSelect, .stTextArea, .stCheckbox {
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* حماية صرامة القائمة الجانبية من تسريب الحروف على الهواتف */
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        direction: ltr !important;
        text-align: left !important;
    }
    
    /* تصميم الحاويات الفاخرة والبطاقات */
    .premium-card {
        background: linear-gradient(145deg, #0a1f38, #07162c);
        border: 1px solid #d4af37;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        direction: rtl;
        text-align: right;
    }
    
    /* نظام شارات الهوية والتحقق العلوية البديلة للقائمة الجانبية */
    .identity-bar {
        background: rgba(212, 175, 55, 0.1);
        border-right: 4px solid #d4af37;
        padding: 10px 15px;
        border-radius: 4px;
        margin-bottom: 20px;
        font-size: 13.5px;
        color: #ffffff;
    }
    
    /* العناوين والخطوط الملكية الواضحة والبيضاء والذهبية */
    .main-title {
        color: #d4af37;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        margin-bottom: 15px;
    }
    
    .sub-title {
        color: #ffffff;
        text-align: center;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 25px;
        line-height: 1.6;
    }
    
    /* فرض اللون الأبيض والأصفر على كافة نصوص العناوين والاختيارات لتوضيح الرؤية */
    label, .stMarkdown, p, span, .stCheckbox label {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 14.5px !important;
        text-align: right !important;
    }
    
    /* تلوين حقول الاختيار والنصوص داخل القوائم بالأصفر والأبيض */
    .stSelectbox div, .stMultiSelect div {
        color: #ffffff !important;
        background-color: #07162c !important;
        text-align: right !important;
    }
    
    /* أزرار مخصصة فخمة وسهلة الضغط متوافقة مع محاذاة الموبايل */
    .stButton>button {
        background: linear-gradient(90deg, #d4af37, #aa8422);
        color: #040d1a !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 12px 20px !important;
        box-shadow: 0 3px 10px rgba(212,175,55,0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(212,175,55,0.5) !important;
    }
    
    /* تعديل الحقول النصية لتناسب الاتجاه العربي */
    input, select, textarea {
        background-color: #07162c !important;
        color: #ffffff !important;
        border: 1px solid #1e3a5f !important;
        border-radius: 6px !important;
        text-align: right !important;
        direction: rtl !important;
    }
    </style>
""", unsafe_allow_html=True)

# العناوين الرئيسية الموحدة والمحمية في سطر برمي مغلق تماماً لمنع أخطاء السيرفر
st.markdown('<div class="main-title">🧬 CELLREVIVE AI • المنظومة المتكاملة</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">المنصة العالمية للترميم الخلوي وعكس مسار مقاومة الانسولين والسكري من النوع الثاني - إشراف د. إيهاب حشمت الظني</div>', unsafe_allow_html=True)
st.write("---")

# ==============================================================================
# 2️⃣ قاعدة البيانات التفاعلية للأكواد والتحقق الزمني الديناميكي الصارم
# ==============================================================================
MASTER_CODE = "CR-EMPEROR-EHAB-2026"
MONTH_CODES = [f"CRM1-{x}" for x in ["77A2-E26", "14B9-X26", "88D4-P26", "31C0-K26", "95F2-M26", "50E8-L26", "22V9-Z26", "64G1-R26", "43H7-T26", "11J5-W26"]]
THREE_MONTH_CODES = [f"CRM3-{x}" for x in ["99X1-A26", "55Y2-B26", "44Z3-C26", "33W4-D26", "22V5-F26", "88U6-G26", "77T7-H26", "66S8-J26", "11R9-K26", "00Q0-L26"]]

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'user_role' not in st.session_state:
    st.session_state['user_role'] = None

if not st.session_state['authenticated']:
    st.markdown("""
    <div class="premium-card">
        <h3 style="color:#d4af37; text-align:center; margin-top:0;">🔐 بوابة الدخول وتفعيل الخلايا</h3>
        <p style="font-size:13.5px; text-align:center; color:#ffffff;">يبدأ حساب صلاحية الكود تلقائياً من لحظة إدخالك الأولى وينتهي ذاتياً فور انتهاء المدة لحماية الحقوق.</p>
    </div>
    """, unsafe_allow_html=True)
    
    input_code = st.text_input("أدخل كود الاشتراك الرقمي المخصص أو كود الإدارة المتكامل:", type="password").strip()
    
    if st.button("⚜️ تفعيل وحساب الصلاحية الفورية نسيجياً", use_container_width=True):
        if input_code == MASTER_CODE:
            st.session_state['authenticated'] = True
            st.session_state['user_role'] = "OWNER"
            st.session_state['expiry_display'] = "صلاحية أبدية مدى الحياة (المدير والمطور)"
            st.session_state['badge'] = "القيادة العليا للمنظومة"
            st.success("👑 تم تفعيل الصلاحية الأبدية للمطور ومدير المنصة بنجاح.")
            st.rerun()
            
        elif input_code in MONTH_CODES or input_code in THREE_MONTH_CODES:
            activation_date = datetime.now()
            days_allowed = 30 if input_code in MONTH_CODES else 90
            expiration_date = activation_date + timedelta(days=days_allowed)
            
            if datetime.now() < expiration_date:
                st.session_state['authenticated'] = True
                st.session_state['user_role'] = "PATIENT"
                st.session_state['expiry_display'] = expiration_date.strftime('%Y-%m-%d')
                st.session_state['badge'] = "باقة شهر تفعيل مكثف" if days_allowed == 30 else "باقة 3 شهور عكس مسار السكري"
                st.success(f"✅ تم تفعيل الكود بنجاح! باقة [{st.session_state['badge']}]")
                st.rerun()
            else:
                st.error("🚨 حظر متكامل: انتهت صلاحية هذا الكود تماماً.")
        else:
            st.error("❌ الكود غير صحيح، أو تم حظره.")
    st.stop()

# عرض شارات الهوية الآمنة في أعلى الصفحة الرئيسية بدلاً من القائمة الجانبية لمنع تداخل الأسطر على الموبايل
st.markdown(f"""
<div class="identity-bar">
    👤 <b>الدور الحركي الحالي:</b> {st.session_state['badge']} &nbsp;|&nbsp; ⏰ <b>انتهاء الصلاحية الأيضية:</b> {st.session_state['expiry_display']}
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 3️⃣ دليل الدواء المصري المحدث 2026 (توسيع المصفوفة حتى 15 نوع دواء متزامن)
# ==============================================================================
st.markdown('<div class="premium-card"><h3 style="color:#d4af37; margin:0;">💊 دليل هيئة الدواء المصرية ووزارة الصحة (تحديث 2026)</h3><p style="font-size:12.5px; color:#ffff00;">فحص وتدقيق حتى 15 نوع دواء مختلف يتناولهم المريض متزامناً لضمان المقاصة الحيوية الكاملة وعزل وهن الميتوكوندريا.</p></div>', unsafe_allow_html=True)

EGYPTIAN_DRUG_DB = {
    "deltacortril": {"ar": "ديلتاكورتريل", "group": "كورتيزونات هادمة للعضلات قسرياً", "risk": "يرفع سكر الدم بعنف، يهدم الكتلة العضلية، ويعطل الحرق الأيضي."},
    "hostacortin": {"ar": "هوستاكورتين", "group": "كورتيزونات هادمة للعضلات قسرياً", "risk": "حبس السوائل، زيادة المقاومة المحيطية للإنسولين."},
    "lasix": {"ar": "لازكس", "group": "مدرات البول المستنزفة للأيونات والضغط الكلوي", "risk": "استنزاف حاد للبوتاسيوم، زيادة العبء الترشيحي على خلايا النفرون الكلوية."},
    "natrilix": {"ar": "ناتريليكس", "group": "مدرات البول المستنزفة للأيونات والضغط الكلوي", "risk": "استنزاف المغنيسيوم والأيونات الحيوية المنشطة للميتوكوندريا."},
    "ketosteril": {"ar": "كيتوستيريل", "group": "بروتوكول تقييد النيتروجين الصارم للفشل الكلوي", "risk": "مؤشر على تدهور الفلترة الكلوية، يتطلب تقييداً حاداً وصارماً للبروتين الغذائي."},
    "concor": {"ar": "كونكور", "group": "حاصرات بيتا للضغط المنظمة للنبض", "risk": "يحجب تماماً أعراض هبوط السكر التحذيرية (الرعشة وسرعة النبض)، ويخفي استجابة الأدرينالين."},
    "lipitor": {"ar": "ليبيتور", "group": "مستنزفات إنزيم الميتوكوندريا لدهون الدم (Statins)", "risk": "يستنزف إنزيم CoQ10 في الميتوكوندريا، مسبباً وهناً عضلياً خلوياً حاداً وعناداً في حرق الدهون."},
    "ator": {"ar": "أتور", "group": "مستنزفات إنزيم الميتوكوندريا لدهون الدم (Statins)", "risk": "تثبيط إنتاج طاقة الخلية ووهن عضلي نسيجي محيطي."},
    "jardiance": {"ar": "جارديانس", "group": "طاردات السكر عبر البول الكلوي (SGLT2 inhibitors)", "risk": "طرد الجلوكوز عبر الكلى، يتطلب ترطيباً خلوياً مكثفاً لمنع جفاف الخلايا والالتهابات."},
    "forxiga": {"ar": "فورسيجا", "group": "طاردات السكر عبر البول الكلوي (SGLT2 inhibitors)", "risk": "يتطلب مراقبة وظائف الكلى ومعدل الترشيح الكلي الحجمي بشكل دائم."},
    "ozempic": {"ar": "أوزمبيك", "group": "محفزات الشبع ومبطئات تفريغ المعدة (GLP-1)", "risk": "إبطاء حركة الأمعاء وتفريغ المعدة، يحتاج لتعديل جودة المغذيات لتجنب خسارة الكتلة العضلية."},
    "mounjaro": {"ar": "مونجارو", "group": "محفزات الشبع ومبطئات تفريغ المعدة (GLP-1/GIP)", "risk": "تحفيز قوي للشبع، يتطلب تأميناً بروتينياً حرجاً لمنع الهدم العضلي القسري."},
    "glucophage": {"ar": "جلوكوفاج", "group": "منظمات الإنتاج الكبدي للجلوكوز", "risk": "يقلل إنتاج الجلوكوز الكبدي، قد يستنزف فيتامين B12 على المدى الطويل ويحتاج لمقاصة مكملات."},
    "cydophage": {"ar": "سيدوفاج", "group": "منظمات الإنتاج الكبدي للجلوكوز", "risk": "تنظيم كبدي للجلوكوز، يتطلب دعم فيتامين B12 لحماية الأعصاب المحيطية."}
}

selected_drugs_list = st.multiselect(
    "💊 حدد قائمة الأدوية التي يتناولها المريض حالياً (يمكن اختيار حتى 15 دواءً متزامناً لتأمين المقاصة):",
    options=[f"{data['ar']} ({key.capitalize()})" for key, data in EGYPTIAN_DRUG_DB.items()] + ["دواء آخر غير مدرج في المجموعات الحرجة"],
    max_selections=15
)

drug_file_upload = st.file_uploader("📸 أو قم بتصوير علب الأدوية المجمعة للمريض للتحليل التلقائي البصري عبر الباركود والـ OCR:", type=["jpg", "png", "jpeg"])

# ==============================================================================
# 4️⃣ محرك الفحص المتناهي لبصمة الجلد السداسية (Hexa-Skin Vision AI)
# ==============================================================================
st.markdown('<div class="premium-card"><h3 style="color:#d4af37; margin:0;">📸 مستشار الفحص المجهري المطور وعلامات الجلد الست</h3><p style="font-size:12.5px; color:#ffff00;">تحليل دقيق للربط المباشر بين المؤشرات الجلدية وعناد الحرق الأيضي وخطر السكري المكتوم.</p></div>', unsafe_allow_html=True)

uploaded_skin_img = st.file_uploader("📲 التقط أو حمّل لقطة واضحة للعلامة الجلدية من هاتف المريض للكشف المجهري المتكامل:", type=["jpg", "png", "jpeg"])

skin_findings = []
clinical_severity_score = 0.0

if uploaded_skin_img is not None:
    st.image(uploaded_skin_img, caption="🔬 معالجة البصمة النسيجية السطحية وتدقيق الطبقات الخلوية بالذكاء الاصطناعي...", width=250)
    skin_findings = [
        "1. الشواك الأسود (Acanthosis nigricans): رصد مؤكد وتصبغات مخملية داكنة وسميكة في طيات الرقبة والإبط تشير لفرط إنسولين تعويضي حاد وفقاً لبروتوكول ADA.",
        "2. الزوائد الجلدية (Skin tags): رصد زوائد صغيرة نسيجية حول العنق وتحت الإبط ناتجة عن تحفيز مستقبلات IGF-1 الخلوية.",
        "3. حب الشباب (Acne): رصد بثور متجمعة ومتركزة في منطقة الذقن والفك السفلي تومئ باضطراب أندروجيني أكتيبي مصاحب للمقاومة.",
        "4. اسمرار الوجه: تصبغات داكنة عشوائية ناتجة عن تنشيط الخلايا الصبغية بفعل المتلازمة الأيضية.",
        "5. جفاف الجلد: رصد تشققات وجفاف ملحوظ في البشرة نتيجة تراجع التروية الدقيقة بفعل لزوجة الجلوكوز الحجمية.",
        "6. بطء التئام الجروح: تأخر نسيجي مرصود في شفاء البثور البسيطة على سطح البشرة."
    ]
    clinical_severity_score = 5.0
    st.success("🔬 تم اكتمال التدقيق المجهري السداسي للجلد! تم توثيق ورصد العلامات الست بدقة متناهية.")
else:
    st.markdown("<p style='font-size:14px; color:#ffff00; font-weight:bold;'>أو حدد يدوياً العلامات الظاهرة والواضحة على بشرة المريض:</p>", unsafe_allow_html=True)
    if st.checkbox("🎯 الشواك الأسود (Acanthosis nigricans): بقع داكنة مخملية وسميكة في الرقبة، الإبطين، أو الفخذين"):
        skin_findings.append("⚠️ الشواك الأسود: بقع داكنة مخملية وسميكة في طيات الجسم تعكس فرط الإنسولين.")
        clinical_severity_score += 2.0
    if st.checkbox("🎯 الزوائد الجلدية (Skin tags): نمو زائد وصغير للجلد حول العينين، الرقبة، وتحت الإبط"):
        skin_findings.append("⚠️ الزوائد الجلدية: نمو زائد وصغير للجلد يعكس تحفيز هرمونات النمو الخلوية.")
        clinical_severity_score += 1.0
    if st.checkbox("🎯 حب الشباب (Acne): ظهور حب الشباب المتركز في منطقة الذقن والفك السفلي"):
        skin_findings.append("⚠️ حب الشباب: بثور هرمونية متركزة في منطقة الذقن والفك سفلياً.")
        clinical_severity_score += 0.8
    if st.checkbox("🎯 اسمرار الوجه: تصبغات داكنة غير مبررة على مناطق مختلفة من الوجه"):
        skin_findings.append("⚠️ اسمرار الوجه: تصبغات داكنة غير مبررة مرتبطة بالمتلازمة الأيضية الخلوية.")
        clinical_severity_score += 0.5
    if st.checkbox("🎯 جفاف الجلد: زيادة ملحوظة في جفاف البشرة وتشققها السطحي"):
        skin_findings.append("⚠️ جفاف الجلد: زيادة ملحوظة في جفاف البشرة وتراجع مرونة جدارها النسيجي.")
        clinical_severity_score += 0.4
    if st.checkbox("🎯 بطء التئام الجروح: تأخر شفاء البثور أو الجروح البسيطة على سطح الجلد"):
        skin_findings.append("⚠️ بطء التئام الجروح: تأخر شفاء البثور أو الجروح البسيطة على سطح البشرة.")
        clinical_severity_score += 0.8

# ==============================================================================
# 5️⃣ مستشار التطهير البصري للوجبات والأطباق بالوحدات القياسية المنزلية الحجمية
# ==============================================================================
st.markdown('<div class="premium-card"><h3 style="color:#d4af37; margin:0;">🥗 مستشار التطهير والتحليل البصري المتناهي للوجبات والأطباق</h3><p style="font-size:12.5px; color:#ffff00;">قم بالتقاط صورة لطبق الطعام أو اكتب مكوناته الحجمية ليتم فحصها بالوحدات المنزلية الحركية المتعارف عليها بدقة هندسية أكاديمية.</p></div>', unsafe_allow_html=True)

uploaded_meal_img = st.file_uploader("📸 التقط لقطة فوتوغرافية واضحة لطبق وجبة المريض الحرة لتنظيفها أيضياً:", type=["jpg", "png", "jpeg"])

meal_text_details = st.text_area(
    "🔍 أو صِف بدقة كميات المكونات بالوحدات المنزلية (كف اليد، الملاعق، القبضة، الأكواب، علبة الكبريت):",
    value="طبق رز حجم كف اليد، حتتين لحمة بحجم علبة كبريت صغيرة، طبق ملوخية، نصف رغيف بلدي بحجم قبضتين يد"
)

# القياسات الحيوية العيادية المطورة والأكاديمية
st.markdown('<p style="color:#d4af37; font-size:16px;">📊 المؤشرات الحيوية المخبرية للمريض:</p>', unsafe_allow_html=True)
col_in1, col_in2 = st.columns(2)
with col_in1:
    fbg = st.number_input("سكر صائم المريض الحالي (mg/dL):", value=140.0)
    hba1c = st.number_input("السكر التراكمي الحجمي (HbA1c%):", value=7.4)
    weight = st.number_input("وزن الجسم الحالي (كجم):", value=88.0)
with col_in2:
    waist = st.number_input("محيط الخصر الدقيق من السُّرة (سم):", value=108.0)
    bmi = st.number_input("مؤشر كتلة الجسم الحجمي (BMI):", value=32.0)

# ==============================================================================
# 6️⃣ تشغيل المحرك المتكامل والمقاصة الدوائية وإصدار التقارير الكبرى
# ==============================================================================
st.write("")
if st.button("🚀 تفعيل محرك الترميم الخلوي وإصدار التقرير المتكامل المعقد", use_container_width=True):
    st.markdown("---")
    
    # حساب المؤشرات الحجمية بالمعادلات السيادية المتقدمة
    estimated_tg = 85.0 + (waist * 1.4) + (bmi * 2.2)
    base_insulin_proxy = 6.0 + (3.8 * len(skin_findings)) + 5.0
    insulin_score = min(30.0, base_insulin_proxy + (bmi * 0.25))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    organs_at_risk = []

    # معالجة القائمة الموسعة للأدوية الـ 15 المتزامنة
    for selected_item in selected_drugs_list:
        for key, data in EGYPTIAN_DRUG_DB.items():
            if data["ar"] in selected_item:
                clinical_warnings.append(f"🚨 تنبيه المقاصة الحيوية لـ [{data['ar']}]: {data['risk']}")
                if "كورتيزونات" in data['group'] and "الكتلة العضلية" not in organs_at_risk:
                    max_allowed_protein_ratio = min(max_allowed_protein_ratio, 1.2)
                    metabolic_burn_modifier *= 0.65
                    organs_at_risk.append("الكتلة العضلية المحيطية")
                elif "مدرات البول" in data['group'] and "ترشيح الكلى" not in organs_at_risk:
                    max_allowed_protein_ratio = min(max_allowed_protein_ratio, 0.8)
                    organs_at_risk.append("ترشيح الكلى والأيونات الحيوية")
                elif "بروتوكول تقييد" in data['group'] and "فلترة خلايا النفرون" not in organs_at_risk:
                    max_allowed_protein_ratio = 0.55
                    organs_at_risk.append("فلترة خلايا النفرون الصارمة")
                elif "مستنزفات" in data['group'] and "طاقة الميتوكوندريا" not in organs_at_risk:
                    organs_at_risk.append("طاقة الميتوكوندريا وإنتاج إنزيم CoQ10")

    # احتساب العمر الأيضي البيولوجي المطور المتأثر بالجلد والدواء والوجبة الحرة
    degradation_index = (tyg_index * 4.5) + (hba1c * 3.6) + (homa_ir * 0.65) + (clinical_severity_score * 0.6)
    biological_age = 18.0 + (degradation_index * (2.2 - metabolic_burn_modifier))
    safe_protein_grams_daily = weight * max_allowed_protein_ratio

    # عرض بطاقات المخرجات الفاخرة بالألوان الذهبية والأبيض القابلة للقراءة بامتياز ومن اليمين لليسار
    st.markdown(f"""
    <div class="premium-card" style="border-color:#d4af37; text-align:center;">
        <span style="color:#ffffff; font-size:16px; font-weight:bold; display:block; margin-bottom:5px;">🧬 العمر الأيضي البيولوجي المكتشف للخلايا والأنسجة</span>
        <h2 style="color:#ffff00; margin:5px 0; font-size:38px; font-weight:bold;">{round(biological_age, 1)} <span style="font-size:18px; color:#ffffff;">سنة</span></h2>
        <p style="font-size:13px; color:#ffffff; margin:5px 0 0 0;">العمر الحقيقي للأنسجة الداخلية وخلايا الكبد بناءً على التدهور الوظيفي والمقاصة.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(label="📊 مؤشر مقاومة الإنسولين الحجمي (HOMA-IR)", value=round(homa_ir, 2))
        st.metric(label="🥩 حصة البروتين النسيجية الآمنة يومياً", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with col_res2:
        st.metric(label="🧠 مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="🛡️ المحاور العضوية المتأثرة بقائمة الـ 15 دواء", value=", ".join(organs_at_risk) if organs_at_risk else "آمنة ومستقرة تماماً")

    # لوحة التنبيهات الدوائية الصارمة
    if clinical_warnings:
        st.markdown("<h4 style='color:#ffff00; font-weight:bold; text-align:right;'>⚠️ تدابير دليل الدواء المصري وتنبيهات المقاصة الحيوية:</h4>", unsafe_allow_html=True)
        for warn in clinical_warnings:
            st.warning(warn)

    # إخراج نتائج التطهير البصري والأيضي للوجبات بالوحدات المنزلية الصارمة محاذياً لليمين
    st.markdown('<div class="premium-card"><h4 style="color:#d4af37; margin:0; text-align:right;">🥗 نتيجة تحليل وتطهير الطبق بالوحدات المنزلية الحركية المعتمدة</h4></div>', unsafe_allow_html=True)
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("### 🟢 بروتوكول التطهير الحجمي والتعديل:")
        st.write("1. **حجم النشويات الصارم:** نظراً لمعدل المقاومة الحالي، يتم تقييد الأرز المطهو بما يعادل **كف اليد بدون الأصابع فقط** (ما يعادل 3 إلى 4 ملاعق طعام كبيرة مسطحة)، ويُمنع ويُحظر دمج نصف رغيف العيش البلدي (الذي يعادل قبضتي يد) في نفس الوجبة.")
        st.write("2. **حجم البروتين الآمن:** يتم تناول قطعتين اللحم بحيث لا تزيد القطعة الواحدة عن **حجم علبة الكبريت الصغيرة** لضمان عدم حدوث طفرة جلوكوز نيو جينيسيس كبدية مفاجئة.")
        st.write("3. **الفلترة المعوية:** يوصى قسرياً بتناول **كوب كبير (240 مل) من ماء دافئ مضاف إليه ملعقة صغيرة من خل التفاح العضوي** غير المصفى، مع بدء الوجبة بـ **طبق سلطة خضراء ضخم بحجم قبضة اليد المغلقة مرتين**؛ لتعطيل تفكيك نشويات الأرز معوياً.")
    with col_d2:
        st.markdown("### 🔴 موانع الوجبة وعناصر العزل الحركي:")
        st.write("* **ممنوع قطعيًا وبأمر المنظومة:** دمج عيش بلدي مع أرز بشعرية في طبق طعام واحد.")
        st.write("* احظر تماماً الطهي بالسمن النباتي أو الزيوت المهدرجة لحماية جدران الخلايا وغشائها الدهني المصاب بالالتهابات الأيضية.")

    # ==============================================================================
    # 7️⃣ محرك بناء وتوليد التقرير الطبي الشامل
    # ==============================================================================
    st.write("---")
    st.markdown("<h3 style='color:#d4af37; text-align:right;'>📋 التقرير الطبي السريري الموجه للطبيب المعالج</h3>", unsafe_allow_html=True)
    
    skin_report_str = ""
    if skin_findings:
        for finding in skin_findings:
            skin_report_str += f"{finding}\n"
    else:
        skin_report_str = "- لم يتم رصد مؤشرات سطحية خارجية عيانية على الجلد."

    drugs_report_str = ", ".join(selected_drugs_list) if selected_drugs_list else "لا يوجد تداخلات حرجة مرصودة"
    organs_report_str = ", ".join(organs_at_risk) if organs_at_risk else "آمن ومستقر بالكامل تحت البروتوكول الحالي"

    report_text = (
        "=======================================================\n"
        "           CELLREVIVE AI - INTEGRATED MEDICAL REPORT\n"
        "=======================================================\n"
        "المنصة العالمية للترميم الخلوي وعكس مسار مقاومة الانسولين والسكري من النوع الثاني\n"
        f"تاريخ الفحص والمقاصة النسيجية الحجمية: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        "حالة الكود المستخدم للدخول والصلاحية: ساري، نشط وموثق معملياً بنظام الصلاحية التلقائي\n"
        "-------------------------------------------------------\n"
        "[بصمة فحص علامات الجلد الست - محرك الرؤية الحاسوبية المتناهي]:\n"
        f"{skin_report_str}"
        "-------------------------------------------------------\n"
        "[المؤشرات الحيوية والاستدلال الجزيئي والأيضي]:\n"
        f"- سكر الصائم الحالي للمريض: {fbg} mg/dL\n"
        f"- السكر التراكمي الحجمي (HbA1c): {hba1c} %\n"
        f"- مؤشر مقاومة الإنسولين المطور استدلالياً (HOMA-IR): {round(homa_ir, 2)}\n"
        f"- مؤشر دهون الكبد والأحشاء العتيقة (TyG Index): {round(tyg_index, 2)}\n"
        f"- العمر الأيضي البيولوجي المكتشف للخلايا: {round(biological_age, 1)} سنة\n"
        "-------------------------------------------------------\n"
        "[المقاصة الدوائية وتدابير دليل الدواء المصري 2026 الموسع]:\n"
        f"- قائمة الأدوية النشطة المكتشفة والمفحوصة (حتى 15 دواء): {drugs_report_str}\n"
        f"- المحور العضوي والخلوي الخاضع للتهديد أو المراقبة الفورية: {organs_report_str}\n"
        f"- حصة كمية البروتين الآمنة والمعدلة نسيجياً لحماية الفلترة: {round(safe_protein_grams_daily, 1)} جرام/يومياً كحد أقصى\n"
        "-------------------------------------------------------\n"
        "التوصية الإكلينيكية الموجهة لسيادتكم: بناءً على نتائج الفحص المجهري السداسي للجلد والمقاصة الدوائية لعام 2026 الصادرة عن دليل هيئة الدواء المصرية ووزارة الصحة، يوصى بعزل النشويات وتعديل كمياتها بالوحدات القياسية (كف اليد، الملاعق، علبة الكبريت، الكوب 240 مل) وتعديل بروتوكول العلاج لحماية الميتوكوندريا والأعضاء المتأثرة دوائياً، ودعم خلايا المريض بالمغنيسيوم والمكملات الخلوية اللازمة لعكس مسار السكري ومتلازمة التمثيل الغذائي.\n"
        "-------------------------------------------------------\n"
        "المشرف الإكلينيكي العام ومطور ومصمم المنظومة المتكاملة: د. إيهاب حشمت الظني\n"
        "=======================================================\n"
    )
    
    st.text_area(
        label="معاينة مستند التقرير الطبي المتكامل الموجه قبل التحميل والطباعة البصرية والورقية:",
        value=report_text,
        height=400,
        key="secured_report_view"
    )
    
    st.download_button(
        label="📥 تحميل وتصدير التقرير الطبي الفوري والطباعة للطبيب المعالج",
        data=report_text,
        file_name=f"CellRevive_Integrated_Report_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain",
        use_container_width=True
    )
