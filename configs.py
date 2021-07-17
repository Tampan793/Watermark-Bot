# (c) @M4SK3R1N

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "1948592559:AAHKY7jkisuJ2cc63nraZnpXQSchWCTaHq8")
	API_ID = int(os.environ.get("API_ID", "6118254"))
	API_HASH = os.environ.get("API_HASH", "7f31b2fa35dde921ddd87895b3de5500")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001523314599"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001483951867")
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "superfast")
	OWNER_ID = int(os.environ.get("OWNER_ID", "1710132981"))
	CAPTION = "By @M4SK3R"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "WMVTHBot")
	DATABASE_URL = os.environ.get("DATABASE_URL", "")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, Saya Bot Watermark Video!

**Bagaimana Cara Menggunakannya?**
**Usage:** Pertama Kirimkan JPG Image/Logo, Kemudian Kirim Video. Lebih baik tambahkan WM ke Video MP4 atau MKV.

__Note: Saya hanya dapat memproses satu video dalam satu waktu. Karena server saya adalah Heroku, kesehatan saya tidak baik. Jika Anda memiliki masalah dengan Menambahkan Tanda Air ke Video, silakan Laporkan di [Support Group](https://t.me/M4SK3R1N).__

Desgined by @M4SK3R
"""
	PROGRESS = """
Persentase : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
