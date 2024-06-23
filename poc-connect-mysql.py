import pymysql

# Establish a database connection
conn = pymysql.connect(
    host='172.31.4.108',
    user='admin',
    password='@dv0t1csS3cr3t!',
    database='adv_warehouse'
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM adv_warehouse.adjustments ORDER BY loki_index DESC LIMIT 1')

# Fetch all results
rows = cursor.fetchall()

# Print each row
for row in rows:
   print(row)

