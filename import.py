import csv
import psycopg2
from flask_sqlalchemy import SQLAlchemy

conn = psycopg2.connect(
  database="stevebreden",
  user="postgres",
  host="localhost",
  port="5432"
  )



# Notice that we don't need the `csv` module.
#with open('Duplex_A_20110907_rooms.csv') as f:
#  next(f)  # Skip the header row.
#  cur.copy_from(f, 'csv_datas4', sep=';')

cur = conn.cursor()
cur.execute("select * from csv_datas4")

with open('Duplex_A_20110907_rooms.csv', 'r') as f:
  reader = csv.reader(f, delimiter=';')
  #next(reader)  # Skip the header row.
  for row in reader:
    print(row)
    cur.execute(
          " INSERT INTO csv_datas4 (floor, room, function) VALUES (%s, %s, %s)",
        (row[1], row[2], row[3])
     #   row
    )



conn.commit()


#insert_query = "INSERT INTO csv_datas4 VALUES {}".format("(11, '1.OG', '1.13', 'WOhnzimmer', 'Angefangen')")
#cur.execute(insert_query)


#with open('Duplex_A_20110907_rooms.csv') as f:
#   reader = csv.reader(f)
#   for row in reader:
#    print(row)

