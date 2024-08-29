"""Player Model"""
from app import db

class Player(db.Model):
    """Model, attributes, and methods for Players"""
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    team = db.Column(db.String(75), nullable=False)
    position = db.Column(db.String(3), nullable=False)
    avg_ownership = db.Column(db.Float, default=0.0)
    tot_yards = db.Column(db.Integer, default=0)
    tot_touchdowns = db.Column(db.Integer, default=0)
    avg_targets = db.Column(db.Float, default=0.0)
    avg_receptions = db.Column(db.Float, default=0.0)
    avg_rush_attempts = db.Column(db.Float, default=0.0)
    avg_yards = db.Column(db.Float, default=0.0)
    avg_passing_attempts = db.Column(db.Float, default=0.0)
    avg_passing_yards = db.Column(db.Float, default=0.0)
    avg_points = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Player {self.name}, Position {self.position}>'

    @staticmethod
    def high_performance_low_ownership(min_avg_points=10, max_ownership=50):
        """List players with consistant performers likely to be available"""
        return Player.query.filter(
            Player.avg_points >= min_avg_points,
            Player.avg_ownership <= max_ownership
        ).order_by(Player.avg_points.desc()).all()

    @staticmethod
    def ownership_spike(min_increase=20, max_ownership=60):
        """Lists players with spike of ownership"""
        pass

    @staticmethod
    def production_jump():
        """Lists players with increased production"""
        pass
