import psutil

from src.algo_combinaison.data_actions import WALLET, actions
from src.algo_combinaison.tools import display_mesure_script, display_graph


def brutforce(wallet: int, actions: list, best_combinaison=[]):
    """
    An algorithm that allows you to know which stocks to buy for a better return.
    It will test all the possibilities?
    Args:
        wallet: int Maximun actions we can buy
        actions: list A list of actions we can buy
        best_combinaison: list A list of the most profitable actions

    Returns: list best_combinaison

    """
    if actions:
        best_combinaison_1 = brutforce(wallet, actions[1:], best_combinaison)

        sum_1 = sum([i.profit for i in best_combinaison_1])

        act = actions[0]
        if act.cost <= wallet:
            best_combinaison_2 = brutforce(wallet - act.cost, actions[1:], best_combinaison + [act])
            sum_2 = sum([i.profit for i in best_combinaison_2])

            if sum_1 < sum_2:
                return best_combinaison_2

        return best_combinaison_1

    else:
        return best_combinaison


print("Algo brutforce")
display_mesure_script(brutforce, WALLET, actions)
cpu = psutil.cpu_percent(4)
ram = psutil.virtual_memory()[2]
display_graph("Le CPU utilisé à :", cpu)
display_graph("Mémoire RAM utilisé à :", ram)
