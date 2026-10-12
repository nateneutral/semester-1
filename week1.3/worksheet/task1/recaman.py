# Worksheet 1.3: Task 1
from recaman_add import RecamanAdd
L = int(input("Length of sequence: ")) # this should be your only input
ak = 0 # next item to be added to sequence
tmpk = 0 # potential item to be added to sequence, used to compare to items already in sequence
sequence =[]
k = 1

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
while len(sequence) < L:
    sequence.append(ak)
    inFlag = False
    if (ak - k) > 0:
        tmpk = ak - k
        for i in sequence:
            if(i == tmpk):
                inFlag = True 
                break
        if not inFlag:
            ak = tmpk
        else:
            ak = RecamanAdd(ak,k)
            
    else:
        ak = RecamanAdd(ak,k)
        
    
    k = k + 1



# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence


