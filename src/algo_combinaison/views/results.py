from src.algo_combinaison.controllers.tools import total_profit, total_cost


def display_benefit(most_profitable_combination: list) -> str:
    """
    Display the total total of pofit
    :param most_profitable_combination:
    :return: str
    """
    profit = total_profit(most_profitable_combination)
    print(f"Benefice de : {profit}€")


def display_total_cost(most_profitable_combination: list) -> str:
    """
    Display the total purchase price of the actions
    :param most_profitable_combination:
    :return:
    """
    total_purchases = total_cost(most_profitable_combination)
    print(f"Cout total : {total_purchases}€")
