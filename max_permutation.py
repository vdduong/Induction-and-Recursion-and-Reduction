# each has a favorite seat
# want to find a way to let them switch seats to make as many people as possible happy with the result
# they refuse also to move to another seat if they can't get their favorite
# a form of matching problem

# bipartite graph, find the largest permutation possible
# in essence, we can implement using a simple list
# eliminate the seat that no one wants to seat in

M = [2,2,0,5,3,5,7,4]

# a naive implementation of the recursive algorithm idea for finding a maximum permutation
def naive_max_perm(M,A=None):
  if A is None:               # the element set not supplied ?
    A = set(xrange(len(M)))   # A = {0,1,..n-1}
  if len(A) == 1: return A    # base case- single element
  B = set(M[i] for i in A)    # the "pointed to" elements
  C = A-B                     # "not pointed to" elements
  if C:                       # any useless elements ?
    A.remove(C.pop())         # remove one of them
    return naive_max_perm(M,A)  # solve remaining problem
  return A                      # all useful, return all

# the function naive_max_perm receives a set of remaining people A and creates a set of seats that are pointed to B.
# if it finds an element in A that is not in B, it removes the element, and solves the remaining problem recursively

# the most wasteful operation is the repeated creation of set B
# if we could just keep track of which chairs are no longer pointed to, we could eliminate this operation entirely
# one way of doing this would be to keep a count for each element

# finding a maximum permutation
def max_perm(M):
  n = len(M)  # how many elements ?
  A = set(range(n)) # A = {0,1,..n-1}
  count = [0]*n     # C[i] == 0 for i in A
  for i in M:       # all that are pointed to
    count[i]+=1     # increment 'point count'
  Q = [i for i in A if count[i] == 0] # useless elements
  while Q:  # while useless elements left
    i = Q.pop() # get one
    A.remove(i) # remove it
    j = M[i]    # who's it pointing to ?
    count[j]-=1 # not anymore
    if count[j]==0: # is j useless now ?
      Q.append(j)   # then deal with it next
  return A          # return useful elements

