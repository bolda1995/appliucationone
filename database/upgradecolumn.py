import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="onec_cinfo",
    user="oleg",
    password="Zxcv7890"

)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the ALTER TABLE query to modify the column data type
alter_query = "ALTER TABLE message_data ALTER COLUMN message_id  TYPE VARCHAR(50)"
cursor.execute(alter_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
