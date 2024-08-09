class utils:
    """
    Miscellaneous helper methods
    """

    def generate_elements_id(item_weights, counter):
        """
        Generates a lookup table for the elements in the weighted list. The lookup table is used to map the elements to their respective IDs.
        """
        lut = {}
        ret_counter = counter
        for item in item_weights:
            lut[item] = ret_counter
            ret_counter += 1
        return lut, ret_counter

    def sort_by_frequency(items, frequencies):
        """
        Sorts the items in a list by their frequency in descending order.
        """
        temp_dict = {}
        for item in items:
            temp_dict[item] = frequencies[item]
        return dict(sorted(temp_dict.items(), key=lambda x: x[1], reverse=True))

    def dbg(func):
        """
        A cheap debug printer lol
        """
        print(func)
        return func
