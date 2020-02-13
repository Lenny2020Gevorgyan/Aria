x = int(input())
h = int(input())
m = int(input())
hours = x + (h * 60)
minutes = m
total = hours + minutes
print(total // 60)
print(total % 60)
