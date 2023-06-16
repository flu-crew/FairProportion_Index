import numpy as np
from Bio import Phylo
import csv

from PostProcess import AnnotateTree

def getFP(tree,node):
    """
    Computes the FP index on a tree for a given node
    :param tree: a rooted phylogeny
    :param node: the node for which the index is to be computed
    :return: FP index value
    """
    path = tree.get_path(node)# gets the list of nodes in path from root(excludin) to node
    no_nodes = len(path) # gets the number of nodes on the path
    val1 = tree.distance(tree.root,path[0])/path[0].count_terminals()## this is the lenth of edge from the root to the firt node in the path to node, divided by the number of clades descendent from that edge
    val2 = 0
    # loop below gets the length off all edges in the path from root(excluding edge from root) to node and divides the
    for i in range(no_nodes-1,0,-1):
        val2+= path[i].branch_length/path[i].count_terminals()

    return(val1+val2)


def getAllFP(tree):
    """
    Computes the FP index for all nodes on a tree
    :param tree: a rooted phylogeny
    :return: a  sorted dictionary with FP of all nodes-- ascedning order
    """
    FP_Dict = {}
    FP_list = []
    post_order_nodes = list(tree.find_clades(order='postorder'))
    terminals = tree.get_terminals()
    for node in terminals:
        FP_Dict[node.name] = getFP(tree, node)

    for node in post_order_nodes:
        if node in terminals:
            FP_list.append(FP_Dict[node.name])
        else:
            FP_list.append(None)

## now sort the dictionary
    keys = list(FP_Dict.keys())
    n = len(keys)
    values = list(FP_Dict.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
## write dict to a file now
    toCSV(FP_Dict)

    return (sorted_dict, FP_list)

def getMinkFP(tree,k):
    """
    returns a list of k min fp indices from list
    :param tree: a rooted phylogeny
    :param k: input integer for the number of mins
    :return: a list of k min FP indices from list
    """
    fp_dict = getAllFP(tree)
    minl = list(fp_dict[0].items())[:k]

    file = open('min_list.txt', 'w')
    for item in minl:
        file.write(str(item))
        file.write("\n")
    file.close()

    return minl

def getMaxkFP(tree,k):
    """
    returns a list of k min fp indices from list
    :param tree:
    :param k:
    :return:
    """
    fp_dict = getAllFP(tree)
    keys = list(fp_dict[0].keys())
    n = len(keys)
    keys = list(fp_dict[0].keys())
    maxl = list(fp_dict[0].items())[n-k:n]
    maxl.reverse()
    file = open('max_list.txt', 'w')

    for item in maxl:
        file.write(str(item))
        file.write("\n")
    file.close()

    return maxl

def toCSV(tree_dict):
    import csv
    csv_columns = ['Name','FP']
    dict_data = tree_dict
    csv_file = "Fp_list.csv"
    try:
        with open('FP_list.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in tree_dict.items():
                writer.writerow([key, value])
    except IOError:
        print("I/O error")


