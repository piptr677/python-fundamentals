#give two integers in first line and more than two integers in third line
a, b = map(int, input().split())
array = input().split()
sum = 0
for each in array:
    sum = sum + int(each)
print(a, b, sum)  # prints first two integers from first line and sum of integers of second line