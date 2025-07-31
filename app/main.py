# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .model_loader import load_model
from hazm import Normalizer
import re

app = FastAPI(
    title="سیستم طبقه‌بندی ایمیل",
    description="سرویس طبقه‌بندی خودکار ایمیل‌ها با استفاده از یادگیری ماشین",
    version="1.0.0"
)

# بارگیری مدل هنگام راه‌اندازی سرویس
model, label_map = load_model()

# ساختار درخواست
class EmailRequest(BaseModel):
    text: str

# نرمال‌ساز متن
normalizer = Normalizer()

def preprocess_text(text: str) -> str:
    """پیش‌پردازش متن ایمیل"""
    text = normalizer.normalize(text)
    text = re.sub(r'[^\w\s]', '', text)  # حذف علائم نگارشی
    return text

@app.post("/classify")
async def classify_email(request: EmailRequest):
    """
    متن ایمیل را دریافت و دسته‌بندی آن را برمی‌گرداند
    
    نمونه درخواست:
    {
        "text": "لطفا قیمت محصول X را اعلام کنید"
    }
    """
    # پیش‌پردازش متن
    processed_text = preprocess_text(request.text)
    
    # پیش‌بینی دسته
    prediction = model.predict([processed_text])[0]
    
    return {
        "original_text": request.text,
        "category": label_map.get(prediction, "نامشخص"),
        "original_label": prediction,
        "confidence": float(model.predict_proba([processed_text]).max())
    }

@app.get("/health")
def health_check():
    """بررسی سلامت سرویس"""
    return {"status": "ok", "model_loaded": model is not None}