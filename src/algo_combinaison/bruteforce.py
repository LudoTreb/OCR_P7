import psutil

from src.algo_combinaison.data_actions import WALLET, actions
from src.algo_combinaison.tools import display_mesure_script, display_graph


def brutforce(wallet: int, list_actions: list, best_combinaison=[]):
    """
    An algorithm that allows you to know which stocks to buy for a better return.
    Args:
        wallet: int - Maximun actions we can buy
        list_actions: list - A list of actions we can buy
        best_combinaison: list - A list of the most profitable actions

    Returns: list - the best combinaison of actions
    """
    if list_actions:
        candidate_combinaison_taken = brutforce(wallet, list_actions[1:], best_combinaison)

        sum_1 = sum([i.profit for i in candidate_combinaison_taken])

        act = list_actions[0]
        if act.cost <= wallet:
            candidate_combinaison_not_taken = brutforce(wallet - act.cost, list_actions[1:], best_combinaison + [act])
            sum_2 = sum([i.profit for i in candidate_combinaison_not_taken])

            if sum_1 < sum_2:
                return candidate_combinaison_not_taken

        return candidate_combinaison_taken

    else:
        return best_combinaison


print(f"{' Algo brutforce ':=^25}")
display_mesure_script(brutforce, WALLET, actions)

cpu = psutil.cpu_percent(4)
ram = psutil.virtual_memory()[2]

display_graph("Le CPU utilisé à :", cpu)
display_graph("Mémoire RAM utilisé à :", ram)
