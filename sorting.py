# to get the sequence sorted up to position i, first sort it recursively up to position i-1
# then swap element seq[i] down until it reaches its correct position among the already sorted elements

# recursive insertion sort, pratical limitation = the length of the sequence it'll work on
def ins_sort_rec(seq,i):
  if i==0: return # base case-- do nothing
  ins_sort_rec(seq,i-1) # sort 0..i-1
  j = i   # start walking down
  while j>0 and seq[j-1] > seq[j]:  # look for OK spot
    seq[j-1], seq[j] = seq[j],seq[j-1]  # keep moving seq[j] down
    j-=1  # decrement j

# insertion sort
# instead of recursing backward, it iterates forward from the first element
def ins_sort(seq):
  for i in xrange(1,len(seq)):
    j=i
    while j>0 and seq[j-1]>seq[j]:
      seq[j-1],seq[j] = seq[j],seq[j-1]
      j-=1

# recursive selection sort
def sel_sort_rec(seq,i):
  if i==0:return
  max_j = i
  for j in range(i):
    if seq[j]>seq[max_j]: max_j=j
  seq[i],seq[max_j] = seq[max_j],seq[i]
  sel_sort_rec(seq,i-1)

# selection sort
def sel_sort(seq):
  for i in xrange(len(seq)-1,0,-1):
    max_j = i
    for j in xrange(i):
      if seq[j]>seq[max_j]: max_j=j
    seq[i],seq[max_j] = seq[max_j],seq[i]



  
