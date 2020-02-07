from bs4 import BeautifulSoup
from database import connectToDb
import requests
import pymysql.cursors


def getPage(link):
    page = requests.get(baseUrl + link)
    html = BeautifulSoup(page.text, 'lxml')

    return html


def getCharName(source):
    html = source

    try:
        name = html.find("h2", attrs={'data-source': 'name'}).get_text()
        if name[-4:] == "(TV)":
            name = name.replace("(TV)", "")
    except AttributeError:
        name = None

    return name


def getCharStatus(source):
    html = source

    try:
        s = html.find("div", attrs={
                                    'data-source': 'status'
                                    }).find("div", attrs={
                                                        'class', 'pi-data-value'
                                                        }).get_text().strip().encode(
                                                                                    "ascii", errors="ignore"
                                                                                    ).decode() 
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


def getCharGender(source):
    html = source

    try:
        gender = html.find("div", attrs={'data-source': 'gender'}).find("div", attrs={'class', 'pi-data-value'}).get_text()
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


def getCharOccupation(source):
    html = source

    try:
        occupation = html.find("div", attrs={'data-source': 'occupation'}).find("div", attrs={'class', 'pi-data-value'}).get_text()
    except AttributeError:
        occupation = None

    return occupation


def getCharDesc(source):
    html = source

    try:
        description = html.find("nav", attrs={'id': 'toc'}).previous_sibling.previous_sibling.find("h2", attrs={'data-source': 'name'})

        if description is None:
            description = html.find("nav", attrs={'id': 'toc'}).previous_sibling.previous_sibling.get_text().strip()
        else:
            description = None
            return description

        """ Check if string is empty, if so go to previous sibling """
        if len(description) == 0:
            description = html.find("nav", attrs={'id': 'toc'}).previous_sibling.previous_sibling.previous_sibling.get_text().strip()

    except AttributeError:
        description = None

    return description


def getCharFirstApp(source):
    html = getPage(link)

    try:
        firstApp = html.find("div", attrs={'data-source': 'first appearance'})
    except AttributeError as e:
        print(e + " First")



baseUrl = "https://expanse.fandom.com"


soup = getPage("/wiki/Characters_(TV)")
tables = soup.find_all("div", attrs={'class': 'floatnone'})

connection = connectToDb()

for table in tables:
    if table.a['href'] == "/wiki/Characters_(TV)" or table.a['href'] == "/wiki/Menacing_Belter_#2":
        continue
    else:
        """ html = getPage("/wiki/Iafrate") """
        html = getPage(table.a['href']) 

        name = getCharName(html)
        status = getCharStatus(html)
        gender = getCharGender(html)
        desc = getCharDesc(html)

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
                    sql = "SELECT COUNT(*) FROM `people` WHERE `name` = %s;"
                    cursor.execute(sql, (name))
                    result_set = cursor.fetchone()

                    if result_set['COUNT(*)'] == 0:
                        print(result_set)
                        # Add data to DB
                        """ try:
                            with connection.cursor() as cursor:
                                sql = "INSERT INTO `people` (`peopleId` `name`, `status`, `gender`, `desc`) VALUES(%s, %s, %s, %s);"
                                cursor.execute(sql, (name, status, gender, desc))
                                connection.commit()
                        except pymysql.Error:
                            print("No Connection to Db ") """
            except pymysql.Error:
                print("Not found ")
            finally:
                connection.close()
        else:
            continue
