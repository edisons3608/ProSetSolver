from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


MODE = 7
possible = list(powerset([i+1 for i in range(MODE)]))

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
color2Num = {"r":0, "g":1, "y":2,"b":3,"p":4,"o":5}
input1 = ""
flag = True
counter = 1
while counter < 8:
    input1 = input("p"+str(counter)+": ")
    
        #print(int(input1))
    inSplit = [*input1]
    #print(inSplit)
    if counter == 1:
        
        for x in range(len(inSplit)):
            p1[color2Num[inSplit[x]]] = 1
    elif counter == 2:

        for x in range(len(inSplit)):
            p2[color2Num[inSplit[x]]] = 1
    elif counter == 3:
        for x in range(len(inSplit)):
            p3[color2Num[inSplit[x]]] = 1
    elif counter == 4:
        for x in range(len(inSplit)):
            p4[color2Num[inSplit[x]]] = 1
    elif counter == 5:
        for x in range(len(inSplit)):
            p5[color2Num[inSplit[x]]] = 1
    elif counter == 6:
        for x in range(len(inSplit)):
            p6[color2Num[inSplit[x]]] = 1
    elif counter == 7:
        for x in range(len(inSplit)):
            p7[color2Num[inSplit[x]]] = 1
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


    