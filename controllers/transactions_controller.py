from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import *
from models.category import *
from models.payee import *

import repositories.transaction_repository as transaction_repository
import repositories.category_repository as category_repository
import repositories.payee_repository as payee_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return render_template('transactions/transactions.html', transactions = transactions, total = total)

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    payees = payee_repository.select_all()
    categories = category_repository.select_all()
    return render_template("transactions/new.html", payees = payees, categories = categories)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    description = request.form['description']
    amount = request.form['amount']
    payee_id = request.form['payee_id']
    date = request.form['date']
    category_id = request.form['category_id']
    payee = payee_repository.select(payee_id)
    category = category_repository.select(category_id)
    transaction = Transaction(description, amount, payee, date, category)
    transaction_repository.save(transaction)
    return redirect('/transactions')

