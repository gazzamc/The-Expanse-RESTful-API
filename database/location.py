import pymysql.cursors
from database.database import connect_to_db


def get_locations_query(id=None, offset=0):
    connection = connect_to_db()

    if connection != "no connection":
        result = []

        try:
            with connection.cursor() as cursor:
                if id is None:
                    """ Get Count of Rows """
                    sql = "SELECT COUNT(*) \
                           FROM `locations`;"
                    cursor.execute(sql)
                    count = cursor.fetchone()
                    count = count['COUNT(*)']

                    sql = "SELECT l.LocationID as id, l.name, l.population, s.name as system, l.desc \
                           FROM locations l \
                           JOIN systems s \
                           ON l.SystemID = s.SystemID \
                           LIMIT 25 \
                           OFFSET %s;"
                    cursor.execute(sql, (int(offset)))
                    result = cursor.fetchall()
                else:
                    sql = "SELECT l.LocationID as id, l.name, l.population, s.name as system, l.desc \
                           FROM locations l \
                           JOIN systems s \
                           ON l.SystemID = s.SystemID \
                           WHERE l.LocationID = %s"
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
                    sql = "SELECT LocationID as id, name\
                           FROM `locations`\
                           WHERE `name` \
                           LIKE %s;"
                    query = (param + '%')
                elif filter == "system":
                    sql = "SELECT l.LocationID as id, l.name, s.name as system\
                           FROM `locations` l\
                           JOIN systems s \
                           ON l.SystemID = s.SystemID \
                           WHERE s.name \
                           LIKE %s;"
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


def add_location_query(name, population, system, desc):
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `locations` WHERE `name` = %s;"
                cursor.execute(sql, (name))
                result = cursor.fetchone()

                if result is None:
                    # Get system id
                    with connection.cursor() as cursor:
                        sql = "SELECT systemid \
                                FROM `systems` \
                                WHERE `name` = %s;"
                        cursor.execute(sql, (system))
                        result = cursor.fetchone()

                        if result is not None:
                            system_id = result['systemid']
                        else:
                            return "system incorrect"

                    with connection.cursor() as cursor:
                        sql = "\
                        INSERT INTO `locations` \
                        (`name`, `population`, `systemid`, `desc`) \
                        VALUES(%s, %s, %s, %s);"
                        cursor.execute(sql,
                                       (name, population, system_id, desc))
                        connection.commit()
                else:
                    return "duplicate"
        except pymysql.Error:
            return "failed"
        finally:
            connection.close()
    else:
        return connection


def edit_location_query(id, name="", population="", system="", desc=""):
    connection = connect_to_db()

    if connection != "no connection":
        try:
            # check if record exists first
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `locations` WHERE `locationid` = %s;"
                cursor.execute(sql, (id))
                result = cursor.fetchone()

                if result is not None:
                    # set values if inputed value is empty
                    if name == "" or name is None:
                        name = result['name']
                    if population == "" or population is None:
                        population = result['population']
                    if desc == "" or desc is None:
                        desc = result['desc']

                    # Get system id if changed
                    if system == "" or system is None:
                        system_id = result['SystemID']
                    else:
                        with connection.cursor() as cursor:
                            sql = "SELECT systemid \
                                    FROM `systems` \
                                    WHERE `name` = %s;"
                            cursor.execute(sql, (system))
                            result = cursor.fetchone()
                            system_id = result['systemid']

                    # Added to DB
                    with connection.cursor() as cursor:
                        sql = "\
                        UPDATE `locations` \
                        SET `name` = %s, `population` = %s, \
                        `systemid` = %s, `desc` = %s \
                        WHERE `locationid` = %s;"
                        cursor.execute(sql,
                                       (name, population, system_id, desc, id))
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
