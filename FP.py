import argparse

from ImplFunc import base, minFP, maxFP
from FPMethods import getFP
from FPMethods import getAllFP
from FPMethods import getMaxkFP

def Main():

 ap = argparse.ArgumentParser(description='Compute FP index on a given nexus tree')
 ap.add_argument("-fpmin", help="Computes Min FP clades", action="store_true")
 ap.add_argument("-fpmax", help="Computes Max FP clades", action="store_true")



 ap.add_argument("filename",help = "nexus file treename",type=str)
 ap.add_argument("kval", help="input k", type=int)

 args = ap.parse_args()
 init = base(args.filename,args.kval)

 if args.fpmin:
     minFP(init[0],init[1],init[2],init[3],)

 if args.fpmax:
     maxFP(init[0], init[1], init[2], init[3])


if __name__ == '__main__':
  Main()













