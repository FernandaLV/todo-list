#!/usr/bin/python
import psycopg2
from bd.config import config

def startConnection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        return conn


def closeConnection(conn):
    if conn is not None:
        conn.close()

def insertTask (key, task, details, status):

    sql = "INSERT INTO tasks (key, task, details, status) VALUES(%s, %s, %s, %s) RETURNING id;"

    taskId = None

    conn = startConnection()

    try:
        # create a cursor
        cur = conn.cursor()
        
        # execute insert query     
        cur.execute(sql, (key, task, details, status))

        # get the generated id back
        taskId = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        closeConnection(conn)
        return taskId

def selectAll ():

    sql = "SELECT id, key, \"timestampCreate\", task, details, status FROM tasks"

    todoList = None

    conn = startConnection()

    try:
        # create a cursor
        cur = conn.cursor()
        
        # execute select query     
        cur.execute(sql)

        # get list
        todoList = cur.fetchall()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        closeConnection(conn)
        return todoList


def selectOne(key):

    sql = "SELECT key, \"timestampCreate\", task, details, status FROM tasks WHERE key = %s;"

    todoList = None

    conn = startConnection()

    try:
        # create a cursor
        cur = conn.cursor()

        # execute select query     
        cur.execute(sql, (key, ))

        # get list
        todoList = cur.fetchone()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        closeConnection(conn)
        return todoList

def updaeteTask(key, task, details, status):
    
    sql = "UPDATE tasks SET task = %s, details = %s, status = %s WHERE key= %s RETURNING id;"

    taskId = None

    conn = startConnection()

    try:
        # create a cursor
        cur = conn.cursor()
        
        # execute insert query     
        cur.execute(sql, (task, details, status, key))

        # get the generated id back
        taskId = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        closeConnection(conn)
        return taskId

def deleteTask(key):
    
    sql = "DELETE FROM tasks WHERE key= %s RETURNING id;"

    taskId = None

    conn = startConnection()

    try:
        # create a cursor
        cur = conn.cursor()
        
        # execute insert query     
        cur.execute(sql, (key, ))

        # get the generated id back
        taskId = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        closeConnection(conn)
        return taskId

