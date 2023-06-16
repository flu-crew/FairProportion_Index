def AnnotateTree(treed,annot_list):
    """
    :param treed: input dendropy tree
    :param annot_list: the list of fp values
    :return: an annotated nexus tree
    """
    i = 0
    for node in treed.postorder_node_iter():
        node.annotations["FP"] = annot_list[i]
        #node.annotations["i_n"] = 1
        if (annot_list[i] == float('inf') or annot_list[i] == float('-inf') or annot_list[i] == float('0') or annot_list[i] == None):
            node.annotations.clear()
           # node.annotations["i_n"]= 0
        i = i + 1

    treed.write(
        path="annotated_tree.nex",
        schema="nexus",
    )
