import psycopg2

# Establish connection
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="1CINFO",
    user="vdgb5",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Define the table creation query with placeholders
create_table_query = """
    CREATE TABLE message_data (
        id SERIAL PRIMARY KEY,
        sending_process_status BOOLEAN,
        need_rewrite BOOLEAN,
        message_type VARCHAR(32),
        processing_type VARCHAR(32),
        receiver_system VARCHAR(32),
        message_id VARCHAR(32),
        sender_system VARCHAR(32)
    )
"""

# Execute the table creation query
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
