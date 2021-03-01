#!/usr/bin/env python

def print_usage():
    print "Usage: run_file.py"

filepath ="path"
filename = open("file_name","r+")

print "----------------------1---------: "
flines = filename.readlines()
count = len(flines)
print "nova -c concat_files.fcl"
for j in range(1,len(flines)):
    try:
        print(" `pnfs2xrootd "+filepath+" "+str(flines[j]).strip()+"`")
    except ValueError:
        break
       
filename.close()

