#ways to traverse through a given 2d grid from one corned to another (m,n). Can be solved in O(1) with combinatorics = (m+n) C n
def traverse_nodp(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return traverse_nodp(m-1, n) + traverse_nodp(m, n - 1)

#with memoization
def traverse(m, n, memo = {}):
    key = m + "," + n
    #ways to traverse (m, n) is same as (n, m)
    alt_key = n + "," + m
    if(key in memo or alt_key in memo):
        return memo[key]
    #base case (1,1) grid has 1 way
    if m == 1 and n == 1:
        return 1
    #cannot have grid w/ 0 width or height
    if m == 0 or n == 0:
        return 0
    memo[key] = traverse(m-1, n, memo) + traverse(m, n - 1, memo)
    return memo[key]

