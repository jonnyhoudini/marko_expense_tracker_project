from flask import Flask, render_template
from flask import Blueprint

from models.transaction import *
from models.category import *
from models.payee import *

import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/")
def index():
    transactions = transaction_repository.select_all()
    return render_template('index.html', transactions = transactions)