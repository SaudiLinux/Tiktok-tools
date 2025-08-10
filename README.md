# أدوات تيك توك - TikTok Tools

## وصف المشروع
أداة متقدمة لاستخراج المعلومات من حسابات تيك توك (OSINT) تم تطويرها بلغة بايثون. تتيح الأداة تحليل الحسابات واستخراج البيانات الحساسة والإحصائيات بشكل شامل.

## المطور
- **الاسم:** SayerLinux
- **البريد الإلكتروني:** SayerLinux@gmail.com
- **الموقع:** https://github.com/SaudiLinux

## المميزات

### ✅ استخراج معلومات المستخدم
- اسم المستخدم الحقيقي
- اسم العرض
- السيرة الذاتية
- الموقع الجغرافي
- رابط الموقع الإلكتروني
- حالة التحقق (Verified)
- حالة الخصوصية (Private)

### ✅ الإحصائيات الكاملة
- عدد المتابعين
- عدد المتابع بهم
- إجمالي الإعجابات
- عدد الفيديوهات المنشورة
- معرف الحساب (Account ID)

### ✅ تحليل الفيديوهات
- عناوين الفيديوهات
- عدد المشاهدات
- عدد الإعجابات
- عدد التعليقات
- عدد المشاركات
- التواريخ
- الوسوم (#hashtags)
- الموسيقى المستخدمة

### ✅ حفظ النتائج
- تنسيق JSON للبيانات الكاملة
- تفسيق CSV للملخص
- إنشاء مجلد منفصل لكل تحليل
- تسمية ملفات حسب التاريخ والوقت

## المتطلبات

### المتطلبات الأساسية
- Python 3.6 أو أحدث
- pip (مدير الحزم)

### تثبيت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

## طريقة التثبيت

### 1. استنساخ المستودع
```bash
git clone https://github.com/SaudiLinux/TikTok-Tools.git
cd TikTok-Tools
```

### 2. تثبيت المتطلبات
```bash
pip install requests beautifulsoup4 lxml colorama urllib3
```
أو
```bash
pip install -r requirements.txt
```

### 3. تشغيل الأداة
```bash
python tiktok-tools.py
```

## طريقة الاستخدام

### الطريقة 1: تشغيل تفاعلي
```bash
python tiktok-tools.py
```
ثم أدخل اسم المستخدم أو الرابط عند الطلب.

### الطريقة 2: استخدام معاملات الأوامر
```bash
# تحليل مستخدم محدد
python tiktok-tools.py username

# تحليل من رابط
python tiktok-tools.py https://tiktok.com/@username

# تحديد عدد الفيديوهات
python tiktok-tools.py username --videos 20

# تحديد مجلد الإخراج
python tiktok-tools.py username --output ./results
```

### أمثلة على الاستخدام
```bash
# تحليل حساب محدد
python tiktok-tools.py @example_user

# تحليل من رابط كامل
python tiktok-tools.py https://www.tiktok.com/@example_user

# تحليل 15 فيديو
python tiktok-tools.py example_user --videos 15
```

## بنية المجلدات الناتجة

عند تشغيل الأداة، يتم إنشاء مجلد جديد يحتوي على:

```
tiktok_username_YYYYMMDD_HHMMSS/
├── username_info.json     # معلومات المستخدم الكاملة
├── username_videos.json   # معلومات الفيديوهات
└── username_summary.csv   # ملخص CSV
```

## تنسيق البيانات

### ملف JSON لمعلومات المستخدم
```json
{
    "username": "example_user",
    "display_name": "اسم العرض",
    "followers": 1000000,
    "following": 500,
    "likes": 50000000,
    "videos_count": 150,
    "bio": "السيرة الذاتية...",
    "profile_picture": "https://...",
    "verified": true,
    "private": false,
    "location": "السعودية",
    "website": "https://example.com",
    "account_id": "123456789"
}
```

### ملف JSON للفيديوهات
```json
[
    {
        "id": "video_1",
        "description": "وصف الفيديو...",
        "likes": 100000,
        "comments": 5000,
        "shares": 2000,
        "views": 1000000,
        "upload_date": "2024-01-15",
        "hashtags": ["#trending", "#fyp"],
        "video_url": "https://tiktok.com/..."
    }
]
```

## ملاحظات مهمة

### ⚠️ تحذيرات
- هذه الأداة للأغراض التعليمية والبحثية فقط
- لا تستخدم لأغراض ضارة أو انتهاك الخصوصية
- الالتزام بشروط استخدام تيك توك
- قد تتطلب بعض الميزات تحديثات بسبب تغييرات في واجهة تيك توك

### 🔒 الأمان
- لا تقم بتخزين كلمات المرور أو معلومات حساسة
- استخدم VPN عند الحاجة
- احترم خصوصية الآخرين

## استكشاف الأخطاء

### مشاكل شائعة

#### خطأ: ModuleNotFoundError
```bash
# حل المشكلة
pip install requests beautifulsoup4 lxml colorama urllib3
```

#### خطأ: Connection Error
- تحقق من اتصال الإنترنت
- جرب استخدام VPN
- تأكد من عدم حجب تيك توك

#### خطأ: User Not Found
- تأكد من صحة اسم المستخدم
- تأكد من أن الحساب عام (غير خاص)
- جرب مع اسم مستخدم مختلف

## التحديثات

### الإصدارات المستقبلية
- دعم تحليل الوسوم (#hashtags)
- تحليل التعليقات
- استخراج المتابعين
- واجهة ويب
- دعم اللغات المتعددة

## المساهمة

نرحب بالمساهمات! يرجى:
1. عمل Fork للمشروع
2. إنشاء Branch جديد
3. تقديم تغييراتك
4. إرسال Pull Request

## الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الشخصي والتعليمي.

## الاتصال

لأي استفسارات أو اقتراحات:
- البريد الإلكتروني: SayerLinux@gmail.com
- GitHub: https://github.com/SaudiLinux

---

**ملاحظة:** هذه الأداة للأغراض التعليمية فقط. استخدمها بمسؤولية واحترم خصوصية الآخرين.