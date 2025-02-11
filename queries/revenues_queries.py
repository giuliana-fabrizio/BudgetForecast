from queries.db_connexion import *

def getRevenue(id):
    db = get_db()
    return db.execute('select * from revenue where id = ?', [id]).fetchone()

def getRevenues():
    db = get_db()
    return db.execute('select * from revenue;').fetchall()

def insertRevenue(name, amount, start_at, stop_at, id_customer):
    db = get_db()
    db.execute(
        'insert into revenue(name, amount, start_at, stop_at, id_customer)\
        values(?, ?, ?, ?, ?);',
        [name, amount, start_at, stop_at, id_customer]
    )
    return db.commit()

def updateRevenue(name, amount, stop_at, id):
    db = get_db()
    db.execute(
        'update revenue set name = ?, amount = ?, stop_at = ? where id = ?;',
        [name, amount, stop_at, id]
    )
    return db.commit()

def deleteRevenue(id):
    db = get_db()
    db.execute('delete from revenue where id = ?;', [id])
    return db.commit()