import psycopg2

# Establish connection to the default PostgreSQL database
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    user="oleg",
    password="Zxcv7890"
)

# Create a cursor object
cur = conn.cursor()

# Define the database name and owner
database_name = "1СINFO"
owner = "oleg"

# Create the database with parameters
cur.execute(f"CREATE DATABASE {database_name} OWNER {owner}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()