from crypt import methods
from logging.config import IDENTIFIER
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.payee import *

import repositories.payee_repository as payee_repository
import repositories.transaction_repository as transaction_repository

payees_blueprint = Blueprint("payees", __name__)

@payees_blueprint.route('/payees')
def payees():
    payees = payee_repository.select_all()
    transactions = transaction_repository.select_all()
    payees_with_totals = []
    for payee in payees:
        payee.amount_of_transactions = payee.get_total_amount_of_transactions(transactions)
        payee.number_of_transactions = payee.get_total_number_of_transactions(transactions)
        payees_with_totals.append(payee)

    return render_template('payees/index.html', payees = payees_with_totals)

@payees_blueprint.route('/payees', methods=['POST'])
def create_payee():
    name = request.form['name']
    payee = Payee(name)
    payee_repository.save(payee)
    return redirect('/payees')

@payees_blueprint.route('/payees/<id>', methods=['GET'])
def show_payee(id):
    payee = payee_repository.select(id)
    return render_template('/payees/show.html', payee = payee)

@payees_blueprint.route('/payees/<id>/edit', methods=['GET'])
def edit_payee(id):
    payee = payee_repository.select(id)
    return render_template('/payees/edit.html', payee = payee)

@payees_blueprint.route('/payees/<id>', methods=['POST'])
def update_payee(id):
    name = request.form['name']
    payee = Payee(name, id)
    payee_repository.update(payee)
    return redirect('/payees')