from typing import Dict, Any

class CellReviveVoiceAndSupplementEngine:
    """
    Sovereign Voice & Supplement Engine for Week 2 (Cellular Resuscitation Phase).
    Dynamically generates personalized voice copy and targeted nutrient micro-dosing.
    """
    
    def __init__(self):
        # قاعدة بيانات المكملات الخلوية الأساسية للأسبوع الثاني
        self.supplement_protocols = {
            "mitochondrial_recharge": {
                "Alpha-Lipoic Acid (ALA)": "600 mg before the first meal (30 mins)",
                "Vitamin B-Complex (Active)": "1 Capsule with the first bite of food",
                "Folic Acid (Methylfolate)": "400 mcg with the first meal"
            },
            "cortisol_stabilization": {
                "Magnesium Glycinate": "400 mg before sleep (45 mins)",
                "Ashwagandha (KSM-66)": "300 mg with the last meal to block night cortisol"
            }
        }

    def generate_week2_protocol(self, patient_metrics: Dict[str, float], sleep_hours: float, user_status: str) -> Dict[str, Any]:
        """
        توليد الجرعات الطبية والنصوص الصوتية المخصصة للأسبوع الثاني بناءً على الحالة اللحظية للمريض
        """
        homa_ir = patient_metrics.get("homa_ir", 1.0)
        
        # 1. تحديد بروتوكول المكملات ديناميكياً
        active_supplements = {}
        active_supplements.update(self.supplement_protocols["mitochondrial_recharge"])
        
        if sleep_hours < 6.0 or user_status == "STRESSED":
            active_supplements.update(self.supplement_protocols["cortisol_stabilization"])
            voice_prompt = (
                "مرحباً بك في الأسبوع الثاني للترميم الخلوي. رصدنا انخفاضاً في جودة النوم؛ "
                "تم تفعيل بروتوكول حماية الخلية من الكورتيزول وتعديل مكملات المغنيسيوم ليلاً لحماية البنكرياس."
            )
        else:
            voice_prompt = (
                "صباح السيادة الخلوية! خلاياك أتمت مرحلة التطهير بنجاح، ونبدأ اليوم شحن الميتوكوندريا "
                "بمركبات ألفا-ليبويك وفيتامينات ب المكثفة لفتح بوابات الطاقة وعكس المقاومة حتماً."
            )
            
        # 2. تعديل جرعة ALA بناءً على شدة مقاومة الإنسولين
        if homa_ir > 4.0:
            active_supplements["Alpha-Lipoic Acid (ALA)"] = "600 mg twice daily (Before first and last meal by 30 mins) due to high cellular resistance."

        return {
            "week_number": 2,
            "phase_name": "Cellular Resuscitation & Mitochondrial Recharge (إعادة الإحياء وشحن الميتوكوندريا)",
            "personalized_voice_prompt": voice_prompt,
            "targeted_supplements": active_supplements
        }

# --- وحدة الفحص والتشغيل التجريبية التلقائية ---
if __name__ == "__main__":
    engine = CellReviveVoiceAndSupplementEngine()
    
    # محاكاة بيانات مريض يعاني من مقاومة إنسولين عالية ونقص نوم
    mock_labs = {"homa_ir": 4.5, "tyg_index": 9.1}
    
    week2_plan = engine.generate_week2_protocol(patient_metrics=mock_labs, sleep_hours=5.5, user_status="STRESSED")
    
    print("=== [إصدار الأسبوع الثاني: نظام المساعد الصوتي والمكملات] ===")
    print(f"\n▶ النص الصوتي للمساعد الذكي:\n\"{week2_plan['personalized_voice_prompt']}\"")
    print("\n📦 بروتوكول المكملات الجزيئية المستهدفة:")
    for supp, dose in week2_plan['targeted_supplements'].items():
        print(f" - {supp}: {dose}")