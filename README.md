Example usage:

If we have two rows of wordle filled in, we can search for an optimal word to use with the following command:

python3 wordle.py -c \"....E,lA..E,.A.lE\" -n risnctb"

There . means unknown letter, capitalized character means green letter, and lower case character means yellow letter. Letters not in word are specified with the -n option. The wordle hints are separated using a comma. 
