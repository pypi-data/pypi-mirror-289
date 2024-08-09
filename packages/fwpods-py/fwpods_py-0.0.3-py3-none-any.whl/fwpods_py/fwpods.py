from orderedset import OrderedSet as OSet


class ppw_code:
    def __init__(self, pre, post, weight):
        self.pre = pre
        self.post = post
        self.weight = weight


class fwpods:
    """
    The core FWPODS Algorithm itself, as described in Bui et al. (2021) doi: 10.1109.
    """

    def __init__(self, swn_tree, min_ws, items_ws, ttw=1):
        self.swn_tree = swn_tree
        self.min_ws = 0 if min_ws is None else min_ws
        self.ttw = float(ttw)
        self.wn_list = []
        self.fwps = []
        self.items_ws = items_ws

    def find_fwps(self, one_freq_items):
        """
        Recursively mines the WN list to find FWPs

        Input data: a WN list of 1-frequent weighted patterns filtered by min_ws (self.wn_list)
        (OrderedSet([item1, item2, item3]): [ppw_code(pre, post, weight), ppw_code,...])

        Output data: This function does not return anything, but the fwps can be accessed through the self.fwps list
        """
        for i in range(len(one_freq_items) - 1, 0, -1):
            i_next = []
            for j in range((i - 1), -1, -1):
                res_wl = self.wl_intersection(one_freq_items[i], one_freq_items[j])

                if self.get_ws(res_wl) >= self.min_ws:
                    self.fwps.append(res_wl)
                    i_next.append(res_wl)
            if len(i_next) != 0:
                self.find_fwps(i_next)

    def wl_intersection(self, wl1, wl2):
        """
        Intersects two WN-lists, see Section 4.1 - Bui et al. (2017) doi: 10.1016.

        Input data: two weighted lists (wl1, wl2) in the form of a tuple
        (items, [ppw_code(pre, post, weight), ppw_code,...])

        Output data: a new weighted list (wl3) in the same format as wl1 and wl2
        (items, [ppw_code(pre, post, weight), ppw_code,...])
        """
        wl3_items = wl1[0].union(wl2[0])
        wl3 = (wl3_items, [])
        sum = self.get_ws(wl1) + self.get_ws(wl2)

        wl1_list = wl1[1]
        wl2_list = wl2[1]
        m = len(wl1_list)
        n = len(wl2_list)
        k = -1
        i = 0
        j = 0
        while i < m and j < n:
            if wl2_list[j].pre < wl1_list[i].pre:
                if wl2_list[j].post > wl1_list[i].post:
                    if k > -1 and wl2_list[j].pre == wl3[1][k].pre:
                        wl3[1][k].weight += wl1_list[i].weight
                    else:
                        wl3[1].append(
                            ppw_code(
                                wl2_list[j].pre, wl2_list[j].post, wl1_list[i].weight
                            )
                        )
                        k += 1
                    i += 1
                else:
                    sum -= wl2_list[j].weight
                    j += 1
            else:
                sum -= wl1_list[i].weight
                i += 1
            if sum < self.min_ws:
                return wl3
        return wl3

    def get_ws(self, wl):
        """
        Calculates the weighted support of a weighted list. Since an item or an intersected one already contains its own transaction weights,
        the weighted support is calculated similarly to that in the initial steps. See Theorem 3 - Bui et al. (2017) doi: 10.1016.

        Input data: a weighted list (wl) in the form of a tuple
        (items, [ppw_code(pre, post, weight), ppw_code,...])
        """
        return sum([ppw.weight for ppw in wl[1]]) / self.ttw

    def print_fwps(self):
        """
        Prints the calculated FWPS
        """
        for fwp in self.fwps:
            print(f"{fwp[0]}: {[(ppw.pre, ppw.post, ppw.weight) for ppw in fwp[1]]}")

    def generate_wn_list(self, node):
        """
        Scan the SWN tree to generate the 1-frequent weighted patterns WN-list, which satisfies the min_ws constraint

        Input data: the root node of the SWN tree, created using the SWN tree manager (swm_tree_manager)
        """
        stack = []
        wnl = {}
        stack.append(node)
        root = node
        while stack:
            current_node = stack.pop()
            for child in current_node.children:
                stack.append(current_node.children[child])
            if current_node != root:
                if self.items_ws[current_node.name] >= self.min_ws:
                    if current_node.name not in wnl:
                        wnl[current_node.name] = [
                            ppw_code(
                                current_node.pre, current_node.post, current_node.weight
                            )
                        ]
                    else:
                        wnl[current_node.name].append(
                            ppw_code(
                                current_node.pre, current_node.post, current_node.weight
                            )
                        )
        return wnl

    def run(self):
        """
        Simply aggregates the functions to mine FWPs or running the FWPODS algorithm
        """
        temp = self.generate_wn_list(self.swn_tree.get_tree())
        self.wn_list.clear()
        self.wn_list = [(OSet([k]), v) for k, v in temp.items()]
        self.find_fwps(self.wn_list)
