import pymysql.cursors
from database import connectToDb


def getPeople():
    connection = connectToDb()

    if connection != "failed":
        result = []

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `people`;"
                cursor.execute(sql)
                result = cursor.fetchall()
        except pymysql.Error as err:
            print(err)
        finally:
            connection.close()
    else:
        result = "failed"

    return result
