#!/usr/bin/env Python

import sys
import os
import os.path

import subprocess

import tempfile
import math

import re
from optparse import OptionParser

                       
#### the main function starts here... 
def main(argv):
    global verbose, G, number_of_nodes, deadline, prices
    usage = "usage: %prog options name"
    parser = OptionParser(usage)
    parser.set_defaults(runs=1, iters=1)
    parser.add_option("-a", "--alg",   dest="alg", help="specify the algorithm", type="string", default="")
    parser.add_option("-d", "--dir",   dest="dir", help="specify input directory", type="string", default="input")
    parser.add_option("-g", "--graph",  dest="graph", help="graph type in size", type="int", default=24)
    parser.add_option("-p", "--perc",  dest="perc", help="start cp percentage deadline", type="int", default=100)
    parser.add_option("-s", "--pstop",  dest="pstop", help="stop cp percentage deadline", type="int", default=-1)
    
    (options, args) = parser.parse_args()

    if options.alg:
      #for pval in xrange(options.perc,options.pstop,-1):
      for pval in xrange(options.perc,options.pstop,-10):
        valid = 0
        invalid = 0
        failed = 0
        for i in xrange(1,5):
           for j in xrange(1,6):
             ifile = str(i)+'.'+str(options.graph)+'.'+str(j)
             #cmd = 'python '+options.alg+' -d'+options.dir+' -i '+ifile+' -p '+str(options.perc)
             #print cmd
             start_cost = 0
             final_cost = 0
             
             subargs = ['python',options.alg,'-d',options.dir,'-i',ifile,'-p',str(pval)]

             print subargs
             p = subprocess.Popen(subargs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

             non_inst_nodes = 0
             new_deadline = 0
             for line in p.stdout.readlines():
               #print line
               if line.startswith( 'start configuartion: cost=' ):
                 tmp0 = line.split(" ")
                 start_cost = int(tmp0[2][5:])
               elif line.startswith( 'final configuration: cost=' ):
                 tmp0 = line.split(" ")
                 final_cost = int(tmp0[2][5:])
                   
                 if start_cost == final_cost:
                    failed = failed + 1
                    print 'start_cost='+str(start_cost)+' final_cost='+str(final_cost),"failed"
                 elif final_cost>start_cost:
                    failed = failed + 1
                    print 'start_cost='+str(start_cost)+' final_cost='+str(final_cost),"valid??"
                 else:
                    valid = valid + 1
                    print 'start_cost='+str(start_cost)+' final_cost='+str(final_cost),"valid"
               elif line.startswith( '**** Invalid final configuration ****' ):
                  invalid = invalid + 1  
                  print 'start_cost='+str(start_cost)+' final_cost='+str(start_cost),"invalid"
             p.communicate()

        score = float(valid )/float(invalid+failed+valid)
        print "\nfinal result p="+str(pval)+" : invalid="+str(invalid),"failed="+str(failed),"valid="+str(valid),"score="+str(round(score,3))
    else:
        sys.exit("\nERROR - Missing option -a or --alg.\n")
    
#############################
# The program starts here...
#############################
if __name__ == '__main__':
         
     main(sys.argv[1:])
        
#############################
# end of the program
#############################
    
