# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format
# A single line of input contains the string S.

# Constraints
# 0 < len(S) < 1000

# Output Format
# Output the sorted string S.

# Sample Input
# Sorting1234

# Sample Output
# ginortS1324

# Solution
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')