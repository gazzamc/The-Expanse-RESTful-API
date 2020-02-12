import pymysql.cursors
from database import connect_to_db


def get_people():
    connection = connect_to_db()

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


def add_people(name, status, gender, desc):
    connection = connect_to_db()

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


def delete_people(id):
    connection = connect_to_db()

    if connection != "failed":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `people` WHERE `id` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                if len(result) != 0:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        DELETE FROM `people` WHERE `id` = %s;"
                        cursor.execute(sql, (id))
                        connection.commit()
                else:
                    return "failed"
        except pymysql.Error:
            return "failed"
        except TypeError:
            return "failed"
        finally:
            connection.close()

    return connection
