from Bio import Phylo
import dendropy


from FPMethods import getMinkFP, getMaxkFP, getAllFP
from PostProcess import AnnotateTree

def base(tree,k):
    t1 = Phylo.read(tree, "nexus")
    o_tree= dendropy.Tree.get(path=tree, schema="nexus")
    allfp = getAllFP(t1)
    return(t1,o_tree,k,allfp[1])
def AllFP(t1,o_tree):
    allfp= getAllFP(t1)
    AnnotateTree(o_tree,allfp[1])

def minFP(t1,o_tree,k,fplist):
    minfp= getMinkFP(t1,k)
    AnnotateTree(o_tree,fplist)

def maxFP(t1,o_tree,k,fplist):
    maxfp= getMaxkFP(t1,k)
    AnnotateTree(o_tree,fplist)







#x=getAllFP(tree)
#print(x[0])
#getMinkFP(tree,10)