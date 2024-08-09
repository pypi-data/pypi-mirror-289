from collections import OrderedDict
from datetime import datetime

from fwpods_py.weights_manager import weights_manager
from fwpods_py.swn_tree_manager import swn_node, swn_tree_manager
from fwpods_py.fwpods import fwpods


class window_manager:
    """
    This is the heart of the algorithm, as it runs and manages the FWPoDS algorithm, over a continuous stream of transactions.

    The following manager class is a provided sample implementation of a window manager for the algorithm.
    You can bring your own implementation or use this one as a reference to implement your own in your own framework/database, etc.
    As long as it contains the following procedures:
    - Initialize the weights manager, SWN tree manager, and the FWPoDS algorithm, on a full window.
    - Do nothing if the window size is not reached.
    - Or update the above structures if the inserted transaction overflows the window size.
    , And structures:
    - The input has to remain simple, takes in only a single transaction entry at a time.
    """

    def __init__(self, initial_transactions, window_size, panel_size, min_ws):
        self.window_size = window_size
        self.panel_size = panel_size

        self.swn_tree = swn_tree_manager()
        self.weights_manager = weights_manager()
        self.min_ws = min_ws

        self.fwps = []
        self.window = OrderedDict()
        self.initial_transactions = initial_transactions

        self.items_freq = {}
        self.ws = {}

        self.tree_build_time = []
        self.total_runtime = []
        self.algo_runtime = []

    def update_transaction(self, t_name, t_items):  # Observer pattern wrapper
        self.add_transaction(t_name, t_items)

    def update_weight(self, item, weight):
        self.weights_manager.update_item_weight(item, weight)

    def new_weights(self, new_items_weights):
        self.weights_manager.items_weight = new_items_weights

    def add_transaction(self, t_name, t_items):
        self.window[t_name] = t_items

        if len(self.window) == self.window_size:
            stamp = datetime.now()
            self.weights_manager.init_db(self.window, self.weights_manager.items_weight)
            self.weights_manager.calculate_ttw()
            self.weights_manager.calculate_items_ws()
            self.fwps = []

            for _, t_items in self.window.items():
                self.__get_items_freq(t_items)

            tree_stamp = datetime.now()
            self.swn_tree.build_tree(
                self.window, self.weights_manager.transaction_weights, self.items_freq
            )
            self.tree_build_time.append(datetime.now() - tree_stamp)

            fwp = fwpods(
                self.swn_tree,
                self.min_ws,
                self.weights_manager.items_ws,
                self.weights_manager.ttw,
            )

            algo_stamp = datetime.now()
            fwp.run()
            self.algo_runtime.append(datetime.now() - algo_stamp)

            self.fwps = fwp.fwps
            self.total_runtime.append(datetime.now() - stamp)

        if len(self.window) > self.window_size:
            stamp = datetime.now()
            self.window.popitem(last=False)
            self.weights_manager.add_transaction(t_name, t_items)
            self.weights_manager.remove_head_transaction()
            self.weights_manager.calculate_ttw()
            self.weights_manager.calculate_items_ws()

            tree_stamp = datetime.now()
            for _, t_items in self.window.items():
                self.__get_items_freq(t_items)

            self.swn_tree.maintain_tree(
                self.window, self.weights_manager.transaction_weights, self.items_freq
            )
            self.tree_build_time.append(datetime.now() - tree_stamp)

            fwp = fwpods(
                self.swn_tree,
                self.min_ws,
                self.weights_manager.items_ws,
                self.weights_manager.ttw,
            )

            algo_stamp = datetime.now()
            fwp.run()
            self.algo_runtime.append(datetime.now() - algo_stamp)

            self.fwps = fwp.fwps
            self.total_runtime.append(datetime.now() - stamp)
        return

    def __get_items_freq(self, items):
        for item in items:
            if item in self.items_freq:
                self.items_freq[item] += 1
            else:
                self.items_freq[item] = 1
