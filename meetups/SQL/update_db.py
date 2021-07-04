from . import sql_connect
sql_connect.init("honey-pot")


def insert(data={}):
    sql_connect.insert("honey-pot", data)
    return
