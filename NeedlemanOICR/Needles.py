import numpy as np

dna1 = 'GCATGCU'
dna2 = 'GATTACA'

def not_reached_end (i,j):
    return (dna1.__len__()+1 == i)and(dna2.__len__()+1 == j)

def not_at_origin (i,j):
    return not (i == j == 0)


arr = np.zeros((dna1.__len__()+1, dna2.__len__()+1), int)

# Basically a 3D boolean array, but encoded with case of strings
dirA = np.full((dna1.__len__()+1, dna2.__len__()+1), 'hvd')

# h -> horizontal
# v -> vertical
# d -> diagonal


# top -> down        means INDEL mutation
# left -> right      means INDEL mutation
indel_score = -1

# diagonal no match  means substitution
sub_score = -1

# diagonal match     means no mutation
match_score = 1

# Used for testing
arr += 1234321

# Fill top row and left coloumn #
for each in range(dna1.__len__()+1):
    arr[0][each] = each*indel_score
for each in range(dna2.__len__()+1):
    arr[each][0] = each*indel_score

for countX in range(1, min(dna1.__len__()+1, dna2.__len__()+1)):
    for countY in range(1, min(dna1.__len__()+1, dna2.__len__()+1)):
        # calculate value at cell [count][count]
        options = []
        options.append(indel_score + arr[countX - 1][countY]) # H
        options.append(indel_score + arr[countX][countY - 1]) # v
        options.append((match_score if dna1[countX-1] == dna2[countY-1] else sub_score) + arr[countX - 1][countY - 1]) # D
        arr[countX][countY] = max(options)
        for each in range(len(options)):
            if options[each] == max(options):
                a = dirA[countX][countY]
                dirA[countX][countY] = ''.join(c.upper() if i in [each] else c for i, c in enumerate(dirA[countX][countY]))


pX = dna1.__len__()
pY = dna2.__len__()
strands = ['', '']
while not_at_origin(pX, pY):
    if arr[pX][pY][0].isupper():
        # Move horizontal
        strands[0] = dna1[pX-1] + strands[0]
        strands[1] = dna2[pY-1] + strands[1]



'''             Not super sure if this is the right approach.
                I will attempt just following the upper cases
                Branching is something I struggle with, so I 
                will try it after tracing simply one path
# while not_reached_end(x, y):
#   make listOfOptions
#   find min
#   fill with min

# Find path back
pX = dna1.__len__()
pY = dna2.__len__()
movements = []
count = 0

while not_at_origin(pX, pY):
    options = [arr[pX][pY], arr[pX-1][pY], arr[pX][pY-1]]
    inter = []
    for b in dirA[pX][pY]:
        if b.isupper():
            inter.append(True)
        else:
            inter.append(False)
    print inter
    print options

    movements[count] = np.where(inter, options)
    count += 1
'''

print arr
print dirA
print movements
