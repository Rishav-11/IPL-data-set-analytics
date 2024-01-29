import csv
import matplotlib.pyplot as plt
from functions import bar_plot

# String constants
YEAR = "Year"
MATCHES_PLAYED = "Number of matches played"
MATCHES_BY_TEAM_BY_YEAR = "Number of matches played per year for all the years in IPL"

# File names
CSV_FILE_PROB_4_5_6 = 'matches.csv'


def plot_matches_per_year():
    ''' function to get data to plot matches per year'''
    # get required data from csv in dict and then call plot function
    with open(CSV_FILE_PROB_4_5_6, encoding="utf-8") as inputfile:
        yearwise_matches_played = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            yearwise_matches_played[season_year] = (
                yearwise_matches_played.get(season_year, 0) + 1
            )

        bar_plot(yearwise_matches_played, YEAR,
                 MATCHES_PLAYED, MATCHES_BY_TEAM_BY_YEAR)

        # show plot
        plt.show()


plot_matches_per_year()  # calling the new function
