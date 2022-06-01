from flask import Flask, render_template

from controllers.transactions_controller import transactions_blueprint
from controllers.payees_controller import payees_blueprint
from controllers.categories_controller import categories_blueprint
from controllers.users_controller import users_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(payees_blueprint)
app.register_blueprint(categories_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')