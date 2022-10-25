import csv

WALLET = 500  # maximun list_actions we can buy


class Action:
    def __init__(self, name, cost, profit_rate):
        """
        Initiate an action
        :param name: str
        :param cost: int
        :param profit_rate: int
        """
        self.name = name
        self.cost = cost
        self.profit_rate = profit_rate
        self.profit = self.calcul_profit()

    def __repr__(self):
        return f"{self.name} - {self.cost}€ - {self.profit_rate}%"

    def calcul_profit(self):
        profit = round((self.cost * self.profit_rate / 100), 2)
        return profit


def get_objects_from_csv(csv_path: str) -> list:
    """
    Create a list of Action objet from a csv file
    :param csv_path: str
    :return list_actions: list
    """
    actions = []
    with open(csv_path, newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for name, cost, profit in reader:
            if round(float(cost)) > 0:
                actions.append(Action(name, round(float(cost)), float(profit)))

        return actions


# path for the csv file
directory = "/Users/ludovic.trebalag/Documents/DA-Python/Projet-07/"
dataset_1 = directory + "ress/data_anterieur/dataset1_Python+P7.csv"
dataset_2 = directory + "ress/data_anterieur/dataset2_Python+P7.csv"

# list_actions list for the optimized algo
dataset_1_actions = get_objects_from_csv(dataset_1)

dataset_2_actions = get_objects_from_csv(dataset_2)

# list_actions list for the bruteforce algo
action_1 = Action("Action-01", 20, 5)
action_2 = Action("Action-02", 30, 10)
action_3 = Action("Action-03", 50, 15)
action_4 = Action("Action-04", 70, 20)
action_5 = Action("Action-05", 60, 17)
action_6 = Action("Action-06", 80, 25)
action_7 = Action("Action-07", 22, 7)
action_8 = Action("Action-08", 26, 11)
action_9 = Action("Action-09", 48, 13)
action_10 = Action("Action-10", 34, 27)
action_11 = Action("Action-11", 42, 17)
action_12 = Action("Action-12", 110, 9)
action_13 = Action("Action-13", 38, 23)
action_14 = Action("Action-14", 14, 1)
action_15 = Action("Action-15", 18, 3)
action_16 = Action("Action-16", 8, 8)
action_17 = Action("Action-17", 4, 12)
action_18 = Action("Action-18", 10, 14)
action_19 = Action("Action-19", 24, 21)
action_20 = Action("Action-20", 114, 18)

actions = [
    action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9, action_10,
    action_11, action_12, action_13, action_14, action_15, action_16, action_17, action_18, action_19, action_20
]
