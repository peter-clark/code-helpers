import numpy as np

pieces=['K', 'Q', 'R1', 'B1', 'N1', 'R2', 'B2', 'N2']
# index 0 = black, index 7 = white (right hand corner)
count=0

def permuteList(list):
    if not list:
            return [[]] # exit case
    result = []
    for e in list:
            temp = list[:] # copy list
            temp.remove(e) # remove element in list
            result.extend([[e] + r for r in permuteList(temp)]) # add removed e plus all permutations of what remains.

    return result

def isValid960Pos(pos):
    valid = True
    bishops = True
    rookyet = False
    kingyet = False

    for p in range(len(pos)):
        piece=pos[p]

        if piece=='B1':
            check=p%2
            if check%2==0:
                return False
            
        if piece=='B2':
            check=p%2
            if check%2==1:
                return False
        
        if piece=='K':
            kingyet=True
            if rookyet==False:
                return False
        
        if piece=='R1' or piece=='R2':
            if rookyet==False:
                if kingyet==True:
                    return False # seen king but not rook yet
                rookyet=True
            else:
                if kingyet==False: # seen both rooks and no king
                    return False
    return True

# Unique from the perspective that chess960 should not include the classic chess
# starting positions. 
def isUniquePos(pos):
    if (pos[4]=='K' and pos[3]=='Q'): # if normal king queen
        if pos[0]=='R' and pos[7]=='R': # if normal rooks
            if pos[1]=='N' and pos[6]=='N': # if normal nights
                if pos[2]=='B' and pos[5]=='B': # if normal s
                    return False
    else:
        return True
    

def makeGeneric(pos): # the actual piece order of minor pieces doesn't matter.
    gen = pos
    for p in range(len(gen)):
        if gen[p]=='B1' or gen[p]=='B2':
            gen[p]='B'
        if gen[p]=='N1' or gen[p]=='N2':
            gen[p]='N'
        if gen[p]=='R1' or gen[p]=='R2':
            gen[p]='R'
    return gen

pos_list = permuteList(pieces)
true_pos_list = set()
for i in pos_list:
    if isValid960Pos(i)==True:
        temp = makeGeneric(i)
        if tuple(temp) not in true_pos_list:
            ## Uncomment below if you want positions that are not the same as OG chess. ##
            #if isUniquePos(temp)==True: 
                true_pos_list.add(tuple(temp))
print(len(true_pos_list))