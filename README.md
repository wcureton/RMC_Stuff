# makefolders3 for cluster job submission
_____________________________________________________________________________________________________
# General Purpose of makefolders3:#  to make cluster job submission easier by automating the process of
                                  making run directories, filling those directories with all of the 
                                  necessary files, and adjusting the job submission script
_____________________________________________________________________________________________________
# Detailed description of makefolders3: it is the third iteration of a python script that-
  * Generates a user specified number of run directories

  * Fills those directories with copies of all of the files in the current working directory
  
  * Changes the cluster job submission script:
    * Modifies which generation node to be used based on user input
    * Changes the screen output file name to the name of the current run directory
_____________________________________________________________________________________________________  
***** In order to run this script on your machine, the following changes must be made *****

1) Adjust the first line of the code based on where python is located. This can be determined by 
   typing the command: which python
   
2) Line 23 and 30 must be adjusted based on the cluster being used and corresponding language

3) Line 43 is specific to my project, therefore, it must be adjusted to call the 'rmcprofile' command
   wherever that may be for you and to give the stem name of your specific project. However, a few
   more lines could be added in order to generalize this process.
   
_____________________________________________________________________________________________________

I'd love to assist if you have any questions or issues in making this script work to your advantage.

                                      <wcureton@vols.utk.edu>
