import streamlit as st
import math

# ==========================================
# 1. الواجهة البصرية والتصميم (التحديث الجديد)
# ==========================================
st.set_page_config(page_title="CellRevive AI", page_icon="🧬", layout="centered")

st.title("🧬 المنظومة السيادية: CellRevive AI")
st.subheader("بروتوكول الترميم الخلوي وعكس مسار السكري")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    fbg = st.number_input("سكر الصائم (mg/dL):", value=142.0)
    hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=7.5)
    weight = st.number_input("الوزن الحالي (كجم):", value=85.0)
with col2:
    waist = st.number_input("محيط الخصر (سم):", value=106.0)
    bmi = st.number_input("مؤشر كتلة الجسم (BMI):", value=31.5)
    has_acanthosis = st.selectbox("التصبغات الجلدية / الشواك الأسود:", ["موجودة وعنيفة", "غير موجودة"])
    medication = st.selectbox("الدواء الحالي المتداخل:", [
        "لا يوجد دواء متداخل حالياً", 
        "Deltacortril (Prednisolone)", 
        "Cydophage / Metformin",
        "Lasix (Furosemide)",
        "Ketosteril"
    ])

# ==========================================
# 2. تشغيل المحرك والمعادلات (الدمج بين القديم والجديد)
# ==========================================
if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك تشفير الخلايا"):
    st.write("---")
    
    # حسابات المؤشرات الحيوية (المنطق القديم المطور)
    estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
    has_signs = True if "موجودة" in has_acanthosis else False
    base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
    insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    # المقاصة الدوائية وحصص البروتين (منطق الأدوية)
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    restricted_organ = "آمن بالكامل"

    if "Deltacortril" in medication:
        max_allowed_protein_ratio = 1.3
        metabolic_burn_modifier = 0.70
        clinical_warnings.append("تنبيه سيادي: دواء Deltacortril يرفع المقاومة قسرياً.")
    elif "Lasix" in medication:
        max_allowed_protein_ratio = 0.8
        restricted_organ = "الـكـلـى (Kidney)"
        clinical_warnings.append("تنبيه كلوية: المريض على مدر بول لاسيكس.")
    elif "Ketosteril" in medication:
        max_allowed_protein_ratio = 0.6
        restricted_organ = "الخلايا الكلوية"
        clinical_warnings.append("تنبيه حرج: بروتوكول تقييد النيتروجين مفعل لحماية وظائف الكلى.")

    degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
    biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
    safe_protein_grams_daily = weight * max_allowed_protein_ratio

    # عرض النتائج النهائية على الواجهة
    st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="مؤشر HOMA-IR المستدل", value=round(homa_ir, 2))
        st.metric(label="كمية البروتين الآمنة يومياً", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with c2:
        st.metric(label="مؤشر دهون الكبد (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="منطقة حماية الأعضاء", value=restricted_organ)

    if clinical_warnings:
        for warning in clinical_warnings:
            st.error(warning)
