def fizzbuzz(n):
  list_to_return = []
  for i in range(1,n+1):
    if i%5 == 0 and i%3 == 0:
      list_to_return.append("FizzBuzz")
    elif i%5 == 0:
      list_to_return.append("Buzz")
    elif i%3 == 0:
      list_to_return.append("Fizz")
    else:
      list_to_return.append(i)
  return list_to_return
print(fizzbuzz(16))
