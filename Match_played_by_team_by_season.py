import csv
import matplotlib.pyplot as plt
from functions import bar_plot, stacked_chart_plot

# String constants
TEAM = "Team"
MATCHES_PLAYED = "Number of matches played"
MATCHES_BY_TEAM_BY_SEASON = "Number of matches played by team by season"

# File names
CSV_FILE_PROB_4_5_6 = 'matches.csv'


def plot_matches_statistics():
    ''' function to get data to plot graphs'''
    # get required data from csv in dict and then call plot function
    with open(CSV_FILE_PROB_4_5_6, encoding="utf-8") as inputfile:
        season_details = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            team1 = match['team1']
            team2 = match['team2']
            season_details[season_year] = (
                season_details.get(season_year, {})
            )
            season_details[season_year][team1] = (
                season_details[season_year].get(team1, 0) + 1
            )
            season_details[season_year][team2] = (
                season_details[season_year].get(team2, 0) + 1
            )

        stacked_chart_plot(season_details, TEAM,
                           MATCHES_PLAYED, MATCHES_BY_TEAM_BY_SEASON)

        # show plot
        plt.show()


plot_matches_statistics()  # calling the new function
