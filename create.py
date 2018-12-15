#automatically create db 
#importing datas 
#visualisieren mit grundriss
#GITHUB safe !!!
import csv
import psycopg2
from flask_sqlalchemy import SQLAlchemy

conn = psycopg2.connect(
  database="stevebreden",
  user="postgres",
  host="localhost",
  port="5432"
  )

#Bei neuem Projekt und neuem Teilnehmer neue Table durch klick anlegen

cur = conn.cursor()
cur.execute("""
CREATE TABLE csv_datas4 (
  id  SERIAL PRIMARY KEY, 
  floor VARCHAR (100) NOT NULL,
  room VARCHAR (100) NOT NULL,
  function VARCHAR (100) NOT NULL,
  status VARCHAR (100) NULL
)
""")

conn.commit()


        

