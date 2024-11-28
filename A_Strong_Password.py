def solve():
    s = input()
    a = 'a'
    b = 'b'
    if len(s) == 1:
        print(s + (a if s[-1] != a else b))
    else:
        for i in range(1 , len(s)):
            if s[i] == s[i-1]:
                # insert a or b which is a not in s
                ans = s[:i] + (a if s[i-1] != a else b) + s[i:]
                print(ans)
                break
t = int(input())
for _ in range(t):
    solve()