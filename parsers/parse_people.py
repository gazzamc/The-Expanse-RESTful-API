"""
    Extracts data from https://expanse.fandom.com
    using beautifulsoup and inserts it into
    the database.
"""

from bs4 import BeautifulSoup
from database import connect_to_db
import requests
import pymysql.cursors


def get_page(link):
    '''
    Takes in URL and gets the HTML source.

            Parameters:
                    link (string): string of URL

            Returns:
                    Object: returns beautiful soup object
    '''
    page = requests.get(baseUrl + link)
    html = BeautifulSoup(page.text, 'lxml')

    return html


def get_char_name(source):
    '''
    Takes in HTML source code and extracts characters name.

            Parameters:
                    source (Object): Beautiful Soup Object

            Returns:
                    string: returns string of name
    '''
    html = source

    try:
        name = html.find("h2", attrs={'data-source': 'name'}).get_text()
        if name[-4:] == "(TV)":
            name = name.replace("(TV)", "")
    except AttributeError:
        name = None

    return name


def get_char_status(source):
    '''
    Takes in HTML source code and extracts characters status.

            Parameters:
                    source (Object): Beautiful Soup Object

            Returns:
                    string: returns string of status
    '''
    html = source

    try:
        s = html.find("div",
                      attrs={
                       'data-source': 'status'}
                      ).find("div",
                             attrs={
                              'class', 'pi-data-value'}
                             ).get_text().strip().encode(
                                                    "ascii",
                                                    errors="ignore").decode()
        """Need to encode/decode to remove symbol on alive status"""

        if s is not None:
            if s.lower() == "alive" or s.lower() == "deceased":
                status = s
            else:
                status = s.strip().split('(')[0]
                status = status.strip().split('[')[0].strip()
        else:
            status = None
    except AttributeError:
        status = None

    return status


def get_char_gender(source):
    '''
    Takes in HTML source code and extracts characters gender.

            Parameters:
                    source (Object): Beautiful Soup Object

            Returns:
                    string: returns string of gender
    '''
    html = source

    try:
        gender = html.find("div",
                           attrs={'data-source': 'gender'}
                           ).find("div",
                                  attrs={'class', 'pi-data-value'}).get_text()
        if gender is not None:
            if gender.lower() == "male" or gender.lower() == "female":
                gender = gender
            else:
                gender = gender[1:].strip().split('[')[0]
                if gender == "":
                    gender = None
    except AttributeError:
        gender = None

    return gender


def get_char_desc(source):
    '''
    Takes in HTML source code and extracts characters description.

            Parameters:
                    source (Object): Beautiful Soup Object

            Returns:
                    string: returns string of description
    '''
    html = source

    try:
        description = html.find("nav",
                                attrs={'id': 'toc'}
                                ).previous_sibling.previous_sibling.find(
                                    "h2",
                                    attrs={'data-source': 'name'})

        if description is None:
            description = html.find(
                "nav",
                attrs={
                        'id': 'toc'
                        }).previous_sibling.previous_sibling.get_text().strip()
        else:
            description = None
            return description

        """ Check if string is empty, if so go to previous sibling """
        if len(description) == 0:
            description = html.find(
                "nav",
                attrs={
                    'id': 'toc'}
                    ).previous_sibling.previous_sibling.previous_sibling
            description = description.get_text().strip()

    except AttributeError:
        description = None

    return description


baseUrl = "https://expanse.fandom.com"

soup = get_page("/wiki/Characters_(TV)")
tables = soup.find_all("div", attrs={'class': 'floatnone'})

# make connection to db
connection = connect_to_db()

# loop through each link, retreive the data and add to db
for table in tables:
    if (table.a['href'] == "/wiki/Characters_(TV)" or
            table.a['href'] == "/wiki/Menacing_Belter_#2"):
        continue
    else:
        html = get_page(table.a['href'])

        name = get_char_name(html)
        status = get_char_status(html)
        gender = get_char_gender(html)
        desc = get_char_desc(html)

        if name is not None:
            if status is not None:
                if status.lower() != "alive" and status.lower() != "deceased":
                    status = "Unknown"
            else:
                status = "Unknown"
            if gender is not None:
                if gender.lower() != "male" and gender.lower() != "female":
                    gender = "Unknown"
            else:
                gender = "Unknown"
            if desc is None:
                desc = ""

            # Check if record exists first
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT COUNT(*) \
                           FROM `people` \
                           WHERE `name` = %s;"
                    cursor.execute(sql, (name))
                    result_set = cursor.fetchone()

                    if result_set['COUNT(*)'] == 0:
                        # Add data to DB
                        try:
                            with connection.cursor() as cursor:
                                sql = "\
                                INSERT INTO `people` \
                                (name`, `status`, `gender`, `desc`)\
                                VALUES(%s, %s, %s, %s);"
                                cursor.execute(sql,
                                               (name, status, gender, desc))
                                connection.commit()
                        except pymysql.Error:
                            print("No Connection to Db")
            except pymysql.Error:
                print("Not found ")
            finally:
                connection.close()
        else:
            continue
