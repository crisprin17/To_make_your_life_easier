#!/usr/bin/env python
import sys
import re

def print_usage():
    print "Usage: get_list_runandsub_filesthatchrushed.py"
    
filename = open("/nova/app/users/crisprin/python/filetthatcrushed.txt","r+")
flines = filename.readlines()
outfilename = open("/nova/app/users/crisprin/python/filetthatcrushed_ListofrunandSubrun.txt","wb")
for i in range(len(flines)): 
    if flines[i].startswith("crisprin"):
        text = str(flines[i-2])   
        ext = "fardet"
        a = text[text.find(ext):]
        run1 = a.split('_')[1:2]
        run = str(run1).lstrip('[\'r000').rstrip('\']')
        sub1 = a.split('_')[2:3]
        sub = str(sub1).lstrip('[\'s').rstrip('\']')
        outfilename.write(str(run)+' '+str(sub)+'\n')
filename.close()
outfilename.close()
