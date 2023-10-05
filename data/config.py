import os
# from data.database import
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
GROUP_ID = -1001978690583
CHANNEL_ID = -1001986923153
CHANNEL_URL = "https://t.me/testmychannel03"
GROUP_URL = "https://t.me/+xxep96iuXxk3ZDky"
BOT_URL = "https://t.me/FreddyKbot"
ADMIN_URL = "https://t.me/AlexNoks"

# Пригласительная ссылка
VK_URL = 'Пригласительная ссылка https://t.me/+xxep96iuXxk3ZDky'
BOT_ID = 1933153305

ADMIN_ID = 1875053743
WORDS = ['реклама','яндекс','wildberries']
db = 'database.db'




# https://t.me/AlexNoks



admins_id = 1400170440


my_list = []

admins_log = [
    '@KatyaMurMur',
    'None'
]

users_id = [
    1924126688,
    993482289,
    6284449881
]

users_log = [
    'OlgaGBoss',
    'AlexNoks',
    'KatyaMurMur',
    'None'
    'FreddyKbot'
]
choose_user = dict(zip(users_log,users_id))
ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URL = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
time_bun_sec = timedelta(seconds=15)
# "id": 1875053743,
# "is_bot": false,
# "first_name": "Alexandr Igorevich",
# "last_name": "Goncharenko", "username": "AlexNoks",
# "language_code": "ru"}