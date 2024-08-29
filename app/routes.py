from flask import Flask, request, jsonify, abort
from app import app, db
from app.models import Player, FantasyTeam

@app.route('/api/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    players_list = [
        {
            'id': player.id,
            'position': player.position,
        }
    for player in players
    ]
    return jsonify(players_list)

@app.route('/', methods=['GET'])
def get_player(id):
    player = Player.get_or_404(id)
    return jsonify({
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'total_yards': player.total_yards,
        'touchdowns': player.touchdowns
    })
