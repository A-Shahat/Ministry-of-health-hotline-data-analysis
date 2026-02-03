"""
=====================================================================
MINISTRY HOTLINE DATA - TRANSLATION & ANONYMIZATION SCRIPT
=====================================================================

Purpose:
- Anonymize caller names and phone numbers
- Drop empty columns
- Translate Arabic columns to English
- Prepare data for analysis

Dataset: ~48,000 hotline calls from Egyptian Ministry of Health
Author: Ahmed El-Shahat
Date: February 2025

=====================================================================
"""

import pandas as pd
import numpy as np
import hashlib
import time
from datetime import datetime
from deep_translator import GoogleTranslator

print("=" * 70)
print("MINISTRY HOTLINE DATA PROCESSING")
print("=" * 70)

print("\n[1/6] Loading data...")
df = pd.read_excel('hotline_data_arabic.xlsx')
print(f"✓ Loaded {len(df):,} rows and {len(df.columns)} columns")

print("\n[2/6] Anonymizing caller names and phone numbers...")
CALLER_NAME_COL = 'اسم المتصل'
PHONE_COL = 'رقم التليفون'

def anonymize(value):
    if pd.isna(value):
        return 'Unknown'
    hash_obj = hashlib.md5(str(value).encode('utf-8'))
    return f"CALLER_{hash_obj.hexdigest()[:8].upper()}"

if CALLER_NAME_COL in df.columns:
    original_count = df[CALLER_NAME_COL].nunique()
    df[CALLER_NAME_COL] = df[CALLER_NAME_COL].apply(anonymize)
    print(f"✓ Anonymized {original_count:,} unique caller names")
else:
    print(f"⚠ Column '{CALLER_NAME_COL}' not found")

if PHONE_COL in df.columns:
    original_count = df[PHONE_COL].nunique()
    df[PHONE_COL] = df[PHONE_COL].apply(anonymize)
    print(f"✓ Anonymized {original_count:,} unique phone numbers")
else:
    print(f"⚠ Column '{PHONE_COL}' not found")

print("\n[3/6] Removing empty / high-null columns...")
empty_columns = df.columns[df.isnull().all()].tolist()
df.drop(columns=empty_columns, inplace=True)

high_null_cols = [
    col for col in df.columns
    if (df[col].isnull().mean() * 100) > 95
]
df.drop(columns=high_null_cols, inplace=True)

print(f"✓ Remaining columns: {len(df.columns)}")

print("\n[4/6] Translating column names...")
column_translation = {
    'طابع زمني': 'timestamp',
    'اسم المتصل': 'caller_id',
    'رقم التليفون': 'phone_id',
    'موضوع الشكوي': 'complaint_subject',
    'جهة الشكوي': 'complaint_entity',
    'موقف الشكوي': 'complaint_status',
    'الموظف': 'employee',
    'عنوان البريد الإلكتروني': 'email',
    'تفاصيل المكالمة': 'call_details',
    'متابعة المكالمة': 'call_followup',
    'هل مكالمة طوارئ؟': 'is_emergency',
    'نوع المستشفى': 'hospital_type',
    'الجهة المسئولة (طوارئ)': 'emergency_responsible_entity',
    'اسم المستشفى': 'hospital_name',
    'المحافظة (طوارئ)': 'governorate_emergency',
    'التشخيص': 'diagnosis',
    'عنوان المستشفى (طوارئ)': 'hospital_address_emergency',
    'حالة المراجعة': 'review_status',
    'الموظف المتابع': 'followup_employee',
    'تاريخ المراجعة': 'review_date',
    'ملاحظات المتابعة النهائية': 'final_followup_notes'
}

df.rename(columns=column_translation, inplace=True)

print("\n[5/6] Translating categorical values...")
translator = GoogleTranslator(source='ar', target='en')

def translate_value(text, retry=3):
    if pd.isna(text) or text == '' or str(text).startswith('CALLER_'):
        return text

    for _ in range(retry):
        try:
            time.sleep(0.1)
            return translator.translate(str(text))
        except Exception:
            time.sleep(1)

    return text

for col in df.select_dtypes(include='object'):
    if col in ['caller_id', 'phone_id', 'timestamp', 'review_date']:
        continue

    if df[col].nunique() < 100:
        mapping = {
            val: translate_value(val)
            for val in df[col].dropna().unique()
        }
        df[f"{col}_en"] = df[col].map(mapping)
        print(f"✓ Translated '{col}'")

print("\n[6/6] Saving output...")
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'ministry_hotline_processed_{timestamp}.xlsx'
df.to_excel(output_file, index=False)

print(f"✓ Saved: {output_file}")
print("\nPROCESSING COMPLETE")

