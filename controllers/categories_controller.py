from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.category import *

import repositories.category_repository as category_repository
import repositories.transaction_repository as transaction_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route('/categories')
def categories():
    categories = category_repository.select_all()
    transactions = transaction_repository.select_all()
    categories_with_totals = []
    for category in categories:
        category.amount_of_transactions = category.get_total_amount_of_transactions(transactions)
        category.number_of_transactions = category.get_total_number_of_transactions(transactions)
        categories_with_totals.append(category)
    return render_template('/categories/index.html', categories = categories_with_totals)

@categories_blueprint.route('/categories', methods=['POST'])
def create_category():
    name = request.form['name']
    category = Category(name)
    category_repository.save(category)
    return redirect('/categories')

@categories_blueprint.route('/categories/<id>', methods=['GET'])
def show_category(id):
    category = category_repository.select(id)
    return render_template('/categories/show.html', category = category)

@categories_blueprint.route('/categories/<id>/edit', methods=['GET'])
def edit_category(id):
    category = category_repository.select(id)
    return render_template('/categories/edit.html', category = category)

@categories_blueprint.route('/categories/<id>', methods=['POST'])
def update_category(id):
    name = request.form['name']
    category = Category(name, id)
    category_repository.update(category)
    return redirect('/categories')