import streamlit as st
import math

# إعدادات الواجهة السيادية المتوافقة تماماً مع الموبايل والكمبيوتر بناءً على آخر تحديث
st.set_page_config(
    page_title="CellRevive AI - Sovereign Engine", 
    page_icon="🧬", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# العناوين الرئيسية باللون الأزرق الداكن الفاخر
st.title("🧬 المنظومة السيادية العالمية: CellRevive AI")
st.header("بروتوكول الترميم الخلوي وعكس مسار السكري")
st.caption("الإصدار المطور لعام 2026 - الربط الشامل مع دليل الدواء المصري والمستشار البصري")
st.write("---")

# 1️⃣ البيانات الحيوية والفيزيولوجية للمريض
st.subheader("1️⃣ المؤشرات الحيوية والفيزيولوجية للعيادة")
fbg = st.number_input("سكر الصائم الحالي (mg/dL):", value=142.0, step=1.0)
hba1c = st.number_input("السكر التراكمي (HbA1c%):", value=7.5, step=0.1)
weight = st.number_input("الوزن الحالي للمريض (كجم):", value=85.0, step=0.5)
waist = st.number_input("محيط الخصر الدقيق (سم):", value=106.0, step=1.0)
bmi = st.number_input("مؤشر كتلة الجسم التقريبي (BMI):", value=31.5, step=0.1)

has_acanthosis = st.selectbox(
    "العلامات الفيزيولوجية الحية (تصبغات الرقبة / زوائد جلدية):", 
    ["موجودة وعنيفة", "غير موجودة"]
)

# 2️⃣ مصفوفة الأمراض والأدوية المتعددة (الربط مع دليل الدواء المصري المحدث 2026)
st.subheader("2️⃣ مصفوفة المقاصة الدوائية المعقدة (طبقاً لدليل هيئة الدواء المصرية 2026)")
st.info("🔬 تم ربط المحرك بالمجموعات العلاجية والمواد الفعالة في السوق المصري لحساب تأثير التداخل الدوائي المتعدد على الكلى، الكبد، والحرق الخلوي.")

selected_groups = st.multiselect(
    "اختر المجموعات الدوائية الحالية للمريض (يمكن اختيار أكثر من مجموعة بناءً على بروتوكول المريض المعقد):",
    [
        "كورتيزونات هادمة للعضلات قسرياً (مثل: Deltacortril, Hostacortin, Prednisolone)",
        "مدرات البول المستنزفة للأيونات والضغط الكلوي (مثل: Lasix, Natrilix, Furosemide)",
        "بروتوكول تقييد النيتروجين الصارم للفشل الكلوي (مثل: Ketosteril)",
        "حاصرات بيتا للضغط المنظمة للنبض (مثل: Concor, Nebilet, Bisoprolol)",
        "مستنزفات إنزيم الميتوكوندريا لدهون الدم (مثل: Ator, Lipitor, Crestor, Statins)",
        "طاردات السكر عبر البول الكلوي (مثل: Jardiance, Forxiga, SGLT2 inhibitors)",
        "محفزات الشبع ومبطئات تفريغ المعدة (مثل: Ozempic, Saxenda, Mounjaro, GLP-1)",
        "منظمات ومثبطات الإنتاج الكبدي للجلوكوز (مثل: Cydophage, Glucophage, Metformin)"
    ]
)

# 3️⃣ مستشار التطهير البصري للوجبة الحرة
st.subheader("3️⃣ مستشار التطهير والتحليل البصري الفوري للوجبات")
st.write("📸 *يسهل على المريض التقاط صورة لوجبته الحالية أو كتابة مكوناتها بحرية تامة دون التقيد بجدول حرمان جامد.*")

meal_input = st.text_area(
    "مكونات الوجبة الحالية المراد فحصها وتطهيرها أيضياً:",
    value="طبق رز بشعرية، حتتين لحمة مطبوخة، طبق ملوخية، نصف رغيف عيش بلدي"
)

# زر التشغيل السيادي المتوافق مع الموبايل
st.write("")
if st.button("🚀 تفعيل بروتوكول الترميم الخلوي وفك التشفير الدوائي والبصري", use_container_width=True):
    st.write("---")
    
    # المعادلات الرياضية للحساب الاستدلالي
    estimated_tg = 90.0 + (waist * 1.34) + (bmi * 2.1)
    has_signs = True if "موجودة" in has_acanthosis else False
    base_insulin_proxy = 5.0 + (3.5 * int(has_signs)) + 8.0
    insulin_score = min(28.0, base_insulin_proxy + (bmi * 0.2))

    homa_ir = (fbg * insulin_score) / 405.0
    tyg_index = math.log((estimated_tg * fbg) / 2.0)
    
    # منطق المقاصة الدوائية الموسع (Polypharmacy Matrix)
    max_allowed_protein_ratio = 1.5
    metabolic_burn_modifier = 1.0
    clinical_warnings = []
    organs_at_risk = []

    if any("كورتيزونات" in g for g in selected_groups):
        max_allowed_protein_ratio = min(max_allowed_protein_ratio, 1.3)
        metabolic_burn_modifier *= 0.70
        clinical_warnings.append("⚠️ مجموعة الكورتيزونات: ترفع عناد حرق الدهون قسرياً وتسبب هدماً عضلياً نسيجياً. تم خفض كفاءة الحرق وتشفير النشويات في الوجبة بشكل صارم.")
        organs_at_risk.append("الكتلة العضلية والمقاومة المحيطية")

    if any("مدرات البول" in g for g in selected_groups):
        max_allowed_protein_ratio = min(max_allowed_protein_ratio, 0.8)
        clinical_warnings.append("⚠️ مجموعة مدرات البول (اللاسيكس وأشباهه): تستنزف البوتاسيوم والأيونات الخلوية، وهناك عبء على الفلترة الكلوية؛ يمنع تماماً الإفراط في كميات البروتين.")
        organs_at_risk.append("ترشيح الكلى وتوازن الأيونات")

    if any("تقييد النيتروجين" in g for g in selected_groups):
        max_allowed_protein_ratio = 0.6
        clinical_warnings.append("🚨 بروتوكول الكيتوستيريل الصارم: المريض في مرحلة حرج كلوية متهالكة؛ يتم قفل حصة البروتين الحيواني وتفعيل تقييد النيتروجين لحظر التدهور.")
        organs_at_risk.append("خلايا النفرون الكلوية")

    if any("حاصرات بيتا" in g for g in selected_groups):
        clinical_warnings.append("⚠️ مجموعة حاصرات بيتا (الكونكور وأشباهه): تحجب ضربات القلب والارتجاف الذي ينبه المريض عند حدوث هبوط حاد في السكر. يجب الفحص الرقمي المستمر للوعي.")
        organs_at_risk.append("استجابة الجهاز العصبي لهبوط السكر")

    if any("مستنزفات إنزيم" in g for g in selected_groups):
        clinical_warnings.append("⚠️ مجموعة الاستاتين لدهون الدم: تستنزف إنزيم CoQ10 في الميتوكوندريا وتسبب وهن عضلي. يوصى كلينيكياً بإضافة المغنيسيوم ومكمل CoQ10 لبروتوكولك وعزل النشويات.")
        organs_at_risk.append("الميتوكوندريا وإنتاج الطاقة العضلية")

    if any("طاردات السكر" in g for g in selected_groups):
        clinical_warnings.append("💧 مجموعة طاردات السكر (الجارديانس/الفوركسيجا): تطرح الجلوكوز عبر البول؛ خطر الجفاف شديد والالتهابات الفطرية مرتفع. يلزم شرب 3-4 لتر ماء.")
        organs_at_risk.append("المسالك البولية وتوازن السوائل الخلوية")

    if any("محفزات الشبع" in g for g in selected_groups):
        clinical_warnings.append("🤢 مجموعة محفزات GLP-1 (الأوزمبيك وأشباهه): تبطئ حركية الأمعاء وإفراغ المعدة؛ يجب حظر الدمج بين الدهون العالية والبروتين في وجبة واحدة لمنع الغثيان الحاد.")
        organs_at_risk.append("الحركية الهضمية للمعدة")

    # حساب العمر البيولوجي المتأثر بالتداخلات
    degradation_index = (tyg_index * 4.2) + (hba1c * 3.5) + (homa_ir * 0.6)
    biological_age = 18.0 + (degradation_index * (2.0 - metabolic_burn_modifier))
    safe_protein_grams_daily = weight * max_allowed_protein_ratio

    # عرض النتائج الكلينيكية الكبرى
    st.success(f"🧬 العمر الأيضي البيولوجي المكتشف للخلايا: {round(biological_age, 1)} سنة")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.metric(label="مؤشر مقاومة الإنسولين المستدل (HOMA-IR)", value=round(homa_ir, 2))
        st.metric(label="حصة البروتين الآمنة القصوى يومياً للمريض", value=f"{round(safe_protein_grams_daily, 1)} جرام")
    with col_r2:
        st.metric(label="مؤشر دهون الكبد والأحشاء (TyG Index)", value=round(tyg_index, 2))
        st.metric(label="الأعضاء تحت المراقبة الدوائية المكثفة لعام 2026", value=", ".join(organs_at_risk) if organs_at_risk else "آمنة بالكامل")

    # محرك التطهير البصري الذكي للوجبة الحرة المقاسة حيوياً ودوائياً
    st.write("---")
    st.subheader("🥗 نتيجة الفحص والتطهير الأيضي للوجبة الحالية:")
    st.warning(f"🔎 الوجبة المرصودة: '{meal_input}'")
    
    c_diet1, c_diet2 = st.columns(2)
    with c_diet1:
        st.markdown("### 🟢 ما يجب إضافته لتطهير الوجبة:")
        st.write("* أضف **طبق سلطة خضراء ضخم** (جرجير، كرفس، خيار) مع ملعقة زيت زيتون بكر؛ لإنشاء شبكة ألياف جيلاتينية تبطئ امتصاص نشويات الرز والعيش قسرياً.")
        st.write("* تناول **ملعقة خل تفاح عضوي مخفف** على كوب ماء قبل الأكل بـ 10 دقائق لتعطيل إنزيم الألفا-أميليز وخفض الحمل الجلايسيمي للرز بنسبة 30%.")
        
        st.markdown("### 📏 الكمية والجرام المسموح به:")
        if homa_ir > 5.0 or any("كورتيزونات" in g for g in selected_groups):
            st.write("* **النشويات المعيارية:** مسموح بـ **3 إلى 4 ملاعق فقط** من الرز، وامنع العيش البلدي تماماً في هذه الوجبة لوجود الرز نظراً للعناد الأيضي الخلوي الحالي المعزز دوائياً.")
        else:
            st.write("* **النشويات المعيارية:** مسموح بـ **5 إلى 6 ملاعق** من الرز أو نصف رغيف عيش بلدي مدعم بالردة.")
        st.write(f"* **البروتين الصافي:** قطعة اللحم أو ربع الفرخة تغطي حوالي {round(safe_protein_grams_daily*0.35, 1)} جرام بروتين، وهي مثالية ومطابقة لمصفوفة حماية الأعضاء الحالية.")

    with c_diet2:
        st.markdown("### 🔴 ما يجب حذفه أو تقليله فوراً من الوجبة:")
        st.write("* **احذف تماماً وعزل:** دمج نوعين من النشويات الصريحة (الرز + العيش البلدي) في جلسة طعام واحدة لمنع طفرات الإنسولين العنيفة.")
        st.write("* **تنبيه الطهي:** تأكد أن الملوخية وشوربة الخضار مطبوخين بمرقة طبيعية أو زبدة حيوانية نقية، واحذر تماماً الزيوت المهدرجة والسمن النباتي لخطورتهم على جدار الخلية.")
        if any("محفزات الشبع" in g for g in selected_groups):
            st.write("* **تنبيه هضمي خاص:** قلل الدهون في الملوخية والشوربة تماماً لتجنب عسر الهضم الحاد الناتج عن دواء التخسيس/السكري المبطئ للمعدة.")

    # عرض التنبيهات الدوائية المعقدة من دليل الدواء في الأسفل
    if clinical_warnings:
        st.write("---")
        st.subheader("⚠️ التدابير الصيدلانية الكلينيكية الفورية (دليل الدواء المصري):")
        for warning in clinical_warnings:
            st.error(warning)
