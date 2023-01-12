Computer programs solve many of the problems we face as a society. I wrote this python script to help me with my wordle addiction. This script saves me tens of minutes of time every day and gives me a better wordle score. 

Is it cheating? Of course it is.

Example usage:

If we have two rows of wordle filled in, we can search for an optimal word to use with the following command:

python3 wordle.py -c \"....E,lA..E,.A.lE\" -n risnctb"

There . means unknown letter, capitalized character means green letter, and lower case character means yellow letter. Letters not in word are specified with the -n option. The wordle hints are separated using a comma. 
