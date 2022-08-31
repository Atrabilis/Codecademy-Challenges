import math

def prime_finder(n):
  primes = list(range(2, n+1))
  print("List to analize : \n", primes, "\n")
  list_to_analize = []
  for i in range(2,n+1):
     list_to_analize = list(range(2, math.ceil(i/2)+1))
     print("Analizing ", i, "with ", list_to_analize)
     
     for j in range(2, math.ceil(i/2)+1):
       print("dividing ", i ,"with ", j)
       
       if i%j == 0 and i != j:
         print("Removing ", i)
         primes.remove(i)
         break
     
     print("primes after this iteration ", primes, "\n")
  return primes
 
print(prime_finder(11))