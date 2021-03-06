'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
 
Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
'''
def main(trust,N):
    first_zone = set()
    second_zone = set()
    for elt in trust:
        first_zone.add(elt[0])
        second_zone.add(elt[1])
    if len(second_zone-first_zone)==-1:
        return -1
    else:
        for elt in second_zone-first_zone:
            return elt