import csv
import matplotlib.pyplot as plt
from functions import bar_plot


def plot_total_runs_by_team():
    ''' function to get data to plot total runs by each team'''
    # ... (existing code)

    # get required data from csv in dict and then call appropriate plot functions
    with open('deliveries.csv', encoding="utf-8") as inputfile:
        team_wise_runs = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            runs_in_this_ball = int(delivery['total_runs'])
            team_wise_runs[delivery['batting_team']] = (
                team_wise_runs.get(
                    delivery['batting_team'], 0) + runs_in_this_ball
            )

    # Plotting total runs by each team
    bar_plot(team_wise_runs, "Team", "Total Runs",
             "Total runs scored by each teams over the history of IPL")
    plt.show()


plot_total_runs_by_team()  # invoking the renamed function
