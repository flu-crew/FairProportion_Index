# Requirements
  * Python 3.7
 
# Packages Used
  * dendropy
  * Bio
  * scipy
  * numpy
  * argparse
  
# FP measures in the tool  
The statistic arguments are as follows:
- fpmin: minimum FP
- fpmax: maximum FP

# Tutorial
To run this tool on a nexus tree please follow the steps below:

1) place a nexus binary treefile in the same directory as the project
2) run FP.py with the following arguements: treename, (int)k, function (-fpmin,-fpmax)
  * example : FP.py t10.tre 3 -fpmax 
    The example above runs FP on the example treefile with 10 taxa and finds the 3 taxa with max fp in the tree.
    
    Note: the user can run multiple functions on the treefile, eg. pdstat.py treename.tre 10 -fpmax -fpmin
    
3) The output of the above command will be a file named "annotated_tree_nex" with all the the terminal clades annotated with their FP indec . This tree file can be opened with FigTree, and the nodes annotated using the "node labels" or "node shapes" menu. In addition, -fpmax returns max_list.txt i.e a txt file with the k max fp node names and values. The same is done for -fpmin with min_list.txt

Input test files with different numbers of input taxa are also present in the Test_Datasets directory
