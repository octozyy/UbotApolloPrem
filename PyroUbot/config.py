import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "850"))

DEVS = list(map(int, os.getenv("DEVS", "7504137934").split()))

API_ID = int(os.getenv("API_ID", "24721040"))

API_HASH = os.getenv("API_HASH", "62acb8a14d937834bcf2fc8e45571e2f")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8252544403:AAGOCB1GMjLt9LQIeqomicN16vPbUdR7cwc")

OWNER_ID = int(os.getenv("OWNER_ID", "7504137934"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://khusususer:whoadmin98@alluserbot1.iws9dgj.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
