import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


def save_df_to_table(df: pd.DataFrame, db_config_map):

    # Convert 'paths' column to JSON-compatible strings
    df["paths"] = df["paths"].apply(lambda x: list(x))  # Convert set to list
    df["paths"] = df["paths"].apply(lambda x: str(x))  # Convert list to string for storage

    # Define the table schema (make sure this matches the actual PostgreSQL table structure)
    table_name = "website_categories"

    # Create a connection and insert data
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config_map)
        cur = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            domain VARCHAR(255) PRIMARY KEY,
            paths TEXT,
            category TEXT
        );
        """
        cur.execute(create_table_query)

        # Insert data using execute_values for bulk insert
        insert_query = f"INSERT INTO {table_name} (domain, paths, category) VALUES %s ON CONFLICT (domain) DO NOTHING;"
        execute_values(
            cur,
            insert_query,
            df.to_records(index=False),  # Convert DataFrame to list of tuples
        )

        # Commit changes and close connection
        conn.commit()
        print("Data successfully saved to PostgreSQL!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


