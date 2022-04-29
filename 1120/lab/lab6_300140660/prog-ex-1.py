def sum_odd_while_v2(n):
   #   '''(int)->int
   #      Returns the sum of all odd integers between 5 and n
   #      '''
      
   A = 5
   an = 0
   while (A < n and (A % 2)==1):
      an = an + A
      A = A + 1
      
   return an

print(sum_odd_while_v2(10))
print(sum_odd_while_v2(-7))   
