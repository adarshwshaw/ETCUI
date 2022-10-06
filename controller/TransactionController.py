from model.models import Transactions
from datetime import datetime
from settings import Engine,Session
from controller.utils import util_row_to_dict

months=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]

# insert
def addTransaction(transaction):
    '''
    :input: Transactions
    :return: insert a transaction
    '''
    sess = Session(bind=Engine)
    sess.add(transaction)
    sess.commit()

# get
def getTotalExpense():
    '''
    :return: get total expense for the month
    '''
    current_month = datetime.now().month
    with Engine.connect() as con:
        result = con.execute(f"select sum(amt) from {Transactions.__tablename__} where STRFTIME('%m',created_dt) == '{current_month}'").scalar()
    return result,months[current_month-1]

#get
def getExpensePerCategore():
    '''
    :return: get sum of expense per categore
    '''
    current_month = datetime.now().month
    with Engine.connect() as con:
        result = con.execute(f"select categore,sum(amt) as amt from {Transactions.__tablename__} where STRFTIME('%m',created_dt) == '{current_month}' group by categore").fetchall()
    return util_row_to_dict(result)

#get
def getExpense():
    current_month = datetime.now().month
    # with Engine.connect() as con:
    #     result = con.execute(f"select * from {Transactions.__tablename__} where STRFTIME('%m',created_dt) == '{current_month}' order by created_dt desc").fetchall()
    # return result
    return getExpenseOfMonth(current_month)

def getExpenseOfMonth(month):
    with Engine.connect() as con:
        result = con.execute(f"select * from {Transactions.__tablename__} where STRFTIME('%m',created_dt) == '{month}' order by created_dt desc").fetchall()
    return result
#put
def updateTransaction(id,setExpr):
    with Engine.connect() as con:
        con.execute(f"update {Transactions.__tablename__} set {setExpr} where id={id}")

def deleteTransaction(id):
    sess=Session(bind=Engine)
    t=sess.query(Transactions).filter(Transactions.id==id).first()
    sess.delete(t)
    sess.commit()

def getLast6monthExpense():
    with Engine.connect() as con:
        result = con.execute(f"select STRFTIME('%m',created_dt) as month,sum(amt) as amt from {Transactions.__tablename__} group by STRFTIME('%m',created_dt) order by created_dt desc").fetchall()[:6]
    result = util_row_to_dict(result)
    for i in range(len(result)):
        result[i]['month'] = months[int(result[i]['month'])-1]
    return result


if __name__=="__main__":
    # t=Transactions(categore="c2",desc="misc",amt=30)
    # addTransaction(t)
    # print(getExpensePerCategore())
    # updateTransaction(1,"amt=110")
    print(getLast6monthExpense())