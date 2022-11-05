from sqlalchemy.orm import declarative_base
import sqlalchemy as db
from datetime import datetime
from settings import Session,Engine

Base = declarative_base()

class Transactions(Base):
    __tablename__ = 'Transactions'

    Categories = ['	Misc','Resturant','paan','Groceries','food delivery','Entertainment','Rent']
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    categore = db.Column(db.String(16),nullable=False,default="Unidentified")
    desc = db.Column(db.String(32),nullable=False)
    amt = db.Column(db.Float(),nullable=False)
    created_dt = db.Column(db.DateTime(),default=datetime.now())

    def __repr__(self):
        return f"<Transaction categore={self.categore} desc={self.desc} amt={self.amt} created_dt={self.created_dt}"

class  Incomes(Base):
    __tablename__= 'Incomes'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    date = db.Column(db.Date(),nullable=False,default=datetime.now)
    amt = db.Column(db.Float(),nullable=False)

    def __repr__(self):
        return f'<Income date={self.date} amt={self.amt}'


if __name__ == '__main__':
    t = Transactions(categore='c3',desc='d4',amt=55.0)
    local_session = Session(bind=Engine)
    local_session.add(t)
    local_session.commit()