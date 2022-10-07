from src.algo_combinaison.controllers.tools import get_objets_from_csv
from src.algo_combinaison.models.models import Action

# path for the csv file
dataset_1 = "ress/data_anterieur/dataset1_Python+P7.csv"
dataset_2 = "ress/data_anterieur/dataset2_Python+P7.csv"

# actions list for the optimized algo
dataset_1_actions = get_objets_from_csv(dataset_1)
dataset_2_actions = get_objets_from_csv(dataset_2)

# actions list for the bruteforce algo
action_1 = Action("Action-1", 20, 5)
action_2 = Action("Action-2", 30, 10)
action_3 = Action("Action-3", 50, 15)
action_4 = Action("Action-4", 70, 20)
action_5 = Action("Action-5", 60, 17)
action_6 = Action("Action-6", 80, 25)
action_7 = Action("Action-7", 22, 7)
action_8 = Action("Action-8", 26, 11)
action_9 = Action("Action-9", 48, 13)
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

# test with list of tuple
actions_2 = [
    ("Action-1", 20, 5), ("Action-2", 30, 10), ("Action-3", 50, 15), ("Action-4", 70, 20),
    ("Action-5", 60, 17), ("Action-6", 80, 25), ("Action-7", 22, 7), ("Action-8", 26, 11),
    ("Action-9", 48, 13), ("Action-10", 34, 27), ("Action-11", 42, 17), ("Action-12", 110, 9),
    ("Action-13", 38, 23), ("Action-14", 14, 1), ("Action-15", 18, 3), ("Action-16", 8, 8),
    ("Action-17", 4, 12), ("Action-18", 10, 14), ("Action-19", 24, 21), ("Action-20", 114, 18)
]
