# app/model_loader.py
import joblib
import os
from sklearn.pipeline import Pipeline
from typing import Tuple

def load_model(model_path: str = "models/svm_model.joblib") -> Tuple[Pipeline, dict]:
    """
    مدل آموزش دیده و نقشه برچسب‌ها را بارگیری می‌کند
    
    پارامترها:
        model_path (str): مسیر فایل مدل
    
    برمی‌گرداند:
        tuple: (مدل بارگیری شده، نقشه برچسب‌ها)
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"فایل مدل در مسیر {model_path} یافت نشد")
    
    model = joblib.load(model_path)
    
    # نقشه برچسب‌ها به فارسی
    label_map = {
        "support_complaint": "پشتیبانی/شکایت",
        "sales_inquiry": "فروش/استعلام",
        "collaboration": "همکاری/شراکت",
        "spam_ad": "هرزنامه/تبلیغات"
    }
    
    return model, label_map