import psycopg2
import psycopg2.extras
import io
import string 
import os
from db_config import db_config

txt_file_directory = "links_txt"
table_name = "external_links"

def insert_links_to_db(links, db_config):
    # Establish a database connection
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
             link TEXT
        );
        """
    cursor.execute(create_table_query)
    
    # Convert data to a CSV-like string (without headers)
    buffer = io.StringIO()
    for row in links:
        buffer.write('\t'.join([str(field) for field in row]) + '\n')

    # Move the cursor back to the beginning of the StringIO buffer
    buffer.seek(0)

    # Perform the bulk insert with copy_from
    cursor.copy_from(buffer, 'external_links', columns=('link',))

    

    # insert_query = 'INSERT INTO external_links (link) VALUES (%s)'
    # psycopg2.extras.execute_values (cursor, insert_query, links, template=None, page_size=10)



    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()


def read_and_insert_links_to_db():
    links = []

    with os.scandir(txt_file_directory) as iter:
            for entry in iter:
                if entry.name.endswith(".warc.gz.txt") and entry.is_file():
                    print(entry.name, entry.path)
                    with open(entry.path, 'r') as file:
                        for line in file:
                            links.append((line.rstrip(),))

    print(f"records to be added: {len(links)}" )
    # Insert links into the database
    insert_links_to_db(links, db_config)

read_and_insert_links_to_db()