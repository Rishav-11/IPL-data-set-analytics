import csv
import matplotlib.pyplot as plt
from functions import bar_plot


def plot_top_10_batsmen_rcb():
    ''' function to get data and plot total runs by top 10 batsmen in RCB'''
    # ... (existing code)

    # get required data from csv in dict and then call appropriate plot functions
    with open('deliveries.csv', encoding="utf-8") as inputfile:
        rcb_playerwise_runs = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            if delivery['batting_team'] == "Royal Challengers Bangalore":
                batsman = delivery['batsman']
                runs_in_this_ball = int(delivery['batsman_runs'])
                rcb_playerwise_runs[batsman] = (
                    rcb_playerwise_runs.get(batsman, 0) + runs_in_this_ball
                )

        # Sorting players based on total runs
        sorted_players = sorted(
            rcb_playerwise_runs.items(), key=lambda x: x[1], reverse=True)
        top_10_rcb_batsmen_runs = dict(sorted_players[:10])

    # Plotting total runs by top 10 batsmen in RCB
    bar_plot(top_10_rcb_batsmen_runs, "Players", "Total Runs",
             "Total runs scored by top 10 batsmen of RCB over the history of IPL")
    plt.show()


plot_top_10_batsmen_rcb()  # invoking the new function
