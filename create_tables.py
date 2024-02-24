# Importing the necessary modules and variables
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    Creates and connects to the ad_revenue database.
    Returns the connection and cursor to the ad_revenue database.
    """
    conn = psycopg2.connect("host=localhost port=5433 dbname=olympicsdb user=postgres password=123456 sslmode=prefer connect_timeout=10")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    return cur, conn


        
def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

        
        

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the ad_revenue database. 
    - Establishes connection with the ad_revenue database and gets
      cursor to it.  
    - Drops all the tables.  
    - Creates all tables needed. 
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()

if __name__ == '__main__':
    main()
