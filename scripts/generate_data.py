from g4f.client import Client
import pandas as pd
import time
import random
import json
import os

client = Client()

# دسته‌بندی‌ها
categories = [
    "support_complaint",  # پشتیبانی/شکایت مشتری
    "sales_inquiry",      # درخواست فروش/استعلام قیمت
    "collaboration",      # همکاری/پیشنهاد شراکت
    "spam_ad"            # هرزنامه/تبلیغات
]

# تمپلیت‌های پیشنهادی برای هر دسته
templates = {
    categories[0]: [
        "شکایت در مورد {محصول} که خراب شده است",
        "پشتیبانی برای مشکل {نرم‌افزار} نیاز دارم",
        "خدمات پس از فروش {شرکت} پاسخگو نیست"
    ],
    categories[1]: [
        "قیمت {محصول} را می‌خواستم بدانم",
        "برای خرید {خدمت} استعلام قیمت می‌خواهم",
        "لیست قیمت‌های به‌روز {دسته‌بندی}"
    ],
    categories[2]: [
        "پیشنهاد همکاری در زمینه {حوزه} دارم",
        "به دنبال شریک برای {کسب‌وکار} هستم",
        "پروپوزال مشارکت برای {پروژه}"
    ],
    categories[3]: [
        "فروش ویژه {محصول} با 50% تخفیف!",
        "شانس برنده شدن {جایزه} را از دست ندهید!",
        "تور لحظه‌آخری {مقصد} فقط امروز"
    ]
}

def generate_email(category: str) -> str:
    """تولید ایمیل مصنوعی با GPT-4.1"""
    template = random.choice(templates[category])
    prompt = (
        f"یک ایمیل واقعی و با جزئیات به زبان فارسی در دسته '{category}' بنویس. "
        f"موضوع ایمیل باید مرتبط با '{template}' باشد. "
        "ایمیل باید شامل: 1. سلام و احوالپرسی 2. بدنه اصلی 3. خداحافظی و امضا باشد."
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
            web_search=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"خطا در تولید ایمیل: {e}")
        with open("error_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{time.ctime()} - {str(e)}\n")
        return ""

# ایجاد دایرکتوری برای ذخیره داده‌ها
os.makedirs("data", exist_ok=True)

# تولید 200 ایمیل برای هر دسته
synthetic_data = []
for category in categories:
    print(f"در حال تولید ایمیل‌های دسته {category}...")
    category_emails = []
    
    for i in range(2):
        try:
            email = generate_email(category)
            if email:
                category_emails.append({
                    "text": email,
                    "label": category
                })
                print(f"text: {email}\nlabel: {category}")
                print(f"ایمیل {i+1}/200 تولید شد")
            else:
                print(f"خطا در تولید ایمیل {i+1}/200")
        except Exception as e:
            print(f"خطای سیستمی در ایمیل {i+1}: {e}")
        
        sleep_time = random.uniform(1.0, 3.0)
        time.sleep(sleep_time)
    
    synthetic_data.extend(category_emails)
    print(f"تولید ایمیل‌های دسته {category} تکمیل شد. تعداد: {len(category_emails)} ایمیل")
    
    # ذخیره موقت با نام فایل انگلیسی
    temp_df = pd.DataFrame(synthetic_data)
    temp_filename = f"temp_{category}.csv"
    temp_df.to_csv(temp_filename, index=False, encoding='utf-8-sig')
    print(f"ذخیره موقت برای دسته {category} انجام شد")

# ذخیره نهایی داده‌ها
if synthetic_data:
    df = pd.DataFrame(synthetic_data)
    output_path = os.path.join("data", "synthetic_emails.csv")
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"داده‌ها با موفقیت ذخیره شدند. مجموع ایمیل‌ها: {len(synthetic_data)}")
else:
    print("هیچ داده‌ای برای ذخیره وجود ندارد")

# ذخیره گزارش نهایی
report = {
    "total_emails": len(synthetic_data),
    "categories": {cat: len([e for e in synthetic_data if e["label"] == cat]) for cat in categories},
    "generated_at": time.ctime()
}

with open("generation_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)