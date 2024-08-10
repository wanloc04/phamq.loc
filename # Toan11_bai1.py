# Problem. For any real number x, [x] denotes the largest integer less than or equal to x. For example, [4.2] = 4 and [0.9] = 0.
# If S is the sum of all integers k with 1 <= k <= 999999 and for which k is divisible by [sqrt(k)], then S equals ?

import math
i = 1
sum = 0
while i <= 999999:
    if i % int(math.sqrt(i))==0:
      sum = sum + i
      i = i+1
    else:
      i = i+1
print(sum)