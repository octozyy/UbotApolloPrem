import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "850"))

DEVS = list(map(int, os.getenv("DEVS", "1950085460").split()))

API_ID = int(os.getenv("API_ID", "20702296"))

API_HASH = os.getenv("API_HASH", "ae201c7defe82c2fe787f519849c902e")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8406231706:AAHc03JupcpuXRmhM-02f9x3tM6Ks6dppUc")

OWNER_ID = int(os.getenv("OWNER_ID", "1950085460"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ibnumuzakim7:ibnumuzakim132@ibnumuzakim.sbwnig8.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
