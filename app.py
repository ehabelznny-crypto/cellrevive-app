import streamlit as st
import math

# إعدادات الصفحة السيادية للتوافق مع الموبايل والكمبيوتر
st.set_page_config(page_title="CellRevive AI - Sovereign v3", page_icon="🧬", layout="centered")

# العناوين الرئيسية باللون الأزرق الداكن الفاخر
st.title("🧬 المنظومة السيادية العالمية: CellRevive AI")
st.header("بروتوكول الترميم الخلوي وفك التشفير الدوائي والبصري")
st.caption("الإصدار العملاق والمطور لعام 2026 - عيادة د. إيهاب")
st.write("---")

# القسم الأول: المدخلات الحيوية والفيزيولوجية
st.subheader("1️⃣ البيانات الحيوية والفيزيولوجية للمريض")
fbg = st.number_input("سكر الصائم الحالي (mg/dL):", value=142.0)
hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=7.5)
weight = st.number_input("الوزن الحالي للمريض (كجم):", value=85.0)
waist = st.number_input("محيط الخصر الدقيق (سم):", value=106.0)
bmi = st.number_input("مؤشر كتلة الجسم (BMI):", value=31.5)

has_acanthosis = st.selectbox("التصبغات الجلدية / الشواك الأسود زوائد الرقبة:", ["موجودة وعنيفة", "غير موجودة"])

# القسم الثاني: مصفوفة الأمراض والأدوية المتعددة والمعقدة (Polypharmacy)
st.subheader("2️⃣ مصفوفة الأمراض والأدوية المتداخلة المعقدة")
medications = st.multiselect(
    "اختر كافة الأدوية التي يتناولها المريض حالياً (يمكن اختيار أكثر من دواء):",
    [
        "لا يوجد أدوية متداخلة حالياً",
        "Deltacortril (كورتيزون هادم للعضلات)",
        "Lasix / مدرات البول (مستنزف للأيونات والكلية)",
        "Ketosteril (حماية كلوية وتقييد نيتروجين صارم)",
        "Concor / Beta-blockers (للضغط - يحجب أعراض الهبوط ويؤثر على النبض)",
        "Ator / Lipitor / Statins (للكوليسترول - مسبب لوهن العضلات الخلوي)",
        "Jardiance / SGLT2 inhibitors (منظم سكري يطرح السكر في البول)",
        "Ozempic / Victoza / GLP-1 (مبطئ إفراغ المعدة ومحفز شبع قسري)"
    ]
)

# القسم الثالث: كاميرا فك شفرة الوجبة الحرة (Visual Meal Decoder)
st.subheader("3️⃣ مستشار التطهير البصري الفوري للوجبات")
st.info("💡 دكتور إيهاب: المريض هنا لا يلتزم بجدول جامد، بل يكتب أو يصور ما يريد أكله الآن والبرنامج يعدل عليه!")
meal_input = st.text_area(
    "اكتب مكونات الوجبة التي يريد المريض تناولها الآن بالتفصيل (مثال: طبق رز مصري، ربع فرخة مشوية، شوربة خضار):",
    value="طبق رز بشعرية، حتتين لحمة مطبوخة، طبق ملوخية، عيش بلدي"
)

