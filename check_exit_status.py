#!/usr/bin/env python                                                                             
                                               
import sys
import re

def print_usage():
    print "Usage: check_exit_status.py"


filepath ="path/"
filename_er = "file_name"
filename_out = "file_name"
filename_original = "file_name"
#when you fetch the output of the jobs you sent on the grid you will have a long list of out and err file that will tell 
#you the results of your job. if they run ok the exit status will be 0.                                                  
outfilenameERR = open(filepath+filename_er,"wb")
outfilenameOUT = open(filepath+filename_out,"wb")
#files containin information about the exit status from two kind of files .err and .out
with open(filepath+filename_original, "r+") as f1:
    for name in f1:
        #take only the value of the exit status
        status = name.split(' ')[-1]
        #if the exit status is different from zero... we have an issue!
        if (int(status) is not 0):
            if ".err" in name:
                outfilenameERR.write(str(name)+'\n')
            else:
                outfilenameOUT.write(str(name)+'\n')

f1.close()
outfilenameERR.close()
outfilenameOUT.close()
