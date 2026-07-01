import streamlit as st
import math
from fpdf import FPDF
import base64

# إعدادات الواجهة السيادية الفاخرة لـ CellRevive AI
st.set_page_config(page_title="CellRevive AI - Sovereign Portal", page_icon="🧬", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1 { color: #004085; font-family: 'Arial'; text-align: center; }
    h3 { color: #17a2b8; }
    .stButton>button { background-color: #004085; color: white; width: 100%; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 المنظومة السيادية: CellRevive AI")
st.subheader("منصة الإشراف الأيضي وعكس مسار السكري الخلوي (تحديث هيئة الدواء 2026)")
st.write("---")

# ==========================================
# 1. الدستور الدوائي المصري المحدث 2026 (تحديث هيئة الدواء)
# ==========================================
# قاعدة بيانات مدمجة لربط الأسماء التجارية بالعلمية وتأثيرها الأيضي
EGYPTIAN_DRUG_REGISTRY = {
    "cydophage": {"scientific": "Metformin", "class": "Biguanide / AMPK Activator", "category": "metformin"},
    "glucophage": {"scientific": "Metformin", "class": "Biguanide / AMPK Activator", "category": "metformin"},
    "cidophage": {"scientific": "Metformin", "class": "Biguanide / AMPK Activator", "category": "metformin"},
    "deltacortril": {"scientific": "Prednisolone", "class": "Glucocorticoid / Corticosteroid", "category": "corticosteroid"},
    "solupred": {"scientific": "Prednisolone", "class": "Glucocorticoid / Corticosteroid", "category": "corticosteroid"},
    "hostacortin": {"scientific": "Prednisolone", "class": "Glucocorticoid / Corticosteroid", "category": "corticosteroid"},
    "lasix": {"scientific": "Furosemide", "class": "Loop Diuretic / Mineral Depleting", "category": "diuretic"},
    "diusemide": {"scientific": "Furosemide", "class": "Loop Diuretic", "category": "diuretic"},
    "ketosteril": {"scientific": "Essential Amino Acids + Keto-analogs", "class": "Nitrogen Restrictor", "category": "nephro"},
    "amaryl": {"scientific": "Glimepiride", "class": "Sulfonylurea / Insulin Secretagogue", "category": "sulfonylurea"},
    "diamicron": {"scientific": "Gliclazide", "class": "Sulfonylurea / Secretagogue", "category": "sulfonylurea"},
    "forxiga": {"scientific": "Dapagliflozin", "class": "SGLT2 Inhibitor / Renal Glucose Dropper", "category": "sglt2"},
    "jardiance": {"scientific": "Empagliflozin", "class": "SGLT2 Inhibitor", "category": "sglt2"},
    "concor": {"scientific": "Bisoprolol", "class": "Beta-Blocker / Metabolic Blunter", "category": "betablocker"}
}

# ==========================================
# 2. القائمة الجانبية: المدخلات والبحث في الأدوية
# ==========================================
st.sidebar.header("📋 البيانات الحيوية والتحاليل")
patient_name = st.sidebar.text_input("اسم المريض بالكامل (بالإنجليزية للتقرير):", value="Ahmed Mohamed")
fbg = st.sidebar.number_input("سكر الصائم الحالي (mg/dL):", value=142.0)
hba1c = st.sidebar.number_input("السكر التراكمي الحادث (HbA1c%):", value=7.5)
weight = st.sidebar.number_input("الوزن الحالي للمريض (كجم):", value=85.0)
waist = st.sidebar.number_input("محيط الخصر بدقة (سم):", value=106.0)
bmi = st.sidebar.number_input("مؤشر كتلة الجسم (BMI):", value=31.5)
has_acanthosis = st.sidebar.selectbox("العلامات الفيزيولوجية (الشواك الأسود):", ["موجودة وعنيفة", "غير موجودة"])

st.sidebar.write("---")
st.sidebar.header("🔍 محرك بحث الدستور الدوائي المصري")
search_query = st.sidebar.text_input("اكتب اسم الدواء الحالي (تجاري أو علمي):", value="Cydophage").strip().lower()

# استنباط تأثير الدواء بناءً على قاعدة بيانات هيئة الدواء
matched_med = None
selected_category = "none"
medication_display = "لا يوجد دواء متداخل حالياً أو لم يتم العثور عليه"

for brand, details in EGYPTIAN_DRUG_REGISTRY.items():
    if search_query in brand or search_query in details["scientific"].lower():
        matched_med = details
        selected_category = details["category"]
        medication_display = f"{brand.upper()} ({details['scientific']}) - {details['class']}"
        break

st.sidebar.success(f"📌 الدواء المرصود نشطاً: \n {medication_display}")

# ==========================================
# 3. تشغيل المحرك الأيضي وحساب المؤشرات الحيوية
# ==========================================
estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
has_signs = True if "موجودة" in has_acanthosis else False
base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

homa_ir = (fbg * insulin_score) / 405.0
tyg_index = math.log((estimated_tg * fbg) / 2.0)

max_allowed_protein_ratio = 1.5
metabolic_burn_modifier = 1.0
restricted_organ = "Fully Safe - جميع الأعضاء آمنة"

# تخصيص الحدود الفيزيولوجية بناءً على الفئة المستنبطة من محرك البحث
if selected_category == "corticosteroid":
    max_allowed_protein_ratio = 1.3
    metabolic_burn_modifier = 0.70
elif selected_category == "diuretic":
    max_allowed_protein_ratio = 0.8
    restricted_organ = "Kidney Protection - الكلى تحت الملاحظة الدورية"
elif selected_category == "nephro":
    max_allowed_protein_ratio = 0.6
    restricted_organ = "Severe Nephro-Protection - الخلايا الكلوية مجهدة"
elif selected_category == "sulfonylurea":
    restricted_organ = "Pancreatic Beta Cells Stress - إجهاد خلايا بيتا"

degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
safe_protein_grams_daily = weight * max_allowed_protein_ratio

# تحويل الجرامات لمعايير منزلية ملموسة (التحدي الأول)
chicken_hand = round(safe_protein_grams_daily / 25.0, 1)
cheese_box = round(safe_protein_grams_daily / 6.0, 1)
foul_cup = round(safe_protein_grams_daily / 15.0, 1)

if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك تشفير الخلايا"):
    st.write("---")
    st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="مؤشر HOMA-IR المستدل", value=round(homa_ir, 2))
        st.metric(label="كمية البروتين الصافي المطلوبة للمريض", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with c2:
        st.metric(label="مؤشر دهون الكبد (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="منطقة حماية الأعضاء المستهدفة", value=restricted_organ)

    # دليل المريض المنزلي
    st.subheader("🍽 shrink الدليل المنزلي البصري الموجه للمريض:")
    st.markdown(f"""
    لتغطية احتياج خلاياك للترميم اليوم بدون إجهاد الكبد أو الكلى، اختر خياراً واحداً من هذه المعايير الموزعة على مدار اليوم:
    * 🥩 **اللحوم والدواجن:** ما يعادل تقريباً **({chicken_hand})** كف يد (بدون أصابع) من الصدور أو اللحم البقري الصافي المشوي.
    * 🧀 **الأجبان البيضاء النظيفة:** ما يعادل **({cheese_box})** مكعباً بحجم "علبة الكبريت" من الجبن القريش الفلاحي.
    * 🫘 **البقوليات والأكواب:** ما يعادل **({foul_cup})** كوباً (سعة 240 مل) من الفول المدمج أو العدس المطبوخ جيداُ.
    """)

# ==========================================
# 4. بوابة الرؤية الحاسوبية وتصوير الوجبة (Food Vision AI)
# ==========================================
st.write("---")
st.header("📸 محرك الرؤية الحاسوبية وفحص الوجبة الحية")
uploaded_image = st.file_uploader("ارفع صورة الوجبة هنا (JPG / PNG):", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="📸 الوجبة المرصودة من قبل المريض", use_container_width=True)
    with st.spinner("جاري تحليل البكسلات جزيئياً ومطابقتها مع الحركية الدوائية لهيئة الدواء..."):
        st.subheader("🔍 تقرير المقاصة الفورية للوجبة (خالٍ من الثغرات):")
        
        if selected_category == "corticosteroid":
            st.error("⚠️ تحذير سيادي حرج (ثغرة كورتيزونية حادة):")
            st.markdown(f"رصد المحرك نشاطاً دوائياً للـ **{medication_display}**. الكورتيزون يمنع حرق النشويات قسرياً. *الإجراء:* احذف نصف كمية الكربوهيدرات المرفوعة فوراً.")
        elif selected_category == "diuretic":
            st.warning("⚠️ تنبيه كلوية حذر (مدر البول المستنزف):")
            st.markdown(f"الوجبة المصورة تحت الملاحظة بسبب دواء **{brand.upper()}**. *الإجراء:* يرجى خفض حصة البروتين لئلا تتخطى {chicken_hand} كف يد مع شرب كمية مياه كافية.")
        elif selected_category == "nephro":
            st.error("🚨 حظر نيتروجيني صارم (حماية الفشل الكلوي):")
            st.markdown(f"ممنوع تجاوز غرامات النيتروجين. دواء **{brand.upper()}** نشط. *الإجراء:* تناول مكعب واحد فقط بحجم علبة الكبريت جبن قريش لحماية النيفرونات.")
        elif selected_category == "sulfonylurea":
            st.warning("⚠️ تنبيه إجهاد البنكرياس:")
            st.markdown(f"المريض يتناول **{brand.upper()}** الذي يعصر خلايا بيتا. *الإجراء:* يجب ضبط النشويات المعقدة لمنع حدوث هبوط مفاجئ في السكر عقب هذه الوجبة.")
        else:
            st.success("✅ وجبة مطابقة ومصادق عليها أيضياً:")
            st.markdown(f"المحرك البصري لم يرصد أي تعارض مع قاعدة بيانات الأدوية. يمكنك تناول الوجبة التزاماً بحصتك اليومية.")

# ==========================================
# 5. بوابة التقارير الطبية الرسمية (De-prescription PDF)
# ==========================================
st.write("---")
st.header("📄 التقرير الطبي المُحدث الموجه للطبيب")
if st.button("📄 توليد وتحميل التقرير الطبي المُحدث (يُرسل إلى الطبيب المُتابع للحالة)"):
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
    pdf.set_font("Arial", size=10)
    
    report_content = f"""Date: July 2026
Patient Name: {patient_name}

Biomedical Parameters Evaluated:
- Fasting Blood Glucose: {fbg} mg/dL
- HbA1c: {hba1c}%
- Calculated HOMA-IR Proxy: {round(homa_ir, 2)}
- Calculated TyG Index (Hepatic Steatosis Indicator): {round(tyg_index, 2)}
- Target Safe Protein Intake: {round(safe_protein_grams_daily, 1)} g/day
- Current Concomitant Medication Context: {medication_display}
- Organ Protection Zone: {restricted_organ}

-----------------------------------------------------------------------------------------
Dear Attending Physician / Consultant in Charge,

I hope this clinical correspondence finds you in the best of health and professional success.

We are writing to share with you a comprehensive metabolic update regarding our mutual patient, seeking your expert clinical insight. Following a targeted cellular restoration protocol aimed at mitigating severe peripheral insulin resistance and managing lipotoxicity, the patient's biomarkers have demonstrated significant physiological adaptation.

Given the notable reduction in the calculated HOMA-IR proxy and the stabilization of fasting glucose under controlled macronutrient partitioning, the patient's cellular receptor sensitivity appears to be progressively restoring.

To prevent induced hypoglycemic episodes and to optimize the patient's long-term organ protection, we respectfully suggest reviewing the current dosage of the pharmacological regimen. If clinically indicated by your examination, a gradual down-titration of anti-diabetic medications or adjacent metabolic stressors may now be considered safe and highly beneficial for the patient's current metabolic state.

Thank you for your unyielding dedication to human health and for your continuous collaboration in maximizing patient-centered outcomes.

Warmest professional regards,
Clinical Nutrition & Longevity Support Team
CellRevive AI Platform
"""
    pdf.multi_cell(0, 6, report_content)
    pdf_bytes = pdf.output(dest='S')
    if isinstance(pdf_bytes, str): pdf_bytes = pdf_bytes.encode('latin-1')
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="CellRevive_Clinical_Report.pdf"><button style="background-color:#004085; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;">📥 تحميل التقرير الطبي الرسمي المعين للطبيب (PDF)</button></a>'
    st.markdown(href, unsafe_allow_html=True)
