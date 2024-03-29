import psycopg2

# Establish connection
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="onec_cinfo",
    user="oleg",
    password="Zxcv7890"
)

# Create a cursor object
cur = conn.cursor()

# Define the table creation query with placeholders
create_table_query = """
    CREATE TABLE message_data (
        sending_process_status BOOLEAN,
        need_rewrite BOOLEAN,
        message_type VARCHAR(32),
        processing_type VARCHAR(32),
        receiver_system VARCHAR(32),
        message_id VARCHAR(50),
        sender_system VARCHAR(32),
        data BYTEA,
        received BOOLEAN
    )
"""

# Execute the table creation query
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
print("ok")