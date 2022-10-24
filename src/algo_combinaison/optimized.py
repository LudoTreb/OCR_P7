import psutil

from src.algo_combinaison.data_actions import WALLET, actions, dataset_1_actions, dataset_2_actions
from src.algo_combinaison.tools import display_mesure_script, display_graph


def optimized(wallet: int, actions: list) -> list:
    """
    An algorithm that allows you to know which stocks to buy for a better return.
    Args:
        wallet: int - Maximun list_actions we can buy
        actions: list - A list of list_actions we can buy

    Returns: list - a list of the most rentable list_actions
    """

    matrice = [[0 for x in range(wallet + 1)] for x in range(len(actions) + 1)]
    print(f"{len(actions)}\n {actions}")
    for i in range(1, len(actions) + 1):

        for capacity in range(1, wallet + 1):
            if actions[i - 1].cost <= capacity:
                matrice[i][capacity] = max(actions[i - 1].profit + matrice[i - 1][capacity - actions[i - 1].cost], matrice[i - 1][capacity])
            else:
                matrice[i][capacity] = matrice[i - 1][capacity]

    capacity = wallet
    n = len(actions)
    best_combinaison = []

    while capacity >= 0 and n >= 0:
        action = actions[n - 1]
        if matrice[n][capacity] == matrice[n - 1][capacity - action.cost] + action.profit:
            best_combinaison.append(action)
            capacity -= action.cost
        n -= 1
    return best_combinaison


print(f"{' Algo optimized ':=^25}")
display_mesure_script(optimized, WALLET, dataset_2_actions)

cpu = psutil.cpu_percent(4)
ram = psutil.virtual_memory()[2]

display_graph("Le CPU utilisé à :", cpu)
display_graph("Mémoire RAM utilisé à :", ram)