from db.run_sql import run_sql

from models.category import *

# CREATE

def save(category):
    sql = "INSERT INTO categories (name) VALUES (?) RETURNING *"
    values = [category.name]
    results = run_sql(sql, values)

    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categories = []

    sql = "SELECT * FROM categories"
    results = run_sql(sql)

    for row in results:
        category = Category(row['name'], row['id'])
        categories.append(category)
    return categories

def select(id):
    category = None

    sql = "SELECT * FROM categories WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        category = Category(result['name'], result['id'])
    return category

def delete_all():
    sql = "DELETE FROM categories"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM categories WHERE id = ?"
    values = [id]
    run_sql(sql, values)

# UPDATE 

def update(category):
    sql = "UPDATE categories SET (name) = (?) WHERE id = ?"
    values = [category.name, category.id]
    run_sql(sql, values)

