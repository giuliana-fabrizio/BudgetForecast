from queries.db_connexion import *

def getCategory(id):
    db = get_db()
    return db.execute('select * from category where id = ?', [id]).fetchone()

def getCategories():
    db = get_db()
    return db.execute('select * from category;').fetchall()

def insertCategory(name, forecast, created_at, updated_at, id_customer):
    db = get_db()
    db.execute(
        'insert into category(name, forecast, created_at, updated_at, id_customer)\
        values(?, ?, ?, ?, ?);',
        [name, forecast, created_at, updated_at, id_customer]
    )
    return db.commit()

def updateCategory(name, forecast, updated_at, id):
    db = get_db()
    db.execute(
        'update category set name = ?, forecast = ?, updated_at = ? where id = ?;',
        [name, forecast, updated_at, id]
    )
    return db.commit()

def deleteCategory(id):
    db = get_db()
    db.execute('delete from category where id = ?;', [id])
    return db.commit()