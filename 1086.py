'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
 
Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 
Note:
1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
'''
def top5average(num_list):
    sum=0
    for i in range(5):
        sum+=num_list[i]
    return sum//5

def average(num_list):
    track_dict = {}
    result=[]
    for i in range(len(num_list)):
        if num_list[i][0] in track_dict:
            track_dict[num_list[i][0]].append(num_list[i][1])
        else:
            track_dict[num_list[i][0]]=[num_list[i][1]]
    for elt in track_dict:
        track_dict[elt].sort()
    for elt in track_dict:
        result.append([elt,top5average(track_dict[elt][:5])])
    return result
print(average([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
