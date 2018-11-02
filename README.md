# To_make_your_life_easier
Tricks to avoid long manual command

Hadd_files.py = the output files from the grid will be allocated in many different folders. If you want to hadd together those histograms in only few files you can use the hadd command. This scripts takes all the files in subdirectory and hadd it together in another directory. Very helpful when you have ~200 000 files in ~200 different folders!

hadd_files.sh= same things then Hadd_files.py but to use if you only have few folder to add.

check_exit_status.py = when you fetch the output of the jobs you sent on the grid you will have a long list of out and err files that will tell you the results of your job. Now you don't want to check one by one the exit status of those jobs when they are more then 100 :D.  if they run ok the exit status will be 0 otherwise you want to collect the name of the out and err files that have an errors to check what went wrong. 

get_list_runandsub_filesthatchrushed.py = When you have a list of files that crushed and you want to strip the information from the file name to isolate run number and subrun and write it on another files

change_filename.py= Sometimes ROOT is boring and requires a lot of declaration of file names (like in a chain when you have to Add->). Since I am lazy, I use this script to write on a file all the filename in the right format to add them to a ROOT Chain, that then I just copy in my C++/ROOT script
