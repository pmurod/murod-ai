import webbrowser
import os
import sys

html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "murod_ai.html")

if not os.path.exists(html_file):
    print("❌ murod_ai.html topilmadi! Fayl bir papkada bo'lishi kerak.")
    sys.exit(1)

url = "file://" + html_file
print("🤖 Murod AI ishga tushmoqda...")
print(f"📂 {html_file}")
webbrowser.open(url)
print("✅ Brauzer ochildi!")
