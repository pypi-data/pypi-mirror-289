from collections import OrderedDict
from fwpods_py.classes.utils import utils


class swn_node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.pre = None
        self.post = None
        self.children = {}
        self.parent = None


class swn_tree_manager:
    """
    SWN tree manager class. This class is responsible for building and maintaining the SWN tree.
    Based on the SWN-tree section of the paper.
    """

    def __init__(self, root=None, tw=None):
        self.root = swn_node("root", 0) if root is None else root
        self.tail = []
        self.transaction_weights = tw

    def print_tree(self, node, level=0):
        """
        Prints the tree in a readable format.
        """
        print(
            "\t" * level, node.name, node.weight, "pre:", node.pre, "post:", node.post
        )
        for child in node.children:
            self.print_tree(node.children[child], level + 1)

    def print_tail_nodes(self):
        """
        Prints the tail nodes of the. Explanation on TAIL can be found in the swn tree section of the paper.
        """
        for t_name, node in self.tail.items():
            print(t_name, ":", node.name, node.weight)

    def get_tree(self):
        """
        Returns the tree aka the root node that contains the tree.
        """
        return self.root

    def build_tree(self, transactions, transact_weights, frequencies):
        """
        Builds the SWN tree from the window of transactions. Refer to the SWN tree construction section of the paper for more information.
        """
        for t_name, t_items in transactions.items():
            t_items = utils.sort_by_frequency(t_items, frequencies)
            self.__add_transaction(t_name, t_items, transact_weights)
        self.__generate_pre_post(self.root)
        return self.root

    def maintain_tree(self, inserted_transacts, transact_weights, frequencies):
        """
        Maintains the SWN tree by adding new transactions and removing the old ones. Refer to the SWN tree maintenance section of the paper for more information.
        """
        self.transaction_weights = (
            transact_weights
            if self.transaction_weights is None
            else self.transaction_weights
        )
        for t_name, t_items in inserted_transacts.items():
            t_items = utils.sort_by_frequency(t_items, frequencies)
            self.__add_transaction(t_name, t_items, self.transaction_weights)
        self.__generate_pre_post(self.root)
        self.__remove_from_tail(len(inserted_transacts))
        return self.root

    def __remove_from_tail(self, num_elems):
        """
        Part of the SWN tree maintenance. Removes the transactions from the tail of the SWN tree.
        """
        for _ in range(num_elems):
            tw, f_node = self.tail.pop(0)
            n = f_node.parent
            while True:
                if n is None:
                    break
                n.weight -= tw
                if n.weight == 0:
                    temp = n.parent.children.pop(n.name)
                    del n
                    n = temp
                else:
                    n = n.parent
                if n == self.root:
                    break
            del f_node
            return self.root

    def __generate_pre_post(self, node):
        self.__generate_pre_order(node, 0)
        self.__generate_post_order(node, 0)

    def __generate_pre_order(self, node, counter):
        node.pre = counter
        counter += 1
        for child in node.children:
            counter = self.__generate_pre_order(node.children[child], counter)
        return counter

    def __generate_post_order(self, node, counter):
        for child in node.children:
            counter = self.__generate_post_order(node.children[child], counter)
        node.post = counter
        counter += 1
        return counter

    def __add_transaction(self, t_name, t_items, t_weight_table):
        """
        The core part of the SWN tree construction. Inserts a single transaction to the SWN tree.
        Refer to the SWN tree construction section of the paper for more information.
        """
        # Functions the same way as the recursive method
        # But utilizing a node pointer instead of subtracting the item from the transaction
        current_node = self.root
        tw = 0
        for item in t_items:
            tw = t_weight_table[t_name]["weight"]
            if item in current_node.children:
                current_node = current_node.children[item]
                current_node.weight += tw
            else:
                new_node = swn_node(item, tw)
                new_node.parent = current_node
                current_node.children[item] = new_node
                current_node = new_node
        self.tail.append((tw, current_node))
