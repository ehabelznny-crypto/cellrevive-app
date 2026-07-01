import streamlit as st
import math

# 1. إعدادات الصفحة السيادية لضمان التوافق الكامل مع الموبايل (أندرويد وآيفون)
st.set_page_config(
    page_title="CellRevive AI", 
    page_icon="🧬", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 2. العناوين الرئيسية بالألوان الرسمية المستقرة (أزرق داكن خط كبير وواضح)
st.title("🧬 المنظومة المتكاملة للترميم الخلوي: CellRevive AI")
st.header("بروتوكول الترميم الخلوي وعكس مسار السكري")
st.caption("إصدار عام 2026 المعتمد للعيادات والمقاصة الدوائية")
st.write("---")

# 3. تقسيم المدخلات لتناسب شاشات الموبايل والكمبيوتر تلقائياً
fbg = st.number_input("سكر الصائم الحالي (mg/dL):", value=142.0, step=1.0)
hba1c = st.number_input("السكر التراكمي الحجمي (HbA1c%):", value=7.5, step=0.1)
weight = st.number_input("الوزن الحالي للمريض (كجم):", value=85.0, step=0.5)
waist = st.number_input("محيط الخصر الدقيق (سم):", value=106.0, step=1.0)
bmi = st.number_input("مؤشر كتلة الجسم التقريبي (BMI):", value=31.5, step=0.1)

has_acanthosis = st.selectbox(
    "العلامات الفيزيولوجية الحية (تصبغات الرقبة / الزوائد):", 
    ["موجودة وعنيفة", "غير موجودة"]
)

medication = st.selectbox(
    "اختر الدواء الحالي المتداخل مع الخلايا:", 
    [
        "لا يوجد دواء متداخل حالياً", 
        "Deltacortril (Prednisolone) - كورتيزون هادم", 
        "Cydophage / Metformin - منظم كبدي",
        "Lasix (Furosemide) - مدر مستنزف للأيونات",
        "Ketosteril - حماية كلوية صارمة"
    ]
)

# 4. زر التفعيل السيادي كبير ومتوافق مع لمس الهاتف
st.write("")
activate_button = st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك تشفير الخلايا", use_container_width=True)

# 5. معالجة البيانات وإخراج النتائج ببطاقات واضحة جداً
if activate_button:
    st.write("---")
    
    # المعادلات الرياضية والمنطق الكلينيكي
    estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
    has_signs = True if "موجودة" in has_acanthosis else False
    base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
    insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    restricted_organ = "آمن بالكامل"

    if "Deltacortril" in medication:
        max_allowed_protein_ratio = 1.3
        metabolic_burn_modifier = 0.70
        clinical_warnings.append("تنبيه سيادي: دواء Deltacortril يرفع المقاومة قسرياً، تم تشفير النشويات وتعديل بروتوكول الحرق الخلوي.")
    elif "Lasix" in medication:
        max_allowed_protein_ratio = 0.8
        restricted_organ = "الـكـلـى (Kidney Protection)"
        clinical_warnings.append("تنبيه كلوية: المريض على مدر بول لاسيكس، يجب مراقبة المعادن بحذر.")
    elif "Ketosteril" in medication:
        max_allowed_protein_ratio = 0.6
        restricted_organ = "الخلايا الكلوية المتهالكة"
        clinical_warnings.append("تنبيه حرج: بروتوكول تقييد النيتروجين مفعل لحماية وظائف الكلى المتدهور.")

    degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
    biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
    safe_protein_grams_daily = weight * max_allowed_protein_ratio

    # عرض المخرجات ببطاقات واضحة الخلفية والألوان على الموبايل
    st.success(f"🧬 العمر الأيضي البيولوجي المكتشف للخلايا: {round(biological_age, 1)} سنة")
    
    st.metric(label="📊 مؤشر مقاومة الإنسولين المستدل (HOMA-IR)", value=round(homa_ir, 2))
    st.metric(label="🥩 كمية البروتين الآمنة الموصى بها يومياً", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    st.metric(label="🧠 مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
    st.metric(label="🛡️ منطقة حماية الأعضاء المستهدفة", value=restricted_organ)

    if clinical_warnings:
        st.subheader("⚠️ الإجراءات الكلينيكية الفورية:")
        for warning in clinical_warnings:
            st.error(warning)
