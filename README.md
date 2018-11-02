# To_make_your_life_easier
Tricks to avoid long manual command

Hadd_files.py = the output files from the grid will be allocated in many different folders. If you want to hadd together those histograms in only few files you can use the hadd command. This scripts takes all the files in subdirectory and hadd it together in another directory. Very helpful when you have ~200 000 files in ~200 different folders!

check_exit_status.py = when you fetch the output of the jobs you sent on the grid you will have a long list of out and err files that will tell you the results of your job. Now you don't want to check one by one the exit status of those jobs when they are more then 100 :D.  if they run ok the exit status will be 0 otherwise you want to collect the name of the out and err files that have an errors to check what went wrong. 
