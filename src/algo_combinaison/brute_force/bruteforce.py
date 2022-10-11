from src.algo_combinaison.data_actions import WALLET, actions, actions_test_tuple

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


def brut_force_recursive_1(wallet, actions, best_combi=[]):
    if actions:
        combi_1, combis_1 = brut_force_recursive_1(wallet, actions[1:], best_combi)
        act = actions[0]
        if act.cost <= wallet:
            combi_2, combis_2 = brut_force_recursive_1(wallet - act.cost, actions[1:], best_combi + [act])

            if combi_1 < combi_2:
                return combi_2, combis_2
        return combi_1, combis_1
    else:
        return sum([i.cost for i in best_combi]), best_combi


def brut_force_recursive_tuple(capacite, elements, elements_selection=[]):
    if elements:
        val1, lstVal1 = brut_force_recursive_tuple(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = brut_force_recursive_tuple(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return round(sum([i[1] * i[2] / 100 for i in elements_selection]), 2), 500 - capacite


def brut_force_recursive(wallet: int, actions: list, n):
    if n == 0 or wallet == 0:
        return 0
    if actions[n - 1].cost > wallet:
        return brut_force_recursive(wallet, actions, n - 1)
    else:
        return actions[n - 1].cost, brut_force_recursive(wallet - actions[n - 1].profit_rate, actions, n - 1),
        brut_force_recursive(wallet, actions, n - 1)


print("Algo brute_force sans recursivité avec liste d'objet : ")
brute_force(WALLET, actions)

print("\nAlgo brute_force avec recursivité et liste d'objet : ")
display_total_cost(brut_force_recursive_1(WALLET, actions)[1])
display_benefit(brut_force_recursive_1(WALLET, actions)[1])

print("\nAlgo brute_force avec recursivité avec liste de tuple : ")
result = brut_force_recursive_tuple(WALLET, actions_test_tuple)
print(f"Cout total : {result[1]}€ \nBenefice de : {result[0]}")


