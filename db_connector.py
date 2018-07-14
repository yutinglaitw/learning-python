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
            connection.commit()
            result = cursor.fetchall()
    except:
        connection.rollback()
    finally:
        connection.close()

    return result

