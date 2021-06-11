import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 4672811))
	API_HASH = os.environ.get("API_HASH")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1290356065))
	CAPTION = "By @AHToolsBot"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "VideoWatermark_Bot")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Mantap Watermark Adder Bot!
**How to Added Watermark to a Video?**
**Usage:** Pertama kirimin satu foto/logo lalu kirim video apa aja biar nongol watermarknya.
__Note: Gw cuma bisa ngolah 1 video dalam sekali kirim, jadi jangan di spam ngirim video!!.).__
Proccess by @mantapvids/n
Donate : https://saweria.co/mantapjozz
"""
	PROGRESS = """
Loading : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
