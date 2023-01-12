# I HATE WORDLE 

Computer programs solve many of the problems we face as a society. I wrote this python script to help me with my wordle addiction. This script saves me tens of minutes of time every day and gives me a better wordle score. 

Is it cheating? Of course it is.

Example usage:

If we have two rows of wordle filled in, we can search for an optimal word to use with the following command:

>python3 wordle.py -c \"....E,lA..E,.A.lE\" -n risnctb"<br />
><br />
>Number of words in dictionary 15920<br />
>wordle hints: ....E,lA..E,.A.lE<br />
>characters not in word risnctb<br />
>Possible words:<br />
>galee<br />
>halke<br />
>halve<br />
>halwe<br />
>jalee<br />
>malee<br />
>value<br />
>valve<br />
>-------<br />
>Ranking<br />
>-------<br />
>halve 34<br />
>value 32<br />
>valve 31<br />
>halwe 31<br />
>halke 31<br />
>malee 28<br />
>jalee 28<br />
>galee 28<br />


There . means unknown letter, capitalized character means green letter, and lower case character means yellow letter. Letters not in word are specified with the -n option. The wordle hints are separated using a comma. 
