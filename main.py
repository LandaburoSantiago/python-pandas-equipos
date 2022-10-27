import pandas as pd

dataset_teams = pd.read_csv('equipos.csv', sep=';')
dataset_results = pd.read_csv('results.csv')

dataset_teams['local_points'] = 0
dataset_teams['visitor_points'] = 0
dataset_teams['quantity_of_draws'] = 0


array_of_intrested_columns = ['local_team',
                              'local_result', 'visitor_team', 'visitor_result']


def assingPoints(match):
    if (match['local_result'] > match['visitor_result']):
        # print("Puntos antes: ", dataset_teams.loc[dataset_teams['team'] ==
        #                                           match['local_team'], 'local_points'])
        # print("Gano", match['local_team'], '(L)')
        dataset_teams.loc[dataset_teams['team'] ==
                          match['local_team'], 'local_points'] += 3
        # print("Puntos puntos despues: ", dataset_teams.loc[dataset_teams['team'] ==
        #                                                    match['local_team'], 'local_points'])
    elif (match['local_result'] < match['visitor_result']):
        # print("Puntos antes: ", dataset_teams.loc[dataset_teams['team'] ==
        #                                           match['visitor_team'], 'visitor_points'])
        # print("Ganó:", match['visitor_team'], '(V)')
        dataset_teams.loc[dataset_teams['team'] ==
                          match['visitor_team'], 'visitor_points'] += 3
        # print("Puntos despues: ", dataset_teams.loc[dataset_teams['team'] ==
        #                                             match['visitor_team'], 'visitor_points'])
    else:
        # print("Puntos antes: ", " de ", match['local_team'],
        #       '(L)', " :", dataset_teams.loc[dataset_teams['team'] ==
        #                                      match['local_team'], 'local_points'])
        # print("empataron", match['local_team'],
        #       '(L)', match['visitor_team'], '(V)')
        dataset_teams.loc[dataset_teams['team'] ==
                          match['local_team'], 'local_points'] += 2
        dataset_teams.loc[dataset_teams['team'] ==
                          match['local_team'], 'quantity_of_draws'] += 1
        dataset_teams.loc[dataset_teams['team'] ==
                          match['visitor_team'], 'quantity_of_draws'] += 1
        # print("Puntos despues: ", " de ", match['local_team'],
        #       '(L)', " :", dataset_teams.loc[dataset_teams['team'] ==
        #                                      match['local_team'], 'local_points'])


dataset_results[array_of_intrested_columns].apply(
    func=assingPoints, axis=1)

dataset_teams['total_points'] = dataset_teams['local_points'] + \
    dataset_teams['visitor_points']
# Los 10 equipos con mayor cantidad de puntos como vistante
top_ten_visitor_points = dataset_teams.sort_values(
    by=['visitor_points'], ascending=False).head(n=10)
# Equipo que tuvo mas partidos empatados
team_with_more_draws = dataset_teams.sort_values(
    by=['quantity_of_draws'], ascending=False).head(n=1)

# Equipo con menor cantidad de puntos
team_with_less_points = dataset_teams.sort_values(
    by=['total_points']).head(n=1)
print(team_with_less_points)
