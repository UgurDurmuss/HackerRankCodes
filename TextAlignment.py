"""
width = 20
print 'HackerRank'.ljust(width,'-')
HackerRank----------

width = 20
print 'HackerRank'.center(width,'-')
-----HackerRank-----

width = 20
print 'HackerRank'.rjust(width,'-')
----------HackerRank
"""


n=5
for i in range(1,n+1):
    print(" "*(n-i)+"H"*(2*i-1))
witdh=7

for i in range(1,7):
    print('HHHHH'.rjust(witdh,' '),end="")
    print('              '.center(witdh,' '),end="")
    print('HHHHH'.rjust(witdh,' '),end="")
    print()
new=32
for _ in range(3):
    num='H'*30
    print(num.rjust(new))
for i in range(1,7):
    print('HHHHH'.rjust(witdh,' '),end="")
    print('              '.center(witdh,' '),end="")
    print('HHHHH'.rjust(witdh,' '),end="")
    print()
offset=20
for i in range(n, 0, -1):#döngü n den 1 kadar gider
    print(" " * offset + " "*(n - i) + 'H' * (2 * i - 1))
