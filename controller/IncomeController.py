from datetime import datetime
from settings import Engine,Session
from model.models import Incomes

def addIncome(income):
    '''
    :input: income
    :return: insert a income
    '''
    with Session(bind=Engine) as sess:
        sess.add(income)
        sess.commit()

def getIncome():
    '''
    :return: return sum of current month income
    '''
    current_month = datetime.now().month
    with Engine.connect() as con:
        result = con.execute(f"select sum(amt) from {Incomes.__tablename__} where STRFTIME('%m',date) == '{current_month}'").scalar()
    return result

def getAllIncome():
    with Engine.connect() as con:
        result = con.execute(f"select * from {Incomes.__tablename__} order by date desc limit 10").fetchall()
    return result

if __name__=="__main__":
    t=Incomes(amt=94000)
    addIncome(t)