import psutil

from src.algo_combinaison.data_actions import WALLET, actions
from src.algo_combinaison.tools import display_mesure_script, display_graph


def optimized(wallet: int, actions: list) -> list:
    """
    An algorithm that allows you to know which stocks to buy for a better return
    Args:
        wallet: int Maximun actions we can buy
        actions: list A list of actions we can buy

    Returns: list a list of the most rentable actions

    """

    matrice = [[0 for x in range(wallet + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):

        for w in range(1, wallet + 1):
            if actions[i - 1].cost <= w:
                matrice[i][w] = max(actions[i - 1].profit + matrice[i - 1][w - actions[i - 1].cost], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    w = wallet
    n = len(actions)
    best_combinaison = []

    while w >= 0 and n >= 0:
        action = actions[n - 1]
        if matrice[n][w] == matrice[n - 1][w - action.cost] + action.profit:
            best_combinaison.append(action)
            w -= action.cost
        n -= 1
    return best_combinaison


print("Algo optimized")
display_mesure_script(optimized, WALLET, actions)
cpu = psutil.cpu_percent(4)
ram = psutil.virtual_memory()[2]
display_graph("Le CPU utilisé à :", cpu)
display_graph("Mémoire RAM utilisé à :", ram)
