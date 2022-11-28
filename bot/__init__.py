import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = os.environ.get('BOT_TOKEN','5541380668:AAGH9yGr_4leFAgG35raDvAi1Q82ynMJGG0')
    APP_ID = os.environ.get('APP_ID','6534707')
    API_HASH = os.environ.get('API_HASH','4bcc61d959a9f403b2f20149cbbe627a')
    DATABASE_URL = os.environ.get('DATABASE_URL','postgres://muuiwiebyrkijb:75dc160ebe4b8c7dfc58c5856e39524e13d065c82d621fc28cb2a8d288b1ded5@ec2-54-163-34-107.compute-1.amazonaws.com:5432/dega4eu8mggpbe')
    SUDO_USERS = os.environ.get('SUDO_USERS','1430593323')
    SUPPORT_CHAT_LINK = os.environ.get('SUPPORT_CHAT_LINK','https://t.me/animecolony')
    DOWNLOAD_DIRECTORY = os.environ.get("DOWNLOAD_DIRECTORY", "./downloads/")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID",'113986320920-6j0u34egb7ptdfgsj9sucdtqpff6arf3.apps.googleusercontent.com')
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET",'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')
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)
