# Write a program that console logs the numbers from 1 to n.
# But for multiple of 3 print "fizz", for multiple of 5 print
# "buzz". The numbers which are multiple of both 3 and 3, for
# those print "fizzbuzz".

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            print(i)


fizzbuzz(100)
