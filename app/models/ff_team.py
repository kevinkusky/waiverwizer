"""Player Model"""
from app import db

class FantasyTeam(db.Model):
    """Model, attributes, and methods for User's Fantasy Team"""
    __tablename__ = 'fantasy_team'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(75), nullable=False)
    players = db.relationship('Player', backref='fantasy_team', lazy=True)

    def __repr__(self):
        return f'<FantasyTeam {self.team_name}, Players {len(self.players)}'
