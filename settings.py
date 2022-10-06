import os
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from flask import Flask

BASE_DIR = os.path.dirname(__file__)

Engine = db.create_engine(f"sqlite:///{BASE_DIR}/site.db",echo=True)
Session = sessionmaker()

app =Flask('ETCUI')
