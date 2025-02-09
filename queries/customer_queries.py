from queries.db_connexion import *

def getUserByEmail(email):
    db = get_db()
    return db.execute('select * from customer where mail like ?;', [email]).fetchone()

def addUser(firstname, name, email, password):
    db = get_db()
    db.execute(
        'insert into customer(firstname, name, mail, password) values (?, ?, ?, ?);',
        [firstname, name, email, password]
    )
    return db.commit()