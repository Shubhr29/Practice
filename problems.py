# 1. function for finding factorial of number

def fact(n):
    result = 1
    while n>1:
        result

# 2. function for finding Nth  fibonacci number

# 3. function for finding if a number is odd or even

def isEven(n):
    return n % 2 == 0
    
# 4. function for findng if a number is prime

def isPrime(n):
  for i in range (2,n):
    if n%i==0:
      return False
  
  return True

result= isPrime(35)
print(result)

# 5. function for checking for palindrome number

def isPalindrome(s):
    return str(s) == str(s)[::-1]

result = isPalindrome('mom')
print(result)