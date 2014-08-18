# a naive algorithm for topological sorting
def naive_topsort(G,S=None):
  if S is None: S = set(G)        # default: all nodes
  if len(S) == 1: return list(S)  # base case, single node
  v = S.pop()                     # reduction: remove a node
  seq = naive_topsort(G,S)        # recursion, n-1
  min_i = 0
  for i,u in enumerate(seq):
    if v in G[u]: min_i = i+1     # after all dependencies
  seq.insert(min_i,v)
  return seq

# topological sorted of a DAG
def topsort(G):
  count = dict((u,0) for u in G)
  for u in G:
    for v in G[u]:
      count[v]+=1       # count every in-edge
  Q = [u for u in G if count[u]==0] # valid initial nodes
  S = []  # the result
  while Q:  # while we have start nodes
    u = Q.pop() # pick one
    S.append(u) # use it as first of the rest
    for v in G[u]:
      count[v]-=1 # uncount its out-edges
      if count[v]==0: # new valid start nodes ?
        Q.append(v)   # deal with them next
  return S

