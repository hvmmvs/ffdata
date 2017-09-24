from flask import Flask, render_template, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse

import nflgame
import numpy as np

from ff import app, api

COLORS = ['#e53935', '#9c27b0', '#e91e63', '#3f51b5', 
		  '#673ab7', '#03a9f4', '#2196f3', '#009688',  
		  '#00bcd4', '#8bc34a', '#4caf50', '#ffeb3b',  
		  '#cddc39', '#ff8c00', '#ffc107', '#ff5722']

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, (list, np.ndarray)):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    elif isinstance(input, bool):
        print input
        return str(input)
    else:
        return input

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/targets')
def targets():
	teams = [[t[1], t[2], t[0]] for t in nflgame.teams]
	teams[21] = ['New York', 'Jets']
	teams[22] = ['New York', 'Giants']
	return render_template('targets.html', teams=teams)

@app.route('/team_targets/<team>', methods=['GET', 'POST'])
def team_targets(team):
	team_initials = nflgame.standard_team(team)
	if team_initials == 'SD':
		team_initials = 'LAC'
	if team_initials == 'JAC':
		team_initials = 'JAX'
	games = nflgame.games(2017, home=team_initials, away=team_initials)
	target_dict = {}
	for i, game in enumerate(games):
		target_dict[i+1] = api.receiving_targets(game, team_initials)
	all_players = []
	for player_dict in target_dict.values():
		all_players += player_dict.keys()
	all_players = list(set(all_players))
	data = [[player_dict[player_name] if player_name in player_dict.keys() else '' for player_name in all_players]
	 			for player_dict in target_dict.values()]
	background_colors = COLORS[:len(all_players)]
	labels = map(str, all_players)

	schedule = api.get_team_schedule(team_initials, 2017)
	print team_initials
	return render_template('team_targets.html', team=team, data=data, background_colors=background_colors, labels=labels, schedule=convert(schedule), teamInitials=team_initials)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")