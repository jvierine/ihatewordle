#!/usr/bin/env python3

import numpy as n
import argparse
import matplotlib.pyplot as plt

class wordle_words:
    def __init__(self):
        self.wordle_words=[]
        for l in open("wordle.txt","r").readlines():
            l=l.strip()
            if len(l)==5:
                if "-" in l:
                    pass
                else:
                    a=n.array(list(l.lower()),dtype="str")
                    self.wordle_words.append(a)
  #                  fo.write("%s\n"%(l.lower()))
 #       fo.close()
        print("Number of words in dictionary %d"%(len(self.wordle_words)))
        self.wordle_words=n.array(self.wordle_words)
        self.n_words=self.wordle_words.shape[0]

    def filter(self, word_idx=[], chars_not_in=["a","y"], wordle_hints=[""]):

        if len(word_idx) == 0:
            word_idx=n.arange(self.n_words,dtype=int)

        wordle_words = self.wordle_words[word_idx,:]
        n_words=len(word_idx)
                              
        # everything is good by default
        okay=n.zeros([n_words,5],dtype=bool)
        okay[:,:]=True
        
        for c in chars_not_in:
            c=n.array(c)
            # mask bad characters
            okay[wordle_words == c]=False

        for wordle_hint in wordle_hints:
            print("wordle hint %s"%(wordle_hint))
            if len(wordle_hint) == 0:
                continue
            elif len(wordle_hint) != 5:
                print("wrong hint length %s"%(wordle_hint))
                exit(0)
                
            wha=list(wordle_hint)
            
            for ci,c in enumerate(wha):
                if not c.isalpha():
                    print("ignoring %s"%(c))
                    continue
                
                print("char %d hint %s"%(ci,c))
                
                # upper case means letter is in correct place
                if c.isupper():
                    
                    nc=n.array( c.lower() )
                    bidx=n.where( wordle_words[:,ci] != nc )[0]
                    okay[bidx,ci] = False
                    
                elif c.islower():
                    
#                    print("lower case %s"%(c))
                    nc=n.array(c.lower())

                    bad_word_idx=n.where(n.sum(wordle_words == nc,axis=1)==0)[0]
                    okay[bad_word_idx,:]=False
                    
                    # if this letter is in this place in the word, then false
                    okay[(wordle_words[:,ci] == nc),ci] = False

                    
        # reduce word array
        gidx=n.where(n.min(okay,axis=1) == True)[0]
        # if short enough list, show all
        if len(gidx) < 300:
            print("Possible words:")
            for i in gidx:
                print("%s%s%s%s%s"%(wordle_words[i,0],wordle_words[i,1],wordle_words[i,2],wordle_words[i,3],wordle_words[i,4]))
        else:
            print("Too many words, not showing all possibilities")
                
        return(word_idx[gidx])

    def find_most_common_matched(self,idx=[]):
        """ 
        figure out what word is best using K-L divergence
        """
        if len(idx) == 0:
            idx=n.arange(self.wordle_words.shape[0],dtype=int)

        words=self.wordle_words[idx,:]
        n_words=len(idx)

        common_counts=[]
        
        # go through all words, 
        for i in range(n_words):
            # test this one
            # find out how many words share characters with this one
            word0=words[i,:]

            n_common_chars=0
            word00=n.unique(word0)
            for ci in range(len(word00)):
                n_common_chars+=n.sum(words == word00[ci])
            common_counts.append(n_common_chars)

        idx=n.argsort(common_counts)[::-1]
        print("-------")
        print("Ranking")
        print("-------")
        if len(idx) > 100:
            idx=idx[0:100]
            print("only showing 100 highest ranked...")
        for i in idx:
            print("%s%s%s%s%s %d"%(words[i,0],words[i,1],words[i,2],words[i,3],words[i,4],common_counts[i]))
        

w=wordle_words()

parser = argparse.ArgumentParser(
prog = 'ProgramName',
    description = "Example of use: python3 wordle.py -c \"....E,lA..E,.A.lE\" -n risnctb",
    epilog = '')

parser.add_argument('-c', '--wordle_hints', default="", action='store')      # wordle lines
parser.add_argument('-n', '--not_in_word', default="", action='store')

#The ArgumentParser.parse_args() method runs the parser and places the extracted data in a argparse.Namespace object:

args = parser.parse_args()
print("wordle hints: %s"%(args.wordle_hints))
print("characters not in word %s"%(args.not_in_word))

#["---tE","C----"])
gidx=w.filter(wordle_hints=args.wordle_hints.split(","),
              chars_not_in=list(args.not_in_word))

w.find_most_common_matched(gidx)
