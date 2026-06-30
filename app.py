from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
# استدعاء المحرك السيادي الذي قمت برفعه مسبقاً
from main import CellReviveSovereignEngine

app = FastAPI(
    title="CellRevive AI - Sovereign Metabolic API",
    description="الواجهة البرمجية السيادية لمنظومة عكس مسار السكري والترميم الخلوي",
    version="2.0.0"
)

# إنشاء نسخة نشطة من المحرك في ذاكرة السيرفر
sovereign_engine = CellReviveSovereignEngine()

# --- نماذج استقبال البيانات المشفرة من هاتف المريض ---
class LabMetricsInput(BaseModel):
    fbg: float       # السكر الصائم
    insulin: float   # الإنسولين الصائم
    tg: float        # الدهون الثلاثية
    hdl: float       # الكوليسترول النافع
    hba1c: float     # السكر التراكمي

class CellularRepairInput(BaseModel):
    metrics: Dict[str, float]
    sleep_hours: float
    stress_level: float
    bmi: float

class FoodItem(BaseModel):
    name: str
    visual_units: float

class PlateAnalysisInput(BaseModel):
    detected_foods: List[FoodItem]
    cri_metrics: Dict[str, Any]

# --- بوابات السيرفر التفاعلية (API Endpoints) ---

@app.post("/api/v2/metabolic-profile", tags=["Metabolic Engine"])
def get_metabolic_profile(data: LabMetricsInput):
    """بوابة حساب البصمة الأيضية والعمر البيولوجي الخلوي"""
    try:
        results = sovereign_engine.calculate_metabolic_phenotype(
            fbg=data.fbg, insulin=data.insulin, tg=data.tg, hdl=data.hdl, hba1c=data.hba1c
        )
        return {"status": "SUCCESS", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في المعالجة الحتمية: {str(e)}")

@app.post("/api/v2/cellular-repair", tags=["Autophagy Engine"])
def get_cellular_repair_index(data: CellularRepairInput):
    """بوابة حساب مؤشر الترميم الخلوي وتحديد ساعات الصيام الديناميكي"""
    try:
        results = sovereign_engine.compute_cellular_repair_index(
            metrics=data.metrics, sleep_hours=data.sleep_hours, stress_level=data.stress_level, bmi=data.bmi
        )
        return {"status": "SUCCESS", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في خوارزمية الصيام: {str(e)}")

@app.post("/api/v2/plate-scan", tags=["AI Vision Simulator"])
def analyze_patient_plate(data: PlateAnalysisInput):
    """بوابة فحص صورة الطبق وتفعيل مصفوفة الإنقاذ والتعويض الحيوي اللحظي"""
    try:
        # تحويل البيانات القادمة إلى الصيغة التي يفهمها المحرك
        foods_list = [{"name": item.name, "visual_units": item.visual_units} for item in data.detected_foods]
        results = sovereign_engine.analyze_and_modify_plate(
            detected_foods=foods_list, cri_metrics=data.cri_metrics
        )
        return {"status": "SUCCESS", "data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في هندسة الوجبة البصرية: {str(e)}")

# أمر تشغيل السيرفر محلياً للفحص والتدقيق
if __name__ == "__main__":
    import uvicorn
    print(">>> جاري تشغيل خادم الويب السيادي لـ CellRevive AI بنجاح...")
    uvicorn.run(app, host="0.0.0.0", port=8000)