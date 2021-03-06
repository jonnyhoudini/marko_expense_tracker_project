from logging.config import IDENTIFIER
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import *
from models.category import *
from models.payee import *
from models.user import *

import repositories.transaction_repository as transaction_repository
import repositories.category_repository as category_repository
import repositories.payee_repository as payee_repository
import repositories.user_repository as user_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    users = user_repository.select_all()
    limit = users[0].limit
    total = 0
    for transaction in transactions:
        total += transaction.amount
    return render_template('transactions/transactions.html', transactions = transactions, total = total, limit = limit)

# NEW

@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    payees = payee_repository.select_all()
    categories = category_repository.select_all()
    return render_template("transactions/new.html", payees = payees, categories = categories)

# CREATE

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

# SHOW

@transactions_blueprint.route("/transactions/<id>", methods = ['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show.html', transaction = transaction)

# EDIT

@transactions_blueprint.route('/transactions/<id>/edit', methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    payees = payee_repository.select_all()
    categories = category_repository.select_all()
    return render_template('transactions/edit.html', transaction = transaction, payees = payees, categories = categories)

# UPDATE

@transactions_blueprint.route('/transactions/<id>', methods=['POST'])
def update_transaction(id):
    description = request.form['description']
    amount = request.form['amount']
    payee_id = request.form['payee_id']
    date = request.form['date']
    category_id = request.form['category_id']
    payee = payee_repository.select(payee_id)
    category = category_repository.select(category_id)
    transaction = Transaction(description, amount, payee, date, category, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

@transactions_blueprint.route('/transactions/<id>/delete', methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
