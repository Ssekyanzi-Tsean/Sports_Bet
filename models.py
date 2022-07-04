from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(JSON)
    home_team = db.Column(JSON)
    away_team = db.Column(JSON)
    home_team_win_odds = db.Column(JSON)
    away_team_win_odds = db.Column(JSON)
    draw_odds = db.Column(JSON)
    game_date = db.Column(JSON)

    def __init__(self, league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date):
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.home_team_win_odds = home_team_win_odds
        self.away_team_win_odds = away_team_win_odds
        self.draw_odds = draw_odds
        self.game_date = game_date

    def __repr__(self) -> str:
        return '<id {}'.format(self.id)
