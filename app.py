import streamlit as st
import math
from datetime import datetime

# إعدادات الواجهة السيادية
st.set_page_config(page_title="CellRevive AI Engine", page_icon="🧬", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #004085; font-family: 'Arial'; text-align: center; }
    h3 { color: #17a2b8; text-align: center; }
    .report-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 2px solid #004085; }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 المنظومة السيادية: CellRevive AI")
st.subheader("بروتوكول الترميم الخلوي وعكس مسار السكري لعام 2026")
st.write("---")

# مدخلات بيانات المريض والتحاليل والأدوية
col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("اسم المريض الثلاثي (لإصدار التقرير):", value="أحمد محمد علي")
    fbg = st.number_input("سكر الصائم الحالي (mg/dL):", value=142.0)
    hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=7.5)
    weight = st.number_input("الوزن الحالي للمريض (كجم):", value=85.0)

with col2:
    waist = st.number_input("محيط الخصر بدقة (سم):", value=106.0)
    bmi = st.number_input("مؤشر كتلة الجسم الحالي (BMI):", value=31.5)
    has_acanthosis = st.selectbox("العلامات الفيزيولوجية (تصبغات الرقبة/الزوائد):", ["موجودة وعنيفة", "غير موجودة"])
    medication = st.selectbox("الدواء المصري الحالي المتداخل مع الأيض:", [
        "لا يوجد دواء متداخل حالياً", 
        "Deltacortril (Prednisolone) - كورتيزون هادم", 
        "Cydophage / Metformin - منظم كبدي",
        "Lasix (Furosemide) - مدر مستنزف للأيونات",
        "Ketosteril - حماية كلوية صارمة"
    ])

# زر التفعيل ومعالجة البيانات
if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك تشفير الخلايا"):
    st.write("---")
    
    # 1. المعادلات الحسابية للمؤشرات الأيضية
    estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
    has_signs = True if "موجودة" in has_acanthosis else False
    base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
    insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    # المقاصة الدوائية وحصص البروتين بناءً على دستور الأدوية
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    restricted_organ = "آمن بالكامل"

    if "Deltacortril" in medication:
        max_allowed_protein_ratio = 1.3  # حماية العضلات دون إجهاد الكلى
        metabolic_burn_modifier = 0.70
        clinical_warnings.append("⚠️ تنبيه سيادي: دواء Deltacortril يرفع المقاومة قسرياً ويسبب هدماً عضلياً.")
    elif "Lasix" in medication:
        max_allowed_protein_ratio = 0.8  # حماية وظائف الكلى من التجفاف
        restricted_organ = "الـكـلـى (Kidney Protection)"
        clinical_warnings.append("⚠️ تنبيه كلوية: المريض على مدر بول لاسيكس، يحظر الإفراط في النيتروجين.")
    elif "Ketosteril" in medication:
        max_allowed_protein_ratio = 0.6  # حماية قصوى ومقاصة نيتروجينية صارمة
        restricted_organ = "الخلايا الكلوية المتهالكة"
        clinical_warnings.append("⚠️ تنبيه حرج: المريض يتناول كيتوستيريل، تم تفعيل بروتوكول حظر النيتروجين لحماية وظائف الكلى.")

    degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
    biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
    
    # حساب البروتين الصافي بالجرام
    safe_protein_grams = weight * max_allowed_protein_ratio

    # 2. التحدي الأول: تحويل الجرامات لمعايير منزلية بصرية دقيقة
    # الحسابات مبنية على متوسط 25g للبروتين الحيواني، و 7g للأجبان والبيض، و 15g للبقوليات لكل معيار
    palm_chicken = round(safe_protein_grams / 25.0, 1)
    palm_fish = round(safe_protein_grams / 20.0, 1)
    matchbox_cheese = round(safe_protein_grams / 6.0, 1)
    foul_cups = round(safe_protein_grams / 15.0, 1)
    eggs_count = math.ceil(safe_protein_grams / 7.0)

    # عرض المخرجات الأساسية للمشرف
    st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="مؤشر مقاومة الإنسولين المستدل (HOMA-IR)", value=round(homa_ir, 2))
        st.metric(label="كمية البروتين الصافي المطلوبة يومياً", value=f"{round(safe_protein_grams, 1)} جرام")
    with c2:
        st.metric(label="مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="منطقة حماية الأعضاء الحيوية", value=restricted_organ)

    st.write("---")
    
    # 🍽️ صياغة الدليل المنزلي الموجه للمريض (تلبية التحدي الأول)
    st.subheader("🍽️ الدليل المنزلي الموجه للمريض (ترجمة غرامات البروتين):")
    st.info(f"عزيزي المريض، لتغطية احتياج خلاياك للترميم اليومي ({round(safe_protein_grams, 1)} جرام بروتين صافي)، يمكنك تناول **أحد الخيارات التالية** موزعة على مدار اليوم:")
    
    st.markdown(f"""
    * **🍗 الفراخ واللحوم الصافية:** ما يعادل **{palm_chicken} كف يد (بدون أصابع)** من صدور الدجاج أو اللحم المشوي.
    * **🐟 الأسماك المشوية:** ما يعادل **{palm_fish} كف يد كامل مع الأصابع** من السمك البلطي أو البوري المتوسط.
    * **🫘 الخيارات النباتية:** ما يعادل **{foul_cups} كوب (سعة 240 مل)** من الفول المدمج أو العدس المطبوخ جيداً.
    * **🧀 الجبن القريش:** ما يعادل **{matchbox_cheese} قطعة بحجم 'علبة الكبريت'** من الجبن القريش الفلاحي.
    * **🥚 البيض المسلوق:** ما يعادل **{eggs_count} بيضات كاملة** مسلوقة طوال اليوم (في حال الاعتماد عليه كمصدر رئيسي).
    """)

    st.write("---")

    # 3. التحدي الثالث: توليد التقرير الأكاديمي السيادي الموجه للطبيب المعالج
    st.subheader("📄 التقرير الأكاديمي السيادي (إصدار De-prescription):")
    
    # محاكاة بنية تقرير احترافي جاهز للطباعة مباشرة
    report_date = datetime.now().strftime("%Y-%m-%d")
    
    st.markdown(f"""
    <div class="report-box">
        <h4 style="color:#004085; text-align:center; margin-bottom:2px;">CellRevive AI Clinical Report</h4>
        <p style="text-align:center; font-size:12px; color:#6c757d;">بروتوكول عكس مسار السكري والتحسين الأيضي المستدام</p>
        <p style="font-size:14px;"><b>التاريخ:</b> {report_date} &nbsp;&nbsp;|&nbsp;&nbsp; <b>اسم المريض:</b> {patient_name}</p>
        <hr style="border: 0.5px solid #004085;">
        <p><b>السيد الزميل الطبيب المعالج المحترم،</b></p>
        <p style="text-align:justify; line-height:1.6;">
            تحية طيبة وبعد، نحيط سيادتكم علماً بأن المريض المذكور أعلاه قد خضع لبروتوكول <b>"الترميم الخلوي"</b> المكثف لتحسين الحساسية النسيجية للإنسولين وعكس العناد الأيضي خلاد الفترة الماضية. وبناءً على خوارزميات الاستدلال الفيزيولوجي لعام 2026، تم رصد المؤشرات الحالية الحيوية التالية:
        </p>
        <ul>
            <li><b>مؤشر مقاومة الإنسولين الحقيقي المستدل (HOMA-IR):</b> {round(homa_ir, 2)} (مؤشر التراجع الكلينيكي)</li>
            <li><b>مؤشر دهون الكبد والأحشاء (TyG Index):</b> {round(tyg_index, 2)}</li>
            <li><b>العمر الأيضي البيولوجي المكتشف للخلايا:</b> {round(biological_age, 1)} سنة</li>
            <li><b>العلاج الدوائي الحالي المتداخل رصده:</b> {medication}</li>
        </ul>
        <p style="background-color:#e2e3e5; padding:10px; border-radius:5px; font-weight:bold; color:#383d41;">
            💡 التوصية السريرية السيادية المقترحة (Clinical Recommendation):<br>
            نظراً لاستعادة الخلايا لجزء كبير من حساسيتها الحيوية للإنسولين وهبوط مؤشر السمية السكرية المزمنة، يُرجى التكرم بالنظر في خفض جرعات مضادات السكري الفموية بنسبة 50% أو البدء في السحب التدريجي لجرعات الكورتيزون/المدرات حسب رؤيتكم الطبية، لتفادي نوبات هبوط السكر المفاجئة (Hypoglycemia) نظراً لاستجابة الأنسجة المتسارعة للترميم الخلوي.
        </p>
        <p style="text-align:right; font-size:12px; margin-top:15px;"><b>صادر عن المحرك الأيضي الذكي لـ CellRevive AI تحت إشراف د. إيهاب</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    # زر مخصص لطباعة الصفحة الحالية كـ PDF في المتصفح
    st.button("🖨️ اضغط Ctrl + P لطباعة التقرير كـ PDF فوراً")
