from flask import Flask , jsonify, request
#jsonify will convert into json
import ipl

app = Flask(__name__)   #?

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')   #all the teams that are playing in ipl
def teams():
    teams = ipl.teamsAPI()      #iple wala file.function ka naa
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamVteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1,team2)
    return jsonify(response)
app.run(debug = True)









