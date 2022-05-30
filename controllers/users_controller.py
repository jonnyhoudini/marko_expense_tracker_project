from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.user import *

import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route('/users', methods=['GET'])
def users():
    users = user_repository.select_all()
    user = users[0]
    return render_template('/users/index.html', user = user)

@users_blueprint.route("/users/<id>", methods = ['GET'])
def show_user(id):
    user = user_repository.select(id)
    return render_template('users/show.html', user = user)

@users_blueprint.route('/users/<id>/edit', methods=['GET'])
def edit_user(id):
    user = user_repository.select(id)
    return render_template('users/edit.html', user = user)

@users_blueprint.route('/users/<id>', methods=['POST'])
def update_user(id):
    user = user_repository.select(id)
    name = user.name
    limit = request.form['limit']
    user = User(name, limit, id)
    user_repository.update(user)
    return redirect('/transactions')

