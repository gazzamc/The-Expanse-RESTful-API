import pymysql.cursors
from database import connect_to_db


def get_locations_query(id=None, offset=0):
    connection = connect_to_db()

    if connection != "no connection":
        result = []

        try:
            with connection.cursor() as cursor:
                if id is None:
                    """ Get Count of Rows """
                    sql = "SELECT COUNT(*) FROM `locations`;"
                    cursor.execute(sql)
                    count = cursor.fetchone()
                    count = count['COUNT(*)']

                    sql = "SELECT * FROM `locations` LIMIT 25 OFFSET %s;"
                    cursor.execute(sql, (int(offset)))
                    result = cursor.fetchall()
                else:
                    sql = "SELECT * FROM `locations` WHERE `locationid` = %s;"
                    cursor.execute(sql, (id))
                    result = cursor.fetchone()
                    count = 1

                    if result is None:
                        return "failed"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection

    return [result, count]


def get_location_query_filtered(filter, param):
    connection = connect_to_db()

    if connection != "no connection":
        result = []

        try:
            with connection.cursor() as cursor:

                if filter == "name":
                    sql = "SELECT locations.locationid as id, name FROM `locations` WHERE `name` LIKE %s;"
                    query = (param + '%')
                elif filter == "status":
                    sql = "SELECT systemid, name, status FROM `systems` WHERE `status` = %s;"
                    query = param
                else:
                    sql = "SELECT systemid, name, gender FROM `systems` WHERE `gender` = %s;"
                    query = param

                cursor.execute(sql, (query))
                result = cursor.fetchall()

                if result is None:
                    return "failed"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection

    return result


def add_location_query(name, planets, desc):
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `systems` WHERE `name` = %s;"
                cursor.execute(sql, (name))
                result = cursor.fetchone()

                if result is None:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        INSERT INTO `systems` (`name`, `planets`, `desc`) VALUES(%s, %s, %s);"
                        cursor.execute(sql, (name, planets, desc))
                        connection.commit()
                else:
                    return "duplicate"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection


def edit_location_query(id, name="", planets="", desc=""):
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `systems` WHERE `systemid` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                # set values if inputed value is empty
                if name == "" or name is None:
                    name = result['name']
                if planets == "" or planets is None:
                    planets = result['status']
                if desc == "" or desc is None:
                    desc = result['desc']

                if result is not None:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        UPDATE `locations` SET `name` = %s, `planets` = %s, `desc` = %s WHERE `systemid` = %s;"
                        cursor.execute(sql, (name, planets, desc, id))
                        connection.commit()
                else:
                    return "no record"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection


def delete_location_query(id):
    connection = connect_to_db()
    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `locations` WHERE `locationid` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                if result is not None:
                    with connection.cursor() as cursor:
                        sql = "\
                        \
                        DELETE FROM `locations` WHERE `locationid` = %s;"
                        cursor.execute(sql, (id))
                        connection.commit()
                else:
                    return "no record"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection
