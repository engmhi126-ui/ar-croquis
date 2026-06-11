# الكروكي التفاعلي AR — المطري كونسلت

## النشر في 3 دقائق (GitHub Pages)
1. أنشئ مستودع جديد باسم `ar-croquis`
2. ارفع: `index.html` + `parcel.glb`
3. Settings → Pages → Branch: main → Save
4. الرابط: `https://USERNAME.github.io/ar-croquis/`
5. أعد توليد QR بالرابط الفعلي:
   `python3 make_qr.py https://USERNAME.github.io/ar-croquis/`
6. ألصق `qr.png` على الكروكي المعتمد (DOCX) أو اطبعه كملصق

## أو على VPS (bmeng.tech)
انسخ المجلد لأي مسار يخدمه Traefik كملفات ثابتة — مثلاً `ar.bmeng.tech`.

## دعم AR حسب الجهاز
- **Android**: يعمل فوراً (Scene Viewer من ملف GLB)
- **iPhone**: العارض ثلاثي الأبعاد يعمل، لكن وضع AR الكامل يحتاج ملف USDZ.
  التحويل: Reality Converter (مجاني على Mac) أو موقع products.aspose.app/3d/conversion/glb-to-usdz
  ثم ضع `parcel.usdz` بجانب GLB — الصفحة تشير له مسبقاً.

## لأرض حقيقية
عدّل `build_glb.py`: استبدل المستطيل بإحداثيات UTM الفعلية (نفس مصفوفات
مهارة land-division) وأنصبة الورثة، ثم أعد التنفيذ.
