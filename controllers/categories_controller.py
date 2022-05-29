from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.category import *

import repositories.category_repository as category_repository

categories_blueprint = Blueprint("categories", __name__)

@categories_blueprint.route('/categories')
def categories():
    categories = category_repository.select_all()
    return render_template('/categories/index.html', categories = categories)