from flask import Flask

from controllers.transactions_controller import transactions_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(transactions_blueprint)