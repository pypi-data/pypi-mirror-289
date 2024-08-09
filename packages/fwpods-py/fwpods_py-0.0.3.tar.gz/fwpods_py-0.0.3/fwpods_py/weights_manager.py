from collections import OrderedDict


class weights_manager:
    """
    A custom helper class to manage the weights of items and transactions.
    This class is responsible for calculating the total transaction weight (ttw) and the weighted support of items (items_ws),
    as well as keeping track of the transactions weights, and items weights, along with other necessary data structures.
    """

    def __init__(self, initial_transactions=None, initial_items_weight=None):
        self.ttw = 0
        self.items_ws = {}  # {item: calculated_weighted_support}
        self.transaction_weights = OrderedDict()  # {tid: {item: [], weight: 00.00}}
        self.items_in_transact_lut = {}
        self.transactions = (
            {} if initial_transactions is None else initial_transactions
        )  # {tid: [items]}
        self.items_weight = {} if initial_items_weight is None else initial_items_weight

    def init_db(self, initial_transactions, initial_items_weight):
        """
        Initializes the database with the initial transactions and items weights, if provided.

        :param initial_transactions: A dictionary of transactions in the form of {tid: [items]}
        :param initial_items_weight: A dictionary of items weights in the form of {item: weight}
        """
        self.transactions = initial_transactions
        self.items_weight = initial_items_weight
        for t_name, t_items in self.transactions.items():
            self.add_transaction(t_name, t_items)
        self.calculate_ttw()
        self.calculate_items_ws()

    def add_transaction(self, t_name, t_items):
        """
        Adds a single transaction to the database, and updates the transaction weights, items in the lookup table, and the total transaction weight.

        :param t_name: The transaction name or ID
        :param t_items: The list of items in the transaction
        """
        tw = 0
        for item in t_items:
            tw += self.items_weight[item]
            if item in self.items_in_transact_lut:
                self.items_in_transact_lut[item].add(t_name)
            else:
                self.items_in_transact_lut[item] = set([t_name])
        self.transaction_weights[t_name] = {"items": t_items, "weight": tw}
        return self.transaction_weights[t_name]

    def remove_head_transaction(self):
        """
        Removes the first transaction from the database, and updates the items in the lookup table.

        :return: The removed transaction name and items
        """
        t_name = list(self.transaction_weights.keys())[0]
        t_items = self.transaction_weights[t_name]["items"]
        for item in t_items:
            if item in self.items_in_transact_lut:
                if t_name in self.items_in_transact_lut[item]:
                    self.items_in_transact_lut[item].remove(t_name)
        self.transaction_weights.pop(t_name)
        return t_name, t_items

    def update_item_weight(self, item, weight):
        """
        Update a single item's weight in the items weights dictionary.
        """
        self.items_weight[item] = weight

    def calculate_ttw(self):
        """
        Calculates the total transaction weight (ttw) by summing up all the transaction weights. Given that the transaction weights are already calculated.
        """
        self.ttw = sum([tw["weight"] for tw in self.transaction_weights.values()])
        return self.ttw

    def calculate_items_ws(self):
        """
        Calculates the weighted support of each 1-item in the database.Get the weighted support of each item in the database.
        """
        self.items_ws = {}
        for item, transact in self.items_in_transact_lut.items():
            self.items_ws[item] = (
                sum([self.transaction_weights[t]["weight"] for t in transact])
                / self.ttw
            )
        return self.items_ws
