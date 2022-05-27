from db.run_sql import run_sql

from models.payee import Payee

# CREATE 
def save(payee):
    sql = "INSERT INTO payees (name) VALUES (?) RETURNING *"
    values = [payee.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    payee.id = id
    return payee

# READ
def select_all():
    payees = []

    sql = "SELECT * FROM payees"
    results = run_sql(sql)

    for row in results:
        payee = Payee(row['name'], row['id'])
        payees.append(payee)
    return payees

def select(id):
    payee = None
    sql = "SELECT * FROM payees WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        payee = Payee(result['name'], result['id'])
    return payee

# UPDATE

def update(payee):
    sql = "UPDATE payees SET (name) = (?) WHERE id = ?"
    values = [payee.name, payee.id]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE FROM payees"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM payees WHERE id = ?"
    values = [id]
    run_sql(sql, values)
