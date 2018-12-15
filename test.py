import csv
import psycopg2
from flask_sqlalchemy import SQLAlchemy

conn = psycopg2.connect(
  database="stevebreden",
  user="postgres",
  host="localhost",
  port="5432"
  )

cur = conn.cursor()

with open('Duplex_A_20110907_rooms.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO csv_files VALUES (%s, %s, %s, %s)",
            row
        )
conn.commit()

#with open('Duplex_A_20110907_rooms.csv') as f:
 #   reader = csv.reader(f)
  #  for row in reader:
   #      print(row)