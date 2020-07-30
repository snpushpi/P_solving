'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
 
Example 1:
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinetely.
Example 3:
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 
Note:
1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
'''
def boundedRobot(instructions):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    direct = 0
    start_point = [0,0]
    new_instructions = ''
    for i in range(4):
        new_instructions+=instructions
    for instruction in new_instructions:
        if instruction=='L':
            direct = (direct+3)%4
        elif instruction=='R':
            direct = (direct+1)%4
        else:
            start_point[0]+=directions[direct][0]
            start_point[1]+=directions[direct][1]
    if start_point==[0,0]:
        return True 
    else:
        return False
print(boundedRobot("GL"))