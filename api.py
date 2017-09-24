import nflgame
import numpy as np

def get_team_plays(team, week=None):
	games = nflgame.games(2017, home=team, away=team, week=week)
	plays = nflgame.combine_plays(games)
	team_plays = plays.filter(team=team)
	return team_plays
	
def get_team_combine_stats(team, week=None):
	games = nflgame.games(2017, home=team, away=team, week=week)
	plays = nflgame.combine_play_stats(games)
	team_plays = plays.filter(team=team)
	return team_plays

def receiving_targets(game, team):
	# plays = get_team_combine_stats(team, week=week)
	plays = nflgame.combine_play_stats([game])
	team_plays = plays.filter(team=team)
	receiving_targets = {str(i.name): i.receiving_tar for i in team_plays.receiving()}
	return receiving_targets

def get_team_schedule(team, year):
	team_games = np.array(nflgame.sched.games.values())[
		map(lambda x: 
			(x['away'] == team or x['home'] == team) and 
			(x['year'] == year and x['season_type'] == 'REG')
		, nflgame.sched.games.values())]
	return team_games

# def pass_targets(team_plays):
# 	receiving_targets = {}
# 	larry_plays = []
# 	pass_plays = [t for t in team_plays if t.receiving_tar]
# 	print len(pass_plays)
# 	for p in pass_plays:
# 		receiving_play = [e for e in p.events if 'receiving_tar' in e.keys()][0]
# 		if receiving_play['playername'] in receiving_targets.keys():
# 			receiving_targets[receiving_play['playername']] += 1
# 			if receiving_play['playername'] == 'L.Fitzgerald':
# 				larry_plays.append(p)
# 		else:
# 			receiving_targets[receiving_play['playername']] = 1
# 			if receiving_play['playername'] == 'L.Fitzgerald':
# 				larry_plays.append(p)
# 	return receiving_targets, larry_plays


