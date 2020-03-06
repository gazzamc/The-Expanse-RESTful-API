import pymysql.cursors
import os


def connect_to_db():
    '''
    Makes a connection with database, returns string if failed.

            Parameters:
                    None

            Returns:
                str: returns 'no connection' if failed
    '''
    # Get credentials
    uri = os.environ.get('CLEARDB_DATABASE_URL')

    if uri is not None:
        host = uri.split('@')[1].split('/')[0]
        user = uri.split('://')[1].split(':')[0]
        password = uri.split(':')[2].split('@')[0]
        db_name = uri.split('/')[3].split('?')[0]

        # Connect to the database
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db=db_name,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    else:
        connection = "no connection"

    return connection
