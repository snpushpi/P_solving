'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''
#ideas -
#use bfs to find the distance from one building to another slot 
#for all possible co-ordinates, we will keep track of the number of buildings we can reach to
def bfs(r,c,distance_reach_map,matrix):
    '''In this function, we run bfs from the vertex r,c to all other reachable vertices and save that info in the distance_reach_map'''
    if r<0 or r>len(matrix) or c<0 or c>len(matrix[0]):
        return
    queue = [[r,c]]
    qdist = [1]
    while queue:
        x,y = queue.pop(0)
        curr_dist = qdist.pop(0)
        distance = [[0,-1],[-1,0],[0,1],[1,0]]
        for dx,dy in distance:
            new_x, new_y = x+dx, y+dy
            if (0<=new_x<len(matrix) and 0<=new_y<len(matrix[0]) and matrix[new_x][new_y]==0):
                matrix[new_x][new_y]=-1
                temp = distance_reach_map[new_x][new_y]
                distance_reach_map[new_x][new_y]=[temp[0]+curr_dist,temp[1]+1]
                queue.append([new_x,new_y])
                qdist.append(curr_dist+1)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==-1:
                matrix[row][col]=0

            
def main(matrix):
    row = len(matrix)
    col = len(matrix[0])
    distance_reach_map = [[(0,0) for i in range(col)] for j in range(row)]
    buildings = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==1:
                bfs(row,col,distance_reach_map,matrix)
                buildings+=1
    result = float('inf')
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            dist, reach = distance_reach_map[row][col]
            if reach==buildings:
                result = min(result,dist)
    return result

print(main([[1, 0, 2, 0, 1], 
		[0, 0, 0, 0, 0], 
		[0, 0, 1, 0 ,0]]))
            