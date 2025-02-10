from queries.db_connexion import *

def getRevenues():
    db = get_db()
    return db.execute('select * from revenue;').fetchall()

def insertRevenue(name, amount, created_at, updated_at, id_customer):
    db = get_db()
    db.execute(
        'insert into revenue(name, amount, created_at, updated_at, id_customer)\
        values(?, ?, ?, ?, ?);',
        [name, amount, created_at, updated_at, id_customer]
    )
    return db.commit()