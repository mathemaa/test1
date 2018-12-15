
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db = SQLAlchemy()

#aufrufen der methode connect zur Verbindung mit der PostgreSQL DB

conn = psycopg2.connect(
  database="project1",
  user="postgres",
  host="localhost",
  port="5432"
  )


#cur = conn.cursor()
#cur.execute("select * from Site1")
#for site1 in cur.fetchall():
#  print site1


#SQL-Befehl ausfuehren

# Machen wir gebrauch vom cursor, da dieser nicht geschlossen wird: cursor.close() ?

#Definierte Klasse 

# Funktion bzw Methode mit den dazugehoerigen Argumenten in klammern

#wie eine neue Instanz der Klasse erzeugt wird.
#Die angegebenen Argumente werden dabei als Eigenschaften=Attribute der Instanz,
#die in Python mit self bezeichnet wird, gespeichert.

class zustand(db.Model):
  __tablename__ = 'site1'
  id = db.Column(db.Integer, primary_key = True)
  floor = db.Column(db.String(100))
  room = db.Column(db.String(100), unique=True)
  status = db.Column(db.String(100))
  



  def __init__(self, floor, room, status):
    #Attribute der Klasse -> self.xxxx
   self.floor = floor
   self.room = room 
   self.status = status 




conn.close()

#print("DB queries completed")  
