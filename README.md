# I HATE WORDLE 

Computer programs solve many of the problems we face as a society. I wrote this python script to help me with my wordle addiction. This script saves me tens of minutes of time every day and gives me a better wordle score. 

Is it cheating? Of course it is.

Example usage:

If we have two rows of wordle filled in, we can search for an optimal word to use with the following command:

>python3 wordle.py -c \"....E,lA..E,.A.lE\" -n risnctb"

Number of words in dictionary 15920
wordle hints: ....E,lA..E,.A.lE
characters not in word risnctb
Possible words:
galee
halke
halve
halwe
jalee
malee
value
valve
-------
Ranking
-------
halve 34
value 32
valve 31
halwe 31
halke 31
malee 28
jalee 28
galee 28


There . means unknown letter, capitalized character means green letter, and lower case character means yellow letter. Letters not in word are specified with the -n option. The wordle hints are separated using a comma. 
