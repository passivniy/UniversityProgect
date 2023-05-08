#1
import math

num = int(input())

lst = []

for i in range(1, int(math.sqrt(num)) + 1):

   if num % i == 0:

       lst.append(i)

       lst.append(num // i)

lst = list(set(lst))

lst.sort()

print(*lst)