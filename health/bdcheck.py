from healthcheck import HealthCheck, EnvironmentDump
from bd.model import startConnection, closeConnection

health = HealthCheck()
envdump = EnvironmentDump()

# check the BD is available
def bd_available():
    conn = startConnection()
    if (conn is None):
        return False, "connexion error"
    else:
        closeConnection(conn)
        return True, "connexion ok"

# check the table tasks is available 
def table_available():
    
    sql = "SELECT id FROM tasks LIMIT 1"


    conn = startConnection()
    cur = conn.cursor()
    cur.execute(sql)
    todoList = cur.fetchall()
    
    cur.close()
    closeConnection(conn)

    return True, "table ok"

# check columns are availables
def columns_available():

    sql = "SELECT key, \"timestampCreate\", task, details, status FROM tasks LIMIT 1"

    conn = startConnection()
    cur = conn.cursor()
    cur.execute(sql)
    todoList = cur.fetchall()
    
    cur.close()
    closeConnection(conn)

    return True, "columns ok"


# Add all checks functions
health.add_check(bd_available)
health.add_check(table_available)
health.add_check(columns_available)

# add your own data to the environment dump
def application_data():
    return {"maintainer": "Fernanda Lembo Vedovello",
            "git_repo": "https://github.com/FernandaLV/todo-list"}

envdump.add_section("application", application_data)

