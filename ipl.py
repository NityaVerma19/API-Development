import pandas as pd
import numpy as np

matches = pd.read_csv("C:/Users/DELL/Downloads/ipl-matches.csv")
matches

print(matches.head())

def teamsAPI():
    teams =  list(set(list(matches['Team1']) + list(matches['Team2'])))   #list of all the teams that are playing in ipl
    teams_dict = {
        'teams' : teams       #we made it into a dictionary because we wanted to return a json file and dict is very similar to json

    }

    return teams_dict

team1 = 'Rajasthan Royals'
team2 = 'Royal Challengers Bangalore'


def teamVteamAPI(team1, team2):

    Valid_team = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 in Valid_team and team2 in Valid_team:
        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (
                matches['Team2'] == team1)]
        # temp_df shows all the matches between these two particular teams
        total_matches = temp_df.shape[0]  # total matches of these two teams

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]  # team 2 ne kitne jeete hai
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]
        draws = total_matches - (matches_won_team1 + matches_won_team2)


        response = {
            'total matches' : str(total_matches),
            team1 : str(matches_won_team1),
            team2 : str(matches_won_team2),
            'draw' : str(draws)

        }
        return response
    else:
        return {'message': 'Invalid team name'}

teamVteamAPI('Rajasthan Royals' , 'Royal Challengers Bangalore')