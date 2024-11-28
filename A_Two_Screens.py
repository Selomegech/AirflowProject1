def solve():
    s = input()
    t = input()
    # finding the common prefix of s and t
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    # print(i)
    if i > 0:
        ans = len(s) + len(t) -  (i-1)
    else:
        ans = len(s) + len(t)
    print(ans)
t = int(input())
for _ in range(t):
    solve()