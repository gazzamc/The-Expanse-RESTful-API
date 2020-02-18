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
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `people` WHERE `name` = %s;"
                cursor.execute(sql, (name))
                result = cursor.fetchone()

                if result is None:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        INSERT INTO `people` (`name`, `status`, `gender`, `desc`) VALUES(%s, %s, %s, %s);"
                        cursor.execute(sql, (name, status, gender, desc))
                        connection.commit()
                else:
                    return "failed"
        except pymysql.Error:
            return "failed"
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

                if result is not None:
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
        finally:
            connection.close()

    return connection


def edit_people(id, name="", status="", gender="", desc=""):
    connection = connect_to_db()

    if connection != "failed":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `people` WHERE `id` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                # set values if inputed value is empty
                if name == "" or name is None:
                    name = result['name']
                if status == "" or status is None:
                    status = result['status']
                if gender == "" or gender is None:
                    gender = result['gender']
                if desc == "" or desc is None:
                    desc = result['desc']

                if result is not None:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        UPDATE `people` SET `name` = %s, `status` = %s, `gender` = %s, `desc` = %s WHERE `id` = %s;"
                        cursor.execute(sql, (name, status, gender, desc, id))
                        connection.commit()
                else:
                    return "failed"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()

    return connection
