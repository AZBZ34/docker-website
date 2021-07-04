def connect(connect_database):
    import pyodbc
    from . import host_info

    driver = 'ODBC Driver 17 for SQL Server'
    host = 'sql-server-db'
    print("Attempting to connect [" + driver + "]", "to [" + host + "].")

    mdf_conn = pyodbc.connect(driver=driver,
                              host=host,
                              database=connect_database,
                              user='sa',
                              password='Super_Duper_Password',
                              )
    db_cursor = mdf_conn.cursor()

    if connect_database == 'master':
        mdf_conn.autocommit = True
        return db_cursor

    return db_cursor


def init(create_database):
    db_cursor = connect("master")

    # db_query = "CREATE DATABASE [" + create_database + "];"
    db_query = """
    IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = '""" + create_database + """')
      BEGIN
        CREATE DATABASE [""" + create_database + """]
      END
    """
    print(db_query)
    db_cursor.execute(db_query)
    db_cursor.commit()

    return db_cursor


def insert(use_database, data={}):
    from datetime import datetime

    db_cursor = connect(use_database)
    table_name = str(datetime.today().strftime('%Y%m%d'))
    data['timestamp'] = str(datetime.today().strftime('%Y-%m-%d, %H:%M:%S'))

    db_query = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='""" + table_name + """' and xtype='U')
	BEGIN
        CREATE TABLE [""" + table_name + """] (
            timestamp varchar(255),
            user_ip varchar(255),
            IPv4 varchar(255),
            country_code varchar(255),
            country_name varchar(255),
            state varchar(255),
            city varchar(255),
            postal varchar(255),
            latitude varchar(255),
            longitude varchar(255)
        );
    END
    """
    print(db_query)
    db_cursor.execute(db_query)
    db_cursor.commit()

    column_names = [
        'timestamp',
        'user_ip',
        'IPv4',
        'country_code',
        'country_name',
        'state',
        'city',
        'postal',
        'latitude',
        'longitude',
    ]
    table_values = []
    for i in column_names:
        table_values.append(data[i])

    column_names = ["[" + i + "]" for i in column_names]
    table_values = ["'" + str(i) + "'" for i in table_values]
    columns_str = ",".join(column_names)
    values_str = ",".join(table_values)

    mdf_query = "INSERT INTO [" + table_name + "] (" + columns_str + ") VALUES (" + values_str + ");"
    print(mdf_query)
    db_cursor.execute(mdf_query)
    db_cursor.commit()

    return
