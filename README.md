# سیستم طبقه‌بندی خودکار ایمیل‌ها

![Email Classification](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![ML](https://img.shields.io/badge/machine%20learning-Naive%20Bayes%7CSVM-orange)
![API](https://img.shields.io/badge/API-FastAPI-brightgreen)

این پروژه یک سیستم طبقه‌بندی خودکار ایمیل‌ها را با استفاده از تکنیک‌های یادگیری ماشین پیاده‌سازی می‌کند. سیستم قادر است ایمیل‌های دریافتی را در یکی از دسته‌های زیر طبقه‌بندی نماید:

- پشتیبانی / شکایت مشتری
- درخواست فروش / استعلام قیمت
- همکاری / پیشنهاد شراکت
- هرزنامه / تبلیغات

## فهرست مطالب

- [راه‌اندازی محلی](#راه‌اندازی-محلی)
- [ساختار پروژه](#ساختار-پروژه)
- [مراحل اجرا](#مراحل-اجرا)
- [استفاده از API](#استفاده-از-api)
- [ارزیابی مدل‌ها](#ارزیابی-مدل‌ها)
- [بهبودهای آتی](#بهبودهای-آتی)

## راه‌اندازی محلی

### پیش‌نیازها

- Python 3.9 یا بالاتر
- pip (مدیریت بسته‌های پایتون)

### نصب و راه‌اندازی

1. کلون کردن مخزن:
   ```bash
   git clone https://github.com/yourusername/email-classifier.git
   cd email-classifier
