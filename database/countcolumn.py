import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="onec_cinfo",
    user="oleg",
    password="Zxcv7890"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute the query to get the column count
cursor.execute("""
    SELECT count(*) 
    FROM information_schema.columns 
    WHERE table_name = 'your_table'
""")

# Fetch the result
column_count = cursor.fetchone()[0]

# Print the number of columns
print("Number of columns:", column_count)

# Close the cursor and connection
cursor.close()
conn.close()