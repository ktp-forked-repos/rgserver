import web

params = {
    'host': 'localhost',
    'dbn': 'postgres',
    'db': 'robotgame',
    'user': 'robot',
    'pw': 'PASSWORD',
    'pooling': False,
}

###########################################################
# don't change below this line unless you know how it works
###########################################################

connection = None
def connect_db():
    global params
    global connection
    if connection is None:
        connection = web.database(**params)
    connection.printing = False  # False by default
    return connection

def connect_fresh_db():
    global params
    con = web.database(**params)
    con.printing = False  # False by default
    return con
