import csv
import matplotlib.pyplot as plt
from functions import bar_plot


def top_ten_economy_bowlers():
    with open('deliveries.csv', 'r', newline='') as input_file:
        deliveries_reader = csv.DictReader(input_file)

        bowlers = {}

        for delivery in deliveries_reader:
            if 'match_id' in delivery and 518 <= int(delivery['match_id']) <= 576:
                bowler = delivery['bowler']
                runs_by_bowler = int(delivery['total_runs'])
                overs_by_bowler = float(delivery['over'])

                if bowler not in bowlers:
                    bowlers[bowler] = {
                        'run': runs_by_bowler, 'overs': overs_by_bowler}

                else:
                    bowlers[bowler]['run'] += runs_by_bowler
                    bowlers[bowler]['overs'] += overs_by_bowler

        for bowler in bowlers:
            economy_rate = (bowlers[bowler].get(
                'run') / bowlers[bowler].get('overs'))
            bowlers[bowler]['economy_rate'] = economy_rate

        sorted_bowlers = sorted(
            bowlers.items(), key=lambda x: x[1]['economy_rate'], reverse=False)
        top_ten_bowlers = sorted_bowlers[:10]
        bowlers = [b[0] for b in top_ten_bowlers]
        economy_rates = [b[1]['economy_rate'] for b in top_ten_bowlers]

        plt.bar(bowlers, economy_rates, color='g',
                width=0.5, label='Top 10 Economical Bowlers')
        plt.xlabel('Bowlers Name')
        plt.ylabel('Economy Rates of each bowler')
        plt.title('Top 10 Economical Bowlers in 2015')
        plt.legend()
        plt.show()


top_ten_economy_bowlers()
