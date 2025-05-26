
import os
import shutil
from datetime import datetime
from bot.config import DB_PATH

def make_backup():
    os.makedirs("backup", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup/backup_{timestamp}.sqlite3"
    shutil.copy(DB_PATH, backup_name)
    print(f"[BACKUP] Резервная копия создана: {backup_name}")
