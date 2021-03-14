import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries 

def load_staging_tables(cur, conn):
    """
    Loads data into staging tables using the queries in `copy_table_queries` list.
    
    This essentially copies songs and log data from S3 using IAM role, and JSON file path (needed for staging_events)
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """
    Inserts data into fact and dimension tables using the queries in `create_table_queries` list. 
    
    Note that the data is inserted from staging tables into these tables, not directly from S3. 
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    - Configuration file 'dwh.cfg' is parsed using 'configparser' module 
    
    - Establishes connection with the database in Redshift cluster's nodes using values stored in config file and make a cursor object for it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
        
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()