import psycopg2

# Establish connection to the default PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    user="your_username",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Define the database name and owner
database_name = "1СINFO"
owner = "vdgb5"

# Create the database with parameters
cur.execute(f"CREATE DATABASE {database_name} OWNER {owner}")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()