#!/bin/env python

import os, sys
import subprocess
import string

def print_usage():
    print "Usage: Hadd_file.py"

if not __name__=='__main__':
    print "This script should be run from the terminal."
    print_usage()
    sys.exit(1)
#main directory where your files are (in subdirectory)
mainDir = '/pnfs/nova/users/crisprin/crisprin_DDupmu_Bckg_AboveHorizon101520_COMBOTOT_isgood_prod4_4Oct2018/'
#output directory where you want your files to be
cdDir   = '/nova/ana/users/crisprin/Eval_S17-10-30/root/UpMubkg/'
#refer to paths regardless of the script location: 
#abspath returns absolute path of a path
#expanduser return the argument with an initial component of ~ or ~user replaced by that user’s home directory
os.chdir(os.path.abspath(os.path.expanduser(cdDir)))

#list of files in each directory that you want to put together
output = [dI for dI in os.listdir(mainDir) if os.path.isdir(os.path.join(mainDir,dI))]
for item in output:
    filename = 'ddupmu_bkg_'+str(item)+'_15oct2018.root'
    #command that you want to run
    comsam = "hadd "+str(filename)+" `pnfs2xrootd /pnfs/nova/users/crisprin/crisprin_DDupmu_Bckg_AboveHorizon101520_COMBOTOT_isgood_prod4_4Oct2018/"+str(item)+"/*/*.root` "
    print (comsam)
    #Execute shell commands
    os.system(comsam)

