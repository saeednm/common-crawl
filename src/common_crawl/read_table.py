import psycopg2
import pandas as pd

def read_table_into_df(db_config_map, table_name, link_column):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config_map)
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
    print(df)    
    return df