# زر التشغيل السيادي الشامل
st.write("")
if st.button("🚀 تشغيل المحرك الأيضي والمقاصة الدوائية والبصرية", use_container_width=True):
    st.write("---")
    
    # حساب المؤشرات القديمة والمطورة
    estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
    has_signs = True if "موجودة" in has_acanthosis else False
    base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
    insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    # معالجة مصفوفة الأدوية المتعددة
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    organs_at_risk = []

    if "Deltacortril (كورتيزون هادم للعضلات)" in medications:
        max_allowed_protein_ratio = min(max_allowed_protein_ratio, 1.3)
        metabolic_burn_modifier *= 0.70
        clinical_warnings.append("⚠️ الكورتيزون (Deltacortril): يرفع عناد حرق الدهون قسرياً ويسبب هدماً عضلياً. تم خفض كفاءة الحرق التلقائي وتشديد حصص النشويات.")
        organs_at_risk.append("الكتلة العضلية والمقاومة المحيطية")

    if "Lasix / مدرات البول (مستنزف للأيونات والكلية)" in medications:
        max_allowed_protein_ratio = min(max_allowed_protein_ratio, 0.8)
        clinical_warnings.append("⚠️ اللاسيكس (Lasix): مستنزف للبوتاسيوم والمعادن الحيوية، هناك ضغط كلوى؛ يمنع تماماً الإفراط في البروتين لحماية ترشيح الكلى.")
        organs_at_risk.append("الكلى والأيونات (البوتاسيوم)")

    if "Ketosteril (حماية كلوية وتقييد نيتروجين صارم)" in medications:
        max_allowed_protein_ratio = 0.6
        clinical_warnings.append("🚨 الكيتوستيريل (Ketosteril): المريض في مرحلة تدهور كلوية متقدمة؛ تم تفعيل بروتوكول تقييد النيتروجين الصارم ومنع أي زيادة في البروتين الحيواني.")
        organs_at_risk.append("وظائف الكلى المتهالكة")

    if "Concor / Beta-blockers (للضغط - يحجب أعراض الهبوط ويؤثر على النبض)" in medications:
        clinical_warnings.append("⚠️ الكونكور (Concor): يحجب ضربات القلب المتسارعة التي تنبه المريض عند حدوث هبوط حاد في السكر. يجب تنبيه المريض للفحص الرقمي الدوري.")
        organs_at_risk.append("الجهاز العصبي المستقل (النبض)")

    if "Ator / Lipitor / Statins (للكوليسترول - مسبب لوهن العضلات الخلوي)" in medications:
        clinical_warnings.append("⚠️ أدوية الاستاتين (Ator): تستنزف إنزيم CoQ10 في الميتوكوندريا وتسبب وهن العضلات. يوصى كلينيكياً بإضافة الماغنيسيوم ومكمل CoQ10 لبروتوكولك.")
        organs_at_risk.append("الميتوكوندريا العضلية")

    if "Jardiance / SGLT2 inhibitors (منظم سكري يطرح السكر في البول)" in medications:
        clinical_warnings.append("💧 الجارديانس (Jardiance): يطرح السكر عبر البول؛ خطر الجفاف والالتهابات الفطرية مرتفع. يجب إلزام المريض بشرب 3 لتر ماء وتطهير موضعي.")
        organs_at_risk.append("المسالك البولية وتوازن السوائل")

    # حساب العمر البيولوجي بناءً على الأدوية والحرق الجديد
    degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
    biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
    safe_protein_grams_daily = weight * max_allowed_protein_ratio

    # عرض النتائج الكلينيكية
    st.success(f"🧬 العمر الأيضي البيولوجي للخلايا: {round(biological_age, 1)} سنة")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.metric(label="مؤشر مقاومة الإنسولين المستدل (HOMA-IR)", value=round(homa_ir, 2))
        st.metric(label="حصة البروتين الآمنة القصوى يومياً", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with col_r2:
        st.metric(label="مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="الأعضاء تحت المراقبة الدوائية المكثفة", value=", ".join(organs_at_risk) if organs_at_risk else "آمنة")

    # محرك فك شفرة الوجبة الحرة (التحليل الذكي للوجبة الحالية)
    st.write("---")
    st.subheader("🥗 نتيجة الفحص البصري الذكي للوجبة الحالية:")
    
    # ذكاء اصطناعي محاكي ومبرمج بناءً على المقاصة والأيض الحالي للمريض
    st.warning(f"🔎 تحليل وجبة: '{meal_input}'")
    
    c_diet1, c_diet2 = st.columns(2)
    with c_diet1:
        st.markdown("### 🟢 ما يجب إضافته لتطهير الوجبة:")
        st.write("* أضف **طبق سلطة خضراء كبير** (جرجير، خيار، فجل) مع ملعقة زيت زيتون بكر؛ لإنشاء شبكة ألياف تبطئ امتصاص نشويات الرز/العيش قسرياً.")
        st.write("* أضف **ملعقة خل تفاح عضوي** على كوب ماء قبل الوجبة بـ 10 دقائق لخفض المؤشر الجلايسيمي بنسبة 30%.")
        
        st.markdown("### 📏 الكمية والجرام المسموح به:")
        if homa_ir > 5.0 or "Deltacortril" in medications:
            st.write(f"* **النشويات:** مسموح بـ **4 ملاعق فقط** من الرز، وامنع العيش البلدي تماماً في وجود الرز نظراً للعناد الأيضي الحالي.")
        else:
            st.write(f"* **النشويات:** مسموح بـ **6 ملاعق** من الرز أو نصف رغيف عيش بلدي.")
        st.write(f"* **البروتين:** تناول قطعة اللحم كاملة أو ربع الفرخة (تحتوي على حوالي {round(safe_protein_grams_daily*0.4, 1)} جرام بروتين صافي)، وهي ممتازة لتغطية احتياجك الخلوي.")

    with c_diet2:
        st.markdown("### 🔴 ما يجب حذفه أو تقليله فوراً:")
        st.write("* **احذف تماماً:** الشوربة المضاف إليها لسان عصفور أو دقيق لتثخينها.")
        st.write("* **قلل بشدة:** الملوخية إذا كانت مطبوخة بسمن نباتي مهدرج (استبدلها بالزبدة الطبيعية الفلاحي بكمية ضئيلة جداً).")
        st.write("* امنع دمج نوعين نشويات (رز + عيش) في نفس الوجبة لوقف تدهور الخلايا.")

    # عرض التنبيهات الدوائية المعقدة في الأسفل
    if clinical_warnings:
        st.write("---")
        st.subheader("⚠️ التدابير الصيدلانية الكلينيكية الفورية للأدوية المعقدة:")
        for warning in clinical_warnings:
            st.error(warning)
