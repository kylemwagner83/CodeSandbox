import sqlite3
from sqlite3 import Error

database = r"E:/Coding/CodingPractice/modules/db/test.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_my_tables():
    sql_create_games_table = """ CREATE TABLE IF NOT EXISTS games (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    played text
                                ); """


    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    watched text
                                ); """


    sql_create_tvshows_table = """ CREATE TABLE IF NOT EXISTS tvshows (
                                    name text PRIMARY KEY,
                                    downloaded_on text,
                                    watched text
                                ); """

    conn = create_connection(database)                                

    if conn is not None:
        create_table(conn, sql_create_games_table)
        create_table(conn, sql_create_movies_table)
        create_table(conn, sql_create_tvshows_table)

    else:
        print("Error! Cannot create the database connection")



def create_game(conn, game):
    sql = """INSERT INTO games(name,downloaded_on,played)
                VALUES(?,?,?) """
    
    c = conn.cursor()
    c.execute(sql, game)
    conn.commit()
    return c.lastrowid

def create_movie(conn, movie):
    sql = """INSERT INTO movies(name,downloaded_on,watched)
                VALUES(?,?,?) """
    
    c = conn.cursor()
    c.execute(sql, movie)
    conn.commit()
    return c.lastrowid

def create_tvshow(conn, tvshow):
    sql = """INSERT INTO tvshows(name,downloaded_on,watched)
                VALUES(?,?,?) """

    c = conn.cursor()
    c.execute(sql, tvshow)
    conn.commit()
    return c.lastrowid


def create_data():
    conn = create_connection(database)
    with conn:
        game1 = ("Game 1","Tue Dec  1 18:10:46 2020","No")
        create_game(conn, game1)

        movie1 = ("Movie 1","Wed Dec  2 10:24:30 2020", "Yes")
        create_movie(conn, movie1)

        tvshow1 = ("TV Show 1","Mon Nov 30 5:35:14 2020", "No")
        create_tvshow(conn, tvshow1)


def update_game(conn, game):
    sql = """UPDATE games
                SET played = ?
            WHERE name = ? """

    c = conn.cursor()
    c.execute(sql, game)
    conn.commit()


def update_data():
    conn = create_connection(database)
    with conn:
        update_game(conn, ("Yes", "Game 1"))


def delete_game(conn, game):
    sql = "DELETE FROM games WHERE name=?"
    c = conn.cursor()
    c.execute(sql, (game,))
    conn.commit()


def delete_all_games(conn):
    sql = "DELETE FROM games"
    c = conn.cursor()
    c.execute(sql)
    conn.commit()


def delete_data():
    conn = create_connection(database)
    with conn:
        delete_game(conn, "Game 1")






if __name__ == "__main__":
    create_data()