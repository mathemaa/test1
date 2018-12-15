from flask import Flask, request, redirect, render_template
from database import db, zustand

app = Flask(__name__)

#disabling event tracker SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/project1'
db.init_app(app)

#ROUTING
@app.route("/")
def index():
  return render_template("index.html")

# GET request
@app.route('/rooms')
def rooms():
  datas = zustand.query.all()
  return render_template('rooms.html',  datas=datas)

@app.route('/final')
def final():
  datas = zustand.query.all()
  return render_template('final.html',  datas=datas)
  

@app.route('/rooms/list')
def tableau():
  datas = zustand.query.all()
  return render_template('list.html',  datas=datas)

#post method to send data from client to server site
@app.route('/add', methods=['POST'])
def add_room():
    newroom=zustand(request.form['floor'], request.form['room'], request.form['status'])
    db.session.add(newroom)
    db.session.commit()
    return redirect('/final')

#mapping model using id
@app.route("/final/delete/<int:id>")
def delete_room(id):
  room = zustand.query.filter_by(id=id).first()
  db.session.delete(room)
  db.session.commit()
  return redirect('/final')
  
@app.route("/final/edit/<int:id>")
def edit(id):
  x = zustand.query.all()
  room = zustand.query.filter_by(id=id).first()
  return render_template('editroom.html', datas=x, room=room)
  
  #rooms = zustand.query.all()
  #if request.methods =='GET':
   # return render_template ('final.html', room=room, rooms=rooms)
  #else:
   # floor=request.form['floor']
    #floor=request.form['room']
    #room.update({'floor':floor, 'room':room})
    #db.session.commit()
    #return redirect('/add')


@app.route("/final/update/<int:id>", methods=['POST'])
def update(id):
  room = zustand.query.filter_by(id=id).first()
  room.floor = request.form['floor']
  room.status =request.form['status']
  room.room =request.form['room']
  db.session.commit()
  return redirect('/final')

    
#debug mode for occuring problems and mistake informations when debugging the code 
if __name__ == "__main__":
  app.run(debug=True)