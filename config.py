import os
from dotenv.main import load_dotenv

load_dotenv()

# Bot setup
PREFIX = "!"
BOT_NAME = "Semikolon"
BOT_TOKEN = os.getenv("DISCORD_TOKEN", "")
