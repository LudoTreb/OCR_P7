from src.algo_combinaison.models.data import actions
from src.algo_combinaison.models.constances import WALLET
from src.algo_combinaison.views.results import display_benefit, display_total_cost
from src.algo_combinaison.controllers.tools import sorted_actions_by_profitability

"""
Less contraintes :

Chaque action ne peut être achetée qu'une seule fois.

Nous ne pouvons pas acheter une fraction d'action.

Nous pouvons dépenser au maximum 500 euros par client.

"""

"""
Aglgoritme sorted_profitability(actions)

Debut
    sorted_actions_by_profitability = trie descendant des actions par profit_rate
Fin

Algorithme display_total_cost(most_profitable_combination)

Debut 
    total_cost = somme des couts des actions de la liste most_profitable_combination
    affiche "Cout total : {total_cost}"
Fin

Algorithme display_benefit(most_profitable_combination)

Debut 
    benefit = somme du rendement des actions de la liste most_profitable_combination
    affiche "Benefice de : {benefit}"
Fin


Aglgoritme bruteforce

Variable 
    wallet = 500 : INT
    action_purchase = 0 : INT
    most_profitable_combination = [] : LIST (liste de la combinaison d'action la plus rentable)
    actions = [action_1, action_2, ..., action_20] : LIST
    (une liste de dictionaire action_1 = {"cost": 20, "profit_rate": 5}) ???

Debut 
    sorted_actions_by_profitability(actions)
    Pour i dans actions:
        Si action_purchase >= wallet:
                break
        Fin Si
        Sinon:
            ajouter i à most_profitable_combination
            action_purchase = action_purchase + i["cost"]
        Fin Sinon
    Fin Pour 
    display_total_cost(most_profitable_combination)
    display_benefit(most_profitable_combination)
Fin

"""


def brute_force(wallet, actions):
    action_purchase = 0
    most_profitable_combinaison = []
    actions_sorted = sorted_actions_by_profitability(actions)
    for i in actions_sorted:
        if action_purchase + i.cost > wallet:
            break
        else:
            most_profitable_combinaison.append(i)
            action_purchase = action_purchase + i.cost

    display_total_cost(most_profitable_combinaison)
    display_benefit(most_profitable_combinaison)


def brute_force_2(actions, best_combinaisons = []):

    if actions:
        purchase = 0
        val_1 = brute_force_2(actions[1:], best_combinaisons)
        val = actions[0]

        if purchase < WALLET:
            purchase = purchase + val.cost
            val_2 = brute_force_2(actions[1:], best_combinaisons + [val])
            if val_1[0].cost < val_2[0].cost:
                return val_2
        return val_1
    else:
        return best_combinaisons

    display_total_cost(best_combinaisons)
    display_benefit(best_combinaisons)


brute_force(WALLET, actions)
# print(brute_force_2(actions))


