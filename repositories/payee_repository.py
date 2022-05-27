from db.run_sql import run_sql

from models.payee import Payee

def save(payee):
    sql = "INSERT INTO payees (name) VALUES (?) RETURNING *"
    values = [payee.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    payee.id = id
    return payee