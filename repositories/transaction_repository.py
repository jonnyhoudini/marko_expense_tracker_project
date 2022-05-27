from db.run_sql import run_sql

from models.transaction import *
from models.payee import *
from models.category import *

import repositories.category_repository as category_repository
import repositories.payee_repository as payee_repository

# CREATE

def save(transaction):
    sql = "INSERT INTO transactions (description, amount, date, submitted, payee_id, category_id) VALUES (?, ?, ?, ?, ?, ?) RETURNING *"
    values = [transaction.description, transaction.amount, transaction.date, transaction.submitted, transaction.payee.id, transaction.category.id]
    results = run_sql(sql, values)

    id = results[0]['id']
    transaction.id = id
    return transaction

# READ

def select_all():
    transactions=[]

    sql = "SELECT * from transactions"
    results = run_sql(sql)

    for row in results:
        payee = payee_repository.select(row['payee_id'])
        category = category_repository.select(row['category_id'])
        transaction = Transaction(row['description'], row['amount'], payee, row['date'], category, row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None

    sql = "SELECT * FROM transactions WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        payee = payee_repository.select(result['payee_id'])
        category = category_repository.select(result['category_id'])
        transaction = Transaction(result['description'], result['amount'], payee, result['date'], category, result['id'])
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (description, amount, date, submitted, payee_id, category_id) = (?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [transaction.description, transaction.amount, transaction.date, transaction.submitted, transaction.payee.id, transaction.category.id, transaction.id]
    run_sql(sql, values)