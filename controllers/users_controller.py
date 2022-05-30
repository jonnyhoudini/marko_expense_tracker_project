from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.user import *

import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)