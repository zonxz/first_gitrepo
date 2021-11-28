#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FIRST and FOLLOW ie. first_follow.py
Objective:

1. Reads a grammar. 

g417 as from the book only added the I production for terminals x | y | z
    also set D = E' U = T' and I = id
E -> TD
D -> +TD | e
T -> FU | e
U -> *FU | e
F -> (E) | I
I -> x | y | z

g420 of Example 4.20 pg 214 of Dragon Book with id defined as x | y

S -> Aa | b
A - > bdB | B
B - > cB | adB | e




2. Finds all FIRST(X) sets, following algorithm on pg. 220-221 of text.
3. Finds all FOLLOW(A) sets following algorithm on pg. 220-221 of text.


@author: code mmodified from tdishant on python implementations of FIRST/FOLLOW
       as student Modifier: 
         
         Caleb Reiman for use of grammer g417.txt and grammer Example 4.20 pg 214 of Dragon Book
         
         SID: 003255251
         
         Email: 003255251@coyote.csusb.edu
"""


import re

def cal_follow(s, productions, first):
    follow = set() # set of 
    if len(s)!=1 :
        return {}
    if(s == list(productions.keys())[0]): #no more to analyze 
        follow.add('$') 
    
    for i in productions:
        for j in range(len(productions[i])):
            if(s in productions[i][j]):
                idx = productions[i][j].index(s)
                
                if(idx == len(productions[i][j])-1):
                    if(productions[i][j][idx] == i):
                        break
                    else:
                        f = cal_follow(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while(idx != len(productions[i][j]) - 1):
                        idx += 1 #pdate index for parsing and recursion update
                        if(not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = cal_first(productions[i][j][idx], productions)
                            
                            if('e' not in f): # empty string not their just add to set
                                for x in f:
                                    follow.add(x)
                                break
                            elif('e' in f and idx != len(productions[i][j])-1): # empty string their but index != length of productions remove the e and add
                                f.remove('e')
                                for k in f:
                                    follow.add(k)
                            
                            elif('e' in f and idx == len(productions[i][j])-1): #we still process though index and call recursion
                                f.remove('e')
                                for k in f:
                                    follow.add(k)
                                
                                f = cal_follow(i, productions, first)
                                for x in f:
                                    follow.add(x)
                            
    return follow
   
def cal_first(s, productions):
    
    first = set()# is a set of terminals
    
    for i in range(len(productions[s])):
        
        for j in range(len(productions[s][i])):
            
            c = productions[s][i][j] 
            
            if(c.isupper()): # if its upper then its production rule
                f = cal_first(c, productions) # recursive call at c
                if('e' not in f): # flagging absent empty string
                    for k in f: #continue parse
                        first.add(k) 
                    break # done
                else:
                    if(j == len(productions[s][i])-1):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('e')
                        for k in f:
                            first.add(k)
            else:
                first.add(c) #should get called when we recurse to lowercase terminal
                break
                
    return first # return top down set of terminals
                       
def main():
    productions = {}
    grammar = open("g417.txt", "r") # write in for txt g420 and g417
    
    first = {}
    follow = {}
    
    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = []
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "-" or i == ">"):
                pass
            else:
                m.append(i)
        
        left_prod = m.pop(0)
        right_prod = []
        t = []
        
        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                right_prod.append(t)
                t = []
        
        right_prod.append(t)
        productions[left_prod] = right_prod
    
    for s in productions.keys():
        first[s] = cal_first(s, productions)
    
    print("*****FIRST*****")
    for lhs, rhs in first.items():
        print(lhs, ":" , rhs)
    
    print("")
    
    for lhs in productions:
        follow[lhs] = set()
    
    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)
    
    print("*****FOLLOW*****")
    for lhs, rhs in follow.items():
        print(lhs, ":" , rhs)
    
    grammar.close()

if __name__ == "__main__":
    main()