# train.py
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from hazm import Normalizer
import re

os.makedirs("models", exist_ok=True)

normalizer = Normalizer()

def preprocess_text(text: str) -> str:
    text = normalizer.normalize(text)
    text = re.sub(r'[^\w\s]', '', text)  
    return text

print("در حال بارگیری داده‌ها...")
df = pd.read_csv("data/synthetic_emails.csv")

print("در حال پیش‌پردازش داده‌ها...")
df['processed_text'] = df['text'].apply(preprocess_text)

X = df['processed_text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("در حال آموزش مدل SVM...")
svm_model = make_pipeline(
    TfidfVectorizer(),
    SVC(kernel='linear', probability=True)
)
svm_model.fit(X_train, y_train)

print("در حال آموزش مدل Naive Bayes...")
nb_model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)
nb_model.fit(X_train, y_train)

joblib.dump(svm_model, 'models/svm_model.joblib')
joblib.dump(nb_model, 'models/nb_model.joblib')
print("مدل‌ها با موفقیت ذخیره شدند")

print("\nارزیابی مدل SVM:")
svm_preds = svm_model.predict(X_test)
print(classification_report(y_test, svm_preds))

print("\nارزیابی مدل Naive Bayes:")
nb_preds = nb_model.predict(X_test)
print(classification_report(y_test, nb_preds))

report = {
    "svm_report": classification_report(y_test, svm_preds, output_dict=True),
    "nb_report": classification_report(y_test, nb_preds, output_dict=True)
}

pd.DataFrame(report).to_csv("models/model_evaluation.csv", index=True)
print("گزارش ارزیابی در models/model_evaluation.csv ذخیره شد")