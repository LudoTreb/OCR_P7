import csv

from src.algo_combinaison.models.models import Action


def sorted_actions_by_profitability(actions: list) -> list:
    """
    Sort actions by their profit_rate
    :param actions: list
    :return: sorted_actions list
    """
    actions_sorted = sorted(actions, key=lambda action: action.profit_rate, reverse=True)
    return actions_sorted


def total_cost(actions: list) -> int:
    """
    The total purchase price of the actions
    :param actions: list
    :return total_price: int
    """
    purchases = []
    for i in actions:
        purchases.append(i.cost)
    total_cost = sum(purchases)
    return total_cost


def total_profit(actions: list) -> float:
    """
    The total of pofit
    :param actions: list
    :return total_profit: float
    """
    profits = [i.cost * i.profit_rate / 100 for i in actions]
    total_profit = round(sum(profits), 2)
    return total_profit


def get_objets_from_csv(csv_path: str) -> list:
    """
    Create a list of Action objet from a csv file
    :param csv_path: str
    :return actions: list
    """
    actions = []
    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for name, cost, profit in reader:
            actions.append(Action(name, cost, profit))
        return actions