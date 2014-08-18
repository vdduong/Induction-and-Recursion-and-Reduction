# reducing a problem A to B involves some form of transformation
# take an example
# have a list of numbers, want to find the two (non identical) numbers that are closest to each other.

from random import randrange
seq = [randrange(10**10) for i in xrange(100)]
dd = float('inf')
for x in seq:
  for y in seq:
    if x==y: continue
    d = abs(x-y)
    if d<dd:
      xx,yy,dd = x,y,d

# two nested loops = quadratic, generally not a good thing
# sorting is in general loglinear (n lgn)
# the insight here is that the two closest numbers must be next to each other in the sorted sequence
seq.sort()
dd = float('inf')
for i in xrange(len(seq)-1):
  x,y = seq[i],seq[i+1]
  if x==y: continue
  d = abs(x-y)
  if d < dd:
    xx,yy,dd = x,y,d

# faster algorithm and same solution
