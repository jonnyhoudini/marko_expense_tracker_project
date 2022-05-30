from db.run_sql import run_sql

from models.user import *

# CREATE

def save(user):
    sql = "INSERT INTO users (name, expenses_limit) VALUES (?, ?) RETURNING *"
    values = [user.name, user.limit]
    results = run_sql(sql, values)

    id = results[0]['id']
    user.id = id
    return user

# READ

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        
        user = User(row['name'], row['expenses_limit'], row['id'])
       
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['expenses_limit'], result['id'])
    return user

def update(user):
    sql = "UPDATE users SET (name, expenses_limit) = (?, ?) WHERE id = ?"
    values = [user.name, user.limit, user.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)



