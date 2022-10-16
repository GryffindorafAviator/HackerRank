# Mr. Vincent works in a door mat manufacturing company. 
# One day, 
# he designed a new door mat with the following specifications:
# Mat size must be N * M. 
# (N is an odd natural number, and M is 3 times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Sample Designs
#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
    
# Input Format
# A single line containing the space separated values of N and M.

# Constraints
# 5 < N < 101
# 15 < M < 303

# Output Format
# Output the design pattern.

# Sample Input
# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# Solution
n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    if i == n // 2:
        print("WELCOME".center(m, "-"))
    elif i < n // 2:
        print((".|." * ((i * 2) + 1)).center(m, "-"))
    else:
        print((".|." * (((n - i - 1) * 2) + 1)).center(m, "-"))
