from typing import Dict, Any, List

class Week2FoodMatrixEngine:
    """
    Epigenetic Food & Polyphenol Matrix Engine for Week 2.
    Detects metabolic accelerators and computes bio-rejuvenation scores.
    """
    
    def __init__(self):
        # قاعدة بيانات الأطعمة المسرّعة للترميم الخلوي للأسبوع الثاني
        self.polyphenol_db = {
            "extra_virgin_olive_oil": {"type": "Membrane Rebuilder", "power_score": 9.5, "action": "ترميم مرونة غشاء الخلية"},
            "avocado": {"type": "Membrane Rebuilder", "power_score": 9.0, "action": "تغذية غلاف المستقبلات الخلوية"},
            "blueberries": {"type": "Mito-Stimulator", "power_score": 9.8, "action": "تحفيز جينات SIRT1 وتجديد الميتوكوندريا"},
            "broccoli": {"type": "Microbiome Modulator", "power_score": 8.8, "action": "إنتاج البوتيريت وعكس التهاب الكبد الدهني"}
        }

    def evaluate_week2_plate(self, captured_foods: List[str]) -> Dict[str, Any]:
        """
        تحليل محتويات طبق المريض بصرياً ورصد جزيئات الشفاء الفوق جينية للأسبوع الثاني
        """
        detected_accelerators = []
        total_rejuvenation_score = 0.0
        clinical_recommendations = []

        for food in captured_foods:
            if food in self.polyphenol_db:
                food_info = self.polyphenol_db[food]
                detected_accelerators.append({
                    "food_name": food,
                    "classification": food_info["type"],
                    "cellular_action": food_info["action"]
                })
                total_rejuvenation_score += food_info["power_score"]

        # صياغة التوصية الطبية التكيفية بناءً على مكونات الطبق
        if total_rejuvenation_score >= 18.0:
            status = "OPTIMAL_MITOCHONDRAL_CHARGE (شحن ميتوكوندري ممتاز)"
            clinical_recommendations.append("طبقك هندسي ومثالي للأسبوع الثاني. غشاء خلاياك يستعيد مرونته الآن.")
        elif total_rejuvenation_score > 0:
            status = "PARTIAL_REPAIR (ترميم جزئي)"
            clinical_recommendations.append("الطبق جيد، ولكن ننصح بإضافة ملعقة من زيت الزيتون البكر أو حفنة توت أزرق لرفع كفاءة مستقبلات الإنسولين.")
        else:
            status = "ZERO_ACCELERators (غياب المسرعات)"
            clinical_recommendations.append("هذا الطبق خالي من محفزات فوق الجينات للأسبوع الثاني. أضف البروكلي أو الدهون الفسفورية فوراً لحماية الخلية.")

        return {
            "detected_accelerators": detected_accelerators,
            "plate_rejuvenation_score": round(total_rejuvenation_score, 1),
            "metabolic_status": status,
            "clinical_guidance": clinical_recommendations
        }

# --- وحدة التشغيل والفحص التجريبية ---
if __name__ == "__main__":
    engine = Week2FoodMatrixEngine()
    
    # محاكاة قيام مريض بتصوير طبق يحتوي على أفوكادو وتوت بري في وجبة الأسبوع الثاني
    patient_plate = ["avocado", "blueberries"]
    
    analysis_results = engine.evaluate_week2_plate(captured_foods=patient_plate)
    
    print("=== [تحليل الهندسة الجزيئية للطبق - الأسبوع الثاني] ===")
    print(f"\n📊 تقييم التجدد الخلوي للوجبة: {analysis_results['plate_rejuvenation_score']} / 20")
    print(f"🧬 الحالة الأيضية اللحظية: {analysis_results['metabolic_status']}")
    print(f"💡 التوجيه الإكلينيكي السيادي: \"{analysis_results['clinical_guidance'][0]}\"")
    print("\n🔍 المكونات النشطة المرصودة:")
    for acc in analysis_results['detected_accelerators']:
        print(f" - [{acc['food_name']}] يعمل كـ ({acc['classification']}) -> التأثير: {acc['cellular_action']}")