
import shutil

def backup_db():
    shutil.copy('finance.db', 'backup_finance.db')

def restore_db():
    shutil.copy('backup_finance.db', 'finance.db')
