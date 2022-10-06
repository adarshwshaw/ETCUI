from settings import Engine
from model.models import Base
from settings import BASE_DIR
import os

if __name__ == '__main__':
    dbPath = os.path.join(BASE_DIR,"site.db")
    if not os.path.exists(dbPath):
        print("creating the database")
        Base.metadata.create_all(Engine)
    else:
        print("database already exist")
