import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

print(num1 * ((num2%100)%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)