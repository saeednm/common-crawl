import psycopg2
from urllib.parse import urlparse
import psycopg2
import pandas as pd
from db_config import db_config

def read_table_into_df(db_config, table_name, link_column):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        # Fetch all links from the database
        cur.execute(f"SELECT {link_column} FROM {table_name};")
        rows = cur.fetchall()

        data = [url for (url,) in rows]
        df = pd.DataFrame(data,columns=['link'])
    
        # Close the database connection
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
    return df


df = read_table_into_df(db_config, 'external_links', "link")
print(df)