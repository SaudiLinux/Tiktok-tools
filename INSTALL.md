# دليل التثبيت السريع - TikTok Tools

## 🚀 التثبيت السريع (ويندوز)

### الخطوة 1: تحميل الملفات
1. قم بتحميل جميع الملفات إلى مجلد واحد
2. افتح Command Prompt أو PowerShell
3. انتقل إلى المجلد الذي يحتوي على الملفات

### الخطوة 2: تثبيت بايثون
إذا لم يكن بايثون مثبتًا:
1. انتقل إلى https://python.org
2. حمل Python 3.8 أو أحدث
3. تأكد من تحديد "Add Python to PATH"

### الخطوة 3: تثبيت المكتبات
في Command Prompt:
```cmd
pip install requests beautifulsoup4 lxml colorama urllib3
```

أو استخدام ملف المتطلبات:
```cmd
pip install -r requirements.txt
```

### الخطوة 4: تشغيل الأداة
#### الطريقة 1: استخدام ملف التشغيل التلقائي
انقر مرتين على `run.bat`

#### الطريقة 2: استخدام سطر الأوامر
```cmd
python tiktok-tools.py
```

#### الطريقة 3: مع مستخدم محدد
```cmd
python tiktok-tools.py username_المستهدف
```

## 🐧 التثبيت على لينكس

### الخطوة 1: تثبيت بايثون والمكتبات
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests beautifulsoup4 lxml colorama urllib3
```

### الخطوة 2: تشغيل الأداة
```bash
chmod +x tiktok-tools.py
python3 tiktok-tools.py
```

## 🍎 التثبيت على macOS

### الخطوة 1: تثبيت بايثون
```bash
brew install python3
pip3 install requests beautifulsoup4 lxml colorama urllib3
```

### الخطوة 2: تشغيل الأداة
```bash
python3 tiktok-tools.py
```

## ✅ التحقق من التثبيت

### تشغيل اختبار سريع
```cmd
python tiktok-tools.py --help
```

### أو استخدام ملف التشغيل التلقائي
انقر على `run.bat` (ويندوز فقط)

## 📁 بنية المجلد بعد التثبيت
```
Tiktok-tools/
├── tiktok-tools.py          # الملف الرئيسي
├── requirements.txt         # متطلبات المكتبات
├── README.md               # دليل الاستخدام
├── INSTALL.md             # هذا الملف
├── run.bat                # ملف تشغيل ويندوز
├── config.py              # إعدادات الأداة
└── example_usage.py       # مثال الاستخدام
```

## 🛠️ استكشاف الأخطاء الشائعة

### خطأ: "python is not recognized"
**الحل:**
1. أضف بايثون إلى PATH
2. أو استخدم `py` بدلاً من `python`

### خطأ: "pip is not recognized"
**الحل:**
```cmd
python -m pip install requests beautifulsoup4 lxml colorama urllib3
```

### خطأ: "ModuleNotFoundError"
**الحل:**
```cmd
pip install requests beautifulsoup4 lxml colorama urllib3
```

### خطأ: "Permission denied"
**الحل (لينكس/ماك):**
```bash
chmod +x tiktok-tools.py
```

## 📞 الدعم الفني

إذا واجهت مشاكل:
1. تأكد من اتصال الإنترنت
2. تحقق من صحة اسم المستخدم
3. تأكد أن الحساب عام (غير خاص)
4. تواصل عبر: SayerLinux@gmail.com

## 🎯 البدء السريع

### بعد التثبيت مباشرة:
1. افتح Command Prompt
2. انتقل إلى مجلد الأداة
3. اكتب: `python tiktok-tools.py`
4. أدخل اسم المستخدم عند الطلب
5. انتظر النتائج!

## 📝 ملاحظات مهمة

- الأداة تعمل مع الحسابات العامة فقط
- تأكد من اتصال إنترنت مستقر
- بعض الميزات قد تختلف حسب تحديثات تيك توك
- استخدم بمسؤولية واحترم خصوصية الآخرين

---

**مطور الأداة:** SayerLinux
**البريد الإلكتروني:** SayerLinux@gmail.com
**GitHub:** https://github.com/SaudiLinux