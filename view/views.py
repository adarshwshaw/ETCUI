import os.path

from settings import app,Engine,Session
from flask import render_template,request,redirect,url_for
from controller import TransactionController as tc,IncomeController as ic
from model.models import Transactions,Incomes

@app.route("/")
def dashboard():
    arg={}
    arg['expense'],arg['month'] = tc.getTotalExpense()
    if arg['expense'] == None:
        arg['expense']=0
    arg['income'] = ic.getIncome()
    if arg['income'] == None:
        arg['income']=0
    arg['remain']=arg['income']-arg['expense']
    piechart = tc.getExpensePerCategore()
    arg['pie_x_val']=[]
    arg['pie_y_val']=[]
    for i in piechart:
        arg['pie_x_val'].append(i['categore'])
        arg['pie_y_val'].append(i['amt'])
    barchar = tc.getLast6monthExpense()
    arg['bar_x_val']=[]
    arg['bar_y_val']=[]
    for i in barchar:
        arg['bar_x_val'].append(i['month'])
        arg['bar_y_val'].append(i['amt'])
    return render_template("Summary.html",**arg)

@app.route("/Income",methods=['GET','POST'])
def income():
    if request.method == 'POST':
        income = Incomes(amt=request.form['amount'])
        ic.addIncome(income)
        return redirect(f"/Income")
    income = ic.getAllIncome()
    return render_template("incomes.html",income=income)

@app.route("/Expense/<year>/<month>",methods=['GET','POST'])
@app.route("/Expense",methods=['GET','POST'])
def expense(year=None,month=None):
    if request.method=='POST':
        if request.form['type']== 'insert':
            t=Transactions(categore=request.form['categore'],desc=request.form['desc'],amt=request.form['amount'])
            tc.addTransaction(t)
        elif request.form['type']== 'update':
            if request.form['setExpr'].upper() == 'DELETE':
                tc.deleteTransaction(request.form['id'])
            else:
                tc.updateTransaction(request.form['id'],request.form['setExpr'])
        elif request.form['type']=='filter':
            month=request.form['month']
            return redirect(f"/Expense/{month[0]}/{month[1]}")
        return redirect("/Expense")
    else:
        if month==None:
            result = tc.getExpense()
        else:
            result = tc.getExpenseOfMonth(year,month)
        return render_template("view.html",transactions=result, categore = Transactions.Categories)


