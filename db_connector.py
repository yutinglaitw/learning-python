'''
MySQL connector
'''
def mysql_connector(sql_command):
    import pymysql
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 db='db')

    try:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(sql_command)
            # connection.commit()
            result = cursor.fetchall()
    except:
        connection.rollback()
    finally:
        connection.close()

    return result

'''
MSSQL connector
'''
def mssql_connector(sql_command):
    import pymssql
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 database='db')

    try:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(sql_command)
            # connection.commit()
            result = cursor.fetchall()
    except:
        connection.rollback()
    finally:
        connection.close()

    return result


'''
MongoDB connector
'''
def mongodb_connector(host, port, database, collection):
    import pymongo

    client = pymongo.MongoClient(host=host, port=port)
    db = client[database]
    coll = db[collection].find()

    result = coll.find()
    # coll.find().limit(10).skip(20)

    return result
