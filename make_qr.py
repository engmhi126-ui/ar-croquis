# -*- coding: utf-8 -*-
"""توليد QR للكروكي التفاعلي — غيّر URL بعد الرفع على GitHub Pages"""
import sys, qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else "https://USERNAME.github.io/ar-croquis/"
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=12, border=3)
qr.add_data(url)
img = qr.make_image(fill_color="#1a5276", back_color="white")
img.save("/home/claude/ar-croquis/qr.png")
print("QR →", url)
