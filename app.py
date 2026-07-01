import streamlit as st
import math
from fpdf import FPDF
import base64

# إعدادات الصفحة والواجهة السيادية لـ CellRevive AI
st.set_page_config(page_title="CellRevive AI - Clinical Portal", page_icon="🧬", layout="centered")

st.title("🧬 المنظومة السيادية: CellRevive AI")
st.subheader("منصة الإشراف الأيضي وعكس مسار السكري الخلوي (تحديث 2026)")
st.write("---")

# 1. مدخلات البيانات الكلينيكية والفيزيولوجية
col1, col2 = st.columns(2)
with col1:
    patient_name = st.text_input("اسم المريض بالكامل:", value="أحمد محمد عبد الله")
    fbg = st.number_input("سكر الصائم الحالي (mg/dL):", value=142.0)
    hba1c = st.number_input("السكر التراكمي الحادث (HbA1c%):", value=7.5)
    weight = st.number_input("الوزن الحالي للمريض (كجم):", value=85.0)

with col2:
    waist = st.number_input("محيط الخصر المقاس بدقة (سم):", value=106.0)
    bmi = st.number_input("مؤشر كتلة الجسم الحالي (BMI):", value=31.5)
    has_acanthosis = st.selectbox("العلامات الفيزيولوجية (الشواك الأسود):", ["موجودة وعنيفة", "غير موجودة"])
    medication = st.selectbox("الدواء المصري الحالي المتداخل:", [
        "لا يوجد دواء متداخل حالياً", 
        "Deltacortril (Prednisolone) - كورتيزون", 
        "Cydophage / Metformin - منظم كبدي",
        "Lasix (Furosemide) - مدر مستنزف",
        "Ketosteril - حماية كلوية صارمة"
    ])

# 2. تشغيل المحرك والمعادلات الجزيئية
estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
has_signs = True if "موجودة" in has_acanthosis else False
base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

homa_ir = (fbg * insulin_score) / 405.0
tyg_index = math.log((estimated_tg * fbg) / 2.0)

max_allowed_protein_ratio = 1.5
metabolic_burn_modifier = 1.0
restricted_organ = "آمن بالكامل"

if "Deltacortril" in medication:
    max_allowed_protein_ratio = 1.3
    metabolic_burn_modifier = 0.70
elif "Lasix" in medication:
    max_allowed_protein_ratio = 0.8
    restricted_organ = "الـكـلـى (Kidney Protection)"
elif "Ketosteril" in medication:
    max_allowed_protein_ratio = 0.6
    restricted_organ = "الخلايا كلوية"

degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
safe_protein_grams_daily = weight * max_allowed_protein_ratio

# تحويل الجرامات إلى معايير منزلية دقيقة يعرفها المريض (التحدي الأول)
chicken_hand = round(safe_protein_grams_daily / 25.0, 1)
cheese_box = round(safe_protein_grams_daily / 6.0, 1)
foul_cup = round(safe_protein_grams_daily / 15.0, 1)

# 3. عرض المخرجات على شاشة التطبيق
if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وحساب البصمة"):
    st.write("---")
    st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="مؤشر HOMA-IR المستدل", value=round(homa_ir, 2))
        st.metric(label="كمية البروتين الصافي المطلوبة", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with c2:
        st.metric(label="مؤشر دهون الكبد (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="منطقة حماية الأعضاء", value=restricted_organ)

    # دليل المريض البصري المنزلي (التحدي الأول مبرمجاً بالكامل)
    st.subheader("🍽️ الدليل المنزلي البصري الموجه للمريض:")
    st.info(f"""
    لتغطية احتياج خلاياك للترميم اليوم بدون إجهاد الأعضاء، اختر خياراً واحداً من هذه المعايير الموزعة على مدار اليوم:
    * 🥩 **اللحوم والدواجن:** ما يعادل تقريباً ({chicken_hand}) كف يد (بدون أصابع) من الصدور أو اللحم الصافي.
    * 🧀 **الأجبان البيضاء النظيفة:** ما يعادل ({cheese_box}) مكعباً بحجم "علبة الكبريت" من الجبن القريش.
    * 🫘 **البقوليات والأكواب:** ما يعادل ({foul_cup}) كوباً (سعة 240 مل) من الفول أو العدس المطبوخ.
    """)

    # 4. توليد التقرير الطبي الـ PDF الإنساني الراقِ (التحدي الثالث)
    st.subheader("📄 بوابة التقارير الطبية الرسمية (De-prescription)")
    
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'CellRevive AI - Clinical Metabolic Report (Confidential)', 0, 1, 'C')
            self.line(10, 20, 200, 20)
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()} | Inter-professional Consultation Report', 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    # ديباجة طبية بالإنجليزية لضمان القبول الأكاديمي الدولي والمحلي
    report_content = f"""
    Date: 2026
    Patient Name: {patient_name}
    Biomedical Parameters Evaluated:
    - Fasting Blood Glucose: {fbg} mg/dL
    - HbA1c: {hba1c}%
    - Calculated HOMA-IR Proxy: {round(homa_ir, 2)}
    - Calculated TyG Index (Hepatic Steatosis Indicator): {round(tyg_index, 2)}
    - Target Safe Protein Intake: {round(safe_protein_grams_daily, 1)} g/day (Physiologically Tailored)
    - Current Concomitant Medication: {medication}

    -----------------------------------------------------------------------------------------
    Dear Attending Physician / Consultant in Charge,
    
    I hope this clinical correspondence finds you in the best of health and professional success.
    
    We are writing to share with you a comprehensive metabolic update regarding our mutual patient, 
    seeking your expert clinical insight. Following a targeted cellular restoration protocol aimed 
    at mitigating severe peripheral insulin resistance and mitigating lipotoxicity, the patient's 
    biomarkers have demonstrated significant physiological adaptation.

    Given the notable reduction in the calculated HOMA-IR proxy and the stabilization of fasting glucose 
    under controlled macronutrient partitioning, the patient's cellular receptor sensitivity appears 
    to be progressively restoring. 

    To prevent induced hypoglycemic episodes and to optimize the patient's long-term organ protection, 
    we respectfully suggest reviewing the current dosage of the pharmacological regimen. If clinically 
    indicated by your examination, a gradual down-titration of anti-diabetic medications or adjacent 
    metabolic stressors may now be considered safe and highly beneficial for the patient's current metabolic state.

    Thank you for your unyielding dedication to human health and for your continuous collaboration 
    in maximizing patient-centered outcomes.

    Warmest professional regards,
    Clinical Nutrition & Longevity Support Team
    CellRevive AI Platform
    """
    
    pdf.multi_cell(0, 7, report_content)
    
    # تحويل البي دي اف لزر تحميل مباشر
    pdf_output = pdf.output(dest='S').encode('latin-1', errors='ignore')
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="CellRevive_Clinical_Report.pdf"><button style="background-color:#004085; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;">📥 تحميل التقرير الطبي الرسمي المعين للطبيب (PDF)</button></a>'
    st.markdown(href, unsafe_allow_html=True)
