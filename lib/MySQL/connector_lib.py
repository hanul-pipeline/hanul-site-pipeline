import mysql.connector, json, csv

# CSV File Located At Local
PATH_DB = '/Users/kimdohoon/src/google/hanul_sql.csv'
with open(PATH_DB, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        db_data = row

# CREATE CONNECTIONS & CURSORS
def mysql_connect():
    conn = mysql.connector.connect(
        host=row[0],
        user=row[1],
        password=row[2],
        database="hanul_site"
    )
    return conn

# UPDATE DATABASE
def JSON_to_table(JSON_DIR, TABLE_NAME):
    conn = mysql_connect()
    cursor = conn.cursor()
    with open(JSON_DIR) as file:
        data = json.load(file)
    sensor_id = data['sensor_id']
    date = data['date']
    time = data['time']
    value = data['value']
    query = f"INSERT INTO {TABLE_NAME} (sensor_id, date, time, value) \
              VALUES ({sensor_id}, {date}, {time}, {value})"
    cursor.execute(query)
    conn.commit()