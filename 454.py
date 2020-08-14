'''Four Sum Problem'''
def main(A,B,C,D):
    hash_set = set()
    for a in A:
        for b in B:
            hash_set.add(a+b)
    for c in C:
        for d in D:
            if -(c+d) in hash_set:
                return True
    return False
    