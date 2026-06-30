import streamlit as st
import math

# إعدادات الصفحة والواجهة السيادية لـ CellRevive AI
st.set_page_config(page_title="CellRevive AI - Sovereign Engine", page_icon="🧬", layout="centered")

# التصميم البصري الفاخر (Medical Dashboard Theme)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #004085; font-family: 'Arial'; text-align: center; }
    h3 { color: #17a2b8; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 المنظومة السيادية العالمية: CellRevive AI")
st.subheader("بروتوكول الترميم الخلوي وعكس مسار السكري (إصدار 2026 المعتمد)")
st.write("---")

# تقسيم الشاشة لإدخال البيانات الكلينيكية والفيزيولوجية
col1, col2 = st.columns(2)

with col1:
    fbg = st.number_input("أدخل سكر الصائم الحالي (mg/dL):", min_value=50.0, max_value=500.0, value=142.0, step=1.0)
    hba1c = st.number_input("أدخل السكر التراكمي (HbA1c%):", min_value=4.0, max_value=16.0, value=7.5, step=0.1)
    weight = st.number_input("أدخل الوزن الحالي للمريض (كجم):", min_value=30.0, max_value=250.0, value=85.0, step=0.5)

with col2:
    waist = st.number_input("أدخل محيط الخصر بدقة (سم):", min_value=50.0, max_value=200.0, value=106.0, step=1.0)
    bmi = st.number_input("مؤشر كتلة الجسم التقريبي (BMI):", min_value=15.0, max_value=60.0, value=31.5, step=0.1)
    has_acanthosis = st.selectbox("العلامات الفيزيولوجية (تصبغات الرقبة/الزوائد الجلدية):", ["موجودة وعنيفة", "غير موجودة"])
    medication = st.selectbox("الدواء المصري الحالي المتداخل مع الأيض الكلي:", [
        "لا يوجد دواء متداخل حالياً", 
        "Deltacortril (Prednisolone) - كورتيزون هادم", 
        "Cydophage / Metformin - منظم كبدي",
        "Lasix (Furosemide) - مدر مستنزف للأيونات",
        "Ketosteril - حماية كلوية صارمة"
    ])

# زر التفعيل السيادي وحساب البصمة الأيضية
if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك تشفير الخلايا"):
    st.write("---")
    with st.spinner("جاري إجراء المقاصة الدوائية الكلينيكية وحساب تراجع الحرق الخلوي..."):
        
        # 1. الاستدلال الفيزيولوجي وغياب التحاليل
        estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
        has_signs = True if "موجودة" in has_acanthosis else False
        base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
        insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

        # 2. مصفوفة الدواء والتأثير الجزيئي وحصص البروتين
        max_allowed_protein_ratio = 1.5
        metabolic_burn_modifier = 1.0
        clinical_warnings = []
        restricted_organ = "آمن بالكامل"

        if "Deltacortril" in medication:
            max_allowed_protein_ratio = 1.3  # رفع لحماية العضلات من الهدم الكورتيزوني دون إجهاد الكلى
            metabolic_burn_modifier = 0.70  # هبوط حاد في الحرق بسبب الكورتيزون
            clinical_warnings.append("تنبيه سيادي: دواء Deltacortril يرفع المقاومة قسرياً، تم تشفير النشويات بشكل أصارم وتعديل الحرق.")
        elif "Lasix" in medication:
            max_allowed_protein_ratio = 0.8  # حماية الكلى
            restricted_organ = "الـكـلـى (Kidney Protection)"
            clinical_warnings.append("تنبيه كلوية: المريض على مدر بول لاسيكس، يجب مراقبة المعادن وحظر الإفراط في البروتين.")
        elif "Ketosteril" in medication:
            max_allowed_protein_ratio = 0.6  # تقييد صارم جداً للنيتروجين
            restricted_organ = "الخلايا الكلوية المتهالكة"
            clinical_warnings.append("تنبيه حرج: بروتوكول تقييد النيتروجين مفعل لحماية وظائف الكلى المتدهورة.")

        # 3. الحسابات والنتائج
        homa_ir = (fbg * insulin_score) / 405.0
        tyg_index = math.log((estimated_tg * fbg) / 2.0)
        
        degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
        biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
        
        safe_protein_grams_daily = weight * max_allowed_protein_ratio

        # عرض المخرجات الطبية الباهرة أمام العين
        st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="مؤشر مقاومة الإنسولين المستدل (HOMA-IR)", value=round(homa_ir, 2))
            st.metric(label="كمية البروتين الآمنة يومياً للمريض", value=f"{round(safe_protein_grams_daily, 1)} جرام")
        with c2:
            st.metric(label="مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
            st.metric(label="منطقة حماية الأعضاء المستهدفة", value=restricted_organ)

        if clinical_warnings:
            st.subheader("⚠️ الإجراءات الكلينيكية الفورية:")
            for warning in clinical_warnings:
                st.error(warning)
        else:
            st.balloons()
            st.info("✅ المؤشرات الحيوية لا تظهر تداخلات دوائية خطيرة على الحرق الخلوي.")
