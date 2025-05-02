import pyfiglet
from termcolor import colored
import requests
import json
import random
import string
import time
import uuid
import os
import sys

def generate_unique_ids():
    """توليد معرفات فريدة للتثبيت (لأغراض اختبارية)."""
    timestamp = int(time.time() * 1000)
    random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    unique_uuid = uuid.uuid4()
    return timestamp, random_id, unique_uuid

def send_request(url, headers, payload):
    """إرسال طلب مع التعامل مع الأخطاء."""
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # يرفع استثناء إذا كانت هناك أخطاء HTTP
        return response.json().get("status") == "ok"
    except Exception as e:
        print(colored(f"Error: {e}", "red"))
        return False

def main():
    # إعدادات آمنة
    MAX_ATTEMPTS = 1  # ⚠️ لا تزيد هذا الرقم!
    TEST_NUMBER = "+1234567890"  # ⚠️ استبدلها برقمك الخاص فقط!

    # التحقق من البيئة الآمنة
    if "github" in os.getenv("HOME", ""):
        print(colored("Error: Not allowed on GitHub Actions!", "red"))
        return

    # واجهة المستخدم
    ascii_art = pyfiglet.figlet_format("TEST MODE")
    print(colored(ascii_art, "cyan"))
    print(colored("FOR EDUCATIONAL USE ONLY", "yellow"))

    # إعداد الطلبات
    headers = {
        'User-Agent': 'Test-Client/1.0',
        'Content-Type': 'application/json'
    }

    # بيانات الاختبار الآمن
    timestamp, android_id, device_uuid = generate_unique_ids()
    payload = {
        "android_id": android_id,
        "app_version": "1.0",
        "event": "test",
        "os": "linux",
        "ts": timestamp,
        "uuid": str(device_uuid),
        "phone": TEST_NUMBER  # ⚠️ يستخدم الرقم الثابت فقط
    }

    # إرسال طلب واحد (للتجربة الآمنة)
    if send_request("https://api.example.com/test_endpoint", headers, payload):
        print(colored("Test request sent (SIMULATION ONLY)", "green"))
    else:
        print(colored("Test failed (SIMULATION)", "red"))

if __name__ == "__main__":
    main()
