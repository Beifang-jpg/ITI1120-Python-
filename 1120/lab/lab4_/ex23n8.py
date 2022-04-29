def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False

# ex 3

def print_all_23n8(num):
     if(num<0):
          print("You input a negative number, unable to do that.")
          return

     for i in range(0,num):
          if (is_divisible23n8(i)):
               print (i)


num = int(input("Enter a number: "))

print_all_23n8(num)