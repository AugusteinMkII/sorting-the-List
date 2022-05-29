###sorting radom integers
import random ##for generating list of random numbers
import pprint
least = []
l=[] ##list of random numbers
for i in range(430):
    l.append(random.randint(1,10000))
while len(l) > 0:
    buf = l[0] ##assigning variable buf the first element in list
    for i in range(len(l)): ##iterating through entire list
        if buf > l[i]: ##comparing each element with var buf
            buf = l[i] ##if element in list less than buf overwriting buf with that value
    least.append(buf) ## otherwise to if condition append buf to least
    l.remove(buf) ##remove the element in buf from list l
pprint.pprint(l)
pprint.pprint(least)