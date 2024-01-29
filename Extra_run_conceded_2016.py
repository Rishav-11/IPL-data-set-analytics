import csv
import matplotlib.pyplot as plt
from functions import bar_plot


def get_match_ids_of_a_year(year: str, matches_csv: str):
    ''' function to get match ids of a specific year'''

    with open(matches_csv, encoding="utf-8") as inputfile:
        matches_reader = csv.DictReader(inputfile)
        match_ids_of_year = []

        for match in matches_reader:
            if match['season'] == year:
                match_ids_of_year.append(match['id'])

    return match_ids_of_year


def plot_extra_runs_2016():
    ''' function to get data and plot extra runs conceded per team in the year 2016'''
    match_ids_of_2016 = get_match_ids_of_a_year("2016", "matches.csv")

    # ... (existing code)

    # get required data from csv in dict and then call appropriate plot functions
    with open('deliveries.csv', encoding="utf-8") as inputfile:
        extra_runs_in_2016 = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            if delivery['match_id'] in match_ids_of_2016:
                extra_runs_in_this_ball = int(delivery['extra_runs'])
                extra_runs_in_2016[delivery['bowling_team']] = (
                    extra_runs_in_2016.get(delivery['bowling_team'], 0)
                    + extra_runs_in_this_ball
                )

    # Plotting extra runs conceded per team in the year 2016
    bar_plot(extra_runs_in_2016, "Team", "Total Extra Runs",
             "Extra runs conceded per team in the year 2016")
    plt.show()


plot_extra_runs_2016()  # invoking the new function
