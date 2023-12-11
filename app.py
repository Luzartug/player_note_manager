from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    note = db.Column(db.Integer, nullable=False)

    def json(self):
        return {"id": self.id, "name": self.name, "note": self.note}

db.create_all()

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'Test success'}), 200)


#Create a route to add a player
@app.route('/player', methods=['POST'])
def create_player():
  try:
    data = request.get_json()
    new_player = Player(name=data['name'], note=data['note'])
    db.session.add(new_player)
    db.session.commit()
    return make_response(jsonify({'message': 'Player created'}), 201)
  except Exception as e:
    return make_response(jsonify({'message': 'error creating player'}), 500)

# get all players
@app.route('/players', methods=['GET'])
def get_players():
  try:
    players = Player.query.all()
    return make_response(jsonify({'players': [player.json() for player in players]}), 200)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting players'}), 500)

# get a player by id
@app.route('/player/<int:id>', methods=['GET'])
def get_player(id):
  try:
    player = Player.query.filter_by(id=id).first()
    if player:
      return make_response(jsonify({'player': player.json()}), 200)
    return make_response(jsonify({'message': 'player not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error getting player'}), 500)

# update a player
@app.route('/player/<int:id>', methods=['PUT'])
def update_player(id):
  try:
    player = Player.query.filter_by(id=id).first()
    if player:
      data = request.get_json()
      player.name = data['name']
      player.note = data['note']
      db.session.commit()
      return make_response(jsonify({'message': 'player updated'}), 200)
    return make_response(jsonify({'message': 'player not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating player'}), 500)

# delete a player
@app.route('/player/<int:id>', methods=['DELETE'])
def delete_player(id):
  try:
    player = Player.query.filter_by(id=id).first()
    if player:
      db.session.delete(player)
      db.session.commit()
      return make_response(jsonify({'message': 'player deleted'}), 200)
    return make_response(jsonify({'message': 'player not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error deleting player'}), 500)