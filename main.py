from itertools import chain, combinations
from re import I

from sympy import true

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


possible = list(powerset([1,2,3,4,5,6,7]))

modified = [];
for x in range(len(possible)):
    if len(possible[x]) > 1:
        modified.append(possible[x])

#print(modified)
def xorList(list1,list2):
    returnlist = []
    for x in range(len(list1)):
        returnlist.append(list1[x] ^ list2[x])

    return returnlist
p1 = [0,0,0,0,0,0]
p2 = [0,0,0,0,0,0]
p3 = [0,0,0,0,0,0]
p4 = [0,0,0,0,0,0]
p5 = [0,0,0,0,0,0]
p6 = [0,0,0,0,0,0]
p7 = [0,0,0,0,0,0]

input1 = ""
flag = True
counter = 1
while counter < 8:
    input1 = input("p"+str(counter)+": ")
    
    if input1 != "end":
        #print(int(input1))
        if counter == 1:
            p1[int(input1)-1] = 1
            
        elif counter == 2:
            p2[int(input1)-1] = 1
        elif counter == 3:
            p3[int(input1)-1] = 1
        elif counter == 4:
            p4[int(input1)-1] = 1
        elif counter == 5:
            p5[int(input1)-1] = 1
        elif counter == 6:
            p6[int(input1)-1] = 1
        elif counter == 7:
            p7[int(input1)-1] = 1
    else:
        counter += 1
        #print(p1)
picDict = {1:p1, 2:p2, 3:p3, 4:p4, 5:p5, 6:p6, 7:p7}
for x in range(len(modified)):
    current = modified[x];
    picture = [0,0,0,0,0,0]
    for x in range(len(current)):
        picture = xorList(picture,picDict[current[x]])
    if picture == [0,0,0,0,0,0]:
        print(current)
        break


    