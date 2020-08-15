'''
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
 
Example 1:
Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
'''
def main(input_list):
    equal_list, unequal_list=[],[]
    for element in input_list:
        elt1, elt2= element[0], element[3]
        if '==' in element:
            if not equal_list:
                equal_list.append(elt1+elt2)
            else:
                found = False
                for i in range(len(equal_list)):
                    val = equal_list[i]
                    if elt1 in val or elt2 in val:
                        val = val + elt1 + elt2
                        found = True
                        equal_list[i]=val
                if not found:
                    equal_list.append(elt1+elt2)
        else:
            if elt1==elt2:
                return False
            unequal_list.append(elt1+elt2)
    for value in unequal_list:
        for elt in equal_list:
            if val[0] in elt and val[1] in elt:
                return False
    return True
print(main(["a==b","a==c","c!=b"]))

                    

