import csv
import matplotlib.pyplot as plt
from functions import stacked_chart_plot

# String constants
TEAM = "Team"
MATCHES_WON = "Number of matches won"
MATCHES_WON_BY_TEAM_BY_YEAR = "Number of matches won per team per year in IPL"

# File names
CSV_FILE_PROB_4_5_6 = 'matches.csv'


def plot_matches_won_per_team_per_year():
    ''' function to get data to plot matches won per team per year'''
    # get required data from csv in dict and then call plot function
    with open(CSV_FILE_PROB_4_5_6, encoding="utf-8") as inputfile:
        season_victory_details = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            winner_team = match['winner']
            season_victory_details[season_year] = (
                season_victory_details.get(season_year, {})
            )
            season_victory_details[season_year][winner_team] = (
                season_victory_details[season_year].get(winner_team, 0) + 1
            )

        stacked_chart_plot(season_victory_details, TEAM,
                           MATCHES_WON, MATCHES_WON_BY_TEAM_BY_YEAR)

        # show plot
        plt.show()


plot_matches_won_per_team_per_year()  # calling the new function
