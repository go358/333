import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_PATH = 'db.sqlite3'
BACKUP_PATH = 'backup/'
ADMIN_ID = int(os.getenv('ADMIN_ID'))
