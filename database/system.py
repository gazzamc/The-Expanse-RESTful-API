"""
    Contains all the different database
    queries for the systems endpoint/table.
"""
import pymysql.cursors
from database.database import connect_to_db


def get_systems_query(id=None, offset=0):
    '''
    Takes in record id, offset and
    returns an Array.

            Parameters:
                    id (int, Optional): id of specific record
                    offset (int, Optional): offset for pagination

            Returns:
                    Array: returns array of database result, count of records
    '''
    connection = connect_to_db()

    if connection != "no connection":
        result = []

        try:
            with connection.cursor() as cursor:
                if id is None:
                    """ Get Count of Rows """
                    sql = "SELECT COUNT(*) \
                           FROM `systems`;"
                    cursor.execute(sql)
                    count = cursor.fetchone()
                    count = count['COUNT(*)']

                    sql = "SELECT systemid as id, `name`, `planets`, `desc` \
                           FROM `systems` \
                           LIMIT 25 \
                           OFFSET %s;"
                    cursor.execute(sql, (int(offset)))
                    result = cursor.fetchall()
                else:
                    sql = "SELECT systemid as id, `name`, `planets`, `desc` \
                           FROM `systems` \
                           WHERE `systemid` = %s;"
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


def get_system_query_filtered(filter, param):
    '''
    Takes in filter, param and
    returns list of database result.

            Parameters:
                    filter (str): filter name
                    param (str): paramater to search for

            Returns:
                    list: returns list of database results
    '''
    connection = connect_to_db()

    if connection != "no connection":
        result = []

        try:
            with connection.cursor() as cursor:

                if filter == "name":
                    sql = "SELECT systems.systemid as id, name \
                           FROM `systems` \
                           WHERE `name` \
                           LIKE %s;"
                    query = (param + '%')

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


def add_system_query(name, planets, desc):
    '''
    Takes in name, planets, desc and returns string.

            Parameters:
                    name (str): name value
                    planets (str): planets value
                    desc (str): desc value

            Returns:
                str: returns string on success or failure
    '''
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * \
                       FROM `systems` \
                       WHERE `name` = %s;"
                cursor.execute(sql, (name))
                result = cursor.fetchone()

                if result is None:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO `systems` (`name`, `planets`, `desc`) \
                               VALUES(%s, %s, %s);"
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


def edit_system_query(id, name="", planets="", desc=""):
    '''
    Takes in id, name, planets, desc and returns string.

            Parameters:
                    id (int): id of record
                    name (str, Optional): name value
                    planets (str, Optional): planets value
                    desc (str, Optional): desc value

            Returns:
                str: returns string on success or failure
    '''
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * \
                       FROM `systems` \
                       WHERE `systemid` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                if result is not None:
                    # set values if inputed value is empty
                    if name == "" or name is None:
                        name = result['name']
                    if planets == "" or planets is None:
                        planets = result['planets']
                    if desc == "" or desc is None:
                        desc = result['desc']

                    with connection.cursor() as cursor:
                        sql = "UPDATE `systems` \
                               SET `name` = %s, `planets` = %s, `desc` = %s \
                               WHERE `systemid` = %s;"
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


def delete_system_query(id):
    '''
    Takes in id of a record and returns string.

            Parameters:
                    id (int): id of record

            Returns:
                    str: returns string on success or failure
    '''
    connection = connect_to_db()
    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * \
                       FROM `systems` \
                       WHERE `systemid` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                if result is not None:
                    with connection.cursor() as cursor:
                        sql = "DELETE FROM `systems` \
                               WHERE `systemid` = %s;"
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
