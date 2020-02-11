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


def addPeople(name, status, gender, desc):
    connection = connectToDb()

    if connection != "failed":
        try:
            with connection.cursor() as cursor:
                sql = "\
                \
                INSERT INTO `people` (`name`, `status`, `gender`, `desc`) VALUES(%s, %s, %s, %s);"
                cursor.execute(sql, (name, status, gender, desc))
                connection.commit()
        except pymysql.Error as err:
            print(err)
        finally:
            connection.close()

    return connection
