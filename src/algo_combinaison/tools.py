import time


def display_best_combination(actions: list) -> str:
    """
    Display all the most profitable actions, their cost and their total profit
    Args:
        actions: list A list of the most rentable actions

    Returns: str

    """
    print("=" * 25)
    for action in actions:
        print(action)
    print("-" * 25)
    total_purchases = round(sum(i.cost for i in actions), 2)
    profit = round(sum(i.profit for i in actions), 2)
    print(f"Cout total : {total_purchases}€")
    print(f"Benefice de : {profit}€")
    print("=" * 25)


def display_mesure_script(function, wallet: int, actions: list) -> str:
    """
    Display the time it took the algorithm to find the most profitable list of actions to buy.
    Args:
        function: function
        wallet: int Maximun actions we can buy
        actions: list A list of actions we can buy

    Returns: str

    """
    start_time = time.time()
    result = function(wallet, actions)
    display_best_combination(result)
    print(f"temps de calcul : {round(time.time() - start_time, 4)}sec")


def display_graph(message: str, data: int, bar_graph=[]) -> str:
    """

    Args:
        message:
        data:
        bar_graph:

    Returns:

    """
    bar_graph.clear()
    print(f"\n{message}")
    for i in range(0, round(data * 0.25)):
        bar_graph.append("🀫")
    for i in range(round(data * 0.25), 25):
        bar_graph.append("🀆")
    print(f"{''.join(bar_graph)} {data}%")
