from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


numDots = 10
possible = list(powerset([i+1 for i in range(numDots+1)]))

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
picDict = {}
for x in range(numDots+1):
    picDict[x+1] = [0 for x in range(numDots)]

input1 = ""

counter = 1
while counter < numDots+2:
    input1 = input("p"+str(counter)+": ")
    
    #print(int(input1))
    inSplit = [int(x) for x in input1.split(",")]
    #print(inSplit)
    for x in range(len(inSplit)):
        picDict[counter][inSplit[x]-1] = 1
    #print(picDict[counter])
    counter += 1
    #print(p1)

for x in range(len(modified)):
    current = modified[x];
    picture = [0 for x in range(numDots)]
    for x in range(len(current)):
        picture = xorList(picture,picDict[current[x]])
    if picture == [0 for x in range(numDots)]:
        print(current)


    