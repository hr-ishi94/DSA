def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))


def reverse_string(str):
    if len(str)<=1:
        return str
    else:
        return reverse_string(str[1:]) + str[0]
print(reverse_string("Hrishi"))


def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n%10 +sum_of_digits(n//10)
    
print(sum_of_digits(12345))