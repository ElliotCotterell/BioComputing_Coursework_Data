import sqlite3

# Connect to the database
conn = sqlite3.connect('sequences.db')

# Create a cursor
cursor = conn.cursor()

# Execute a query to get column names from the database
cursor.execute("SELECT * FROM sequences LIMIT 0")

# Fetch the column names and print them
column_names = [description[0] for description in cursor.description]
print(column_names)

# ['id', 'name', 'sequence']

# Execute a query to fetch data from the database
cursor.execute("SELECT * FROM sequences")

# Fetch the first row and print it
#first_row = cursor.fetchone()
#print(first_row)

# Fetch the rest of the rows and print them
#rows = cursor.fetchall()
#for row in rows:
 #   print(row)

# Close the connection
conn.close()

