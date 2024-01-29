import csv
import matplotlib.pyplot as plt
from functions import bar_plot


def foreign_umpire_analysis():
    """Analyzes and plots the number of foreign umpires in IPL by country."""
    # String constants
    UMPIRE = "Country"
    TOT_NUMBER = "Total Numbers of Umpire"
    UMPIRES_GRAPH_TITLE = "Number of umpires in IPL by country (Non-Indians)"
    INDIA = "India"

    # File name
    CSV_FILE_PROB_3 = 'umpires.csv'

    # get required data from csv in dict and then call plot function
    with open(CSV_FILE_PROB_3, encoding="utf-8") as inputfile:
        country_wise_umpire = {}
        umpires_reader = csv.DictReader(inputfile)

        for umpire_info in umpires_reader:
            country_of_umpire = umpire_info[' country'].strip()
            if country_of_umpire != INDIA:
                country_wise_umpire[country_of_umpire] = (
                    country_wise_umpire.get(country_of_umpire, 0)
                    + 1
                )
        bar_plot(country_wise_umpire, UMPIRE, TOT_NUMBER, UMPIRES_GRAPH_TITLE)
        # show plot
        plt.show()


# Call the function to execute the analysis
foreign_umpire_analysis()
