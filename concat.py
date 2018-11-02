#!/usr/bin/env python

def print_usage():
    print "Usage: run_file.py"


filename = open("/nova/app/users/crisprin/GENIE_relS17_10_30/AllFlavor_newROCKBOX.txt","r+")
print "----------------------1---------: "
flines = filename.readlines()
count = len(flines)
print "nova -c concat_files.fcl"
for j in range(1,len(flines)):
    try:
        print(" `pnfs2xrootd /pnfs/nova/users/crisprin/GENIE/tautau/AllFlavor/"+str(flines[j]).strip()+"`")
    except ValueError:
        break
       
filename.close()

