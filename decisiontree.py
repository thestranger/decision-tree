from process_data import compile_data

# Splits data by an attribute into 2 new sets of data
# returns (data_matching_attribute, data_not_matching)


def split_data(data, attribute_index, attribute_val):
        return ([datum for datum in data
                 if datum[attribute_index] == attribute_val],
                [datum for datum in data
                 if datum[attribute_index] != attribute_val])


def count_positives(data, dvs_should_be):
    return len([datum for datum in data
                if datum[-1] in dvs_should_be])


def gini(data, dvs_should_be):
    num_records = len(data)
    positives = float(count_positives(data, dvs_should_be))
    return 1 - (positives/num_records)**2 - ((num_records - positives)/num_records)**2


class Node(object):
    """Representation for node in decision tree"""
    def __init__(self, records=None, attribute_index=None,
                 attribute_val=None, yes_node=None, no_node=None):
        super(Node, self).__init__()
        self.records = records
        self.attribute_index = attribute_index
        self.attribute_val = attribute_val
        self.yes_node = yes_node
        self.no_node = no_node


data = compile_data('data.dat')
print gini(data, ['5'])
