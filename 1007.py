'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
'''
def domino(A,B):
    if len(A)!=len(B):
        return -1
    marker_set = {A[0], B[0]}
    for i in range(1,len(A)):
        track_set = marker_set.copy()
        for elt in track_set:
            if elt not in {A[i], B[i]}:
                marker_set.remove(elt)
    if len(marker_set)==0:
        return -1
    if len(marker_set)==1:
        elt = marker_set.pop()
        return min(len(A)-A.count(elt),len(B)-B.count(elt))
    if len(marker_set)==2:
        elt1= marker_set.pop()
        elt2 = marker_set.pop()
        return min(len(A)-A.count(elt1), len(A)-A.count(elt2), len(B)-B.count(elt1), len(B)-B.count(elt2))
print(domino([2,1,2,4,2,2],[5,2,6,2,3,2]))