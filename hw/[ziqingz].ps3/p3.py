import sys
f = lambda a, str1, str2, str3: print (str3) if a % 3 == 0 and a % 5 == 0 else print(str2) if a % 5 == 0 else print(str1) if a % 3 == 0 else print(a)
[f(i, 'Fizz', 'Buzz', 'FizzBuzz') for i in range(1, int(sys.argv[1])+1)]
