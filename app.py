from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSON
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:sekyanzi481@localhost:5432/sportsbet"

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class GamesDb(db.Model):
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


@app.route('/')
def hello():
    return {"Hello : World!"}


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


if __name__ == '__main':
    app.run(debug=True)
