x = [2, 4, 6, 8, 10]
y = [81, 93, 91, 97, 98]

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

print('x axios mean: ', mean_x)
print('y axios mean: ', mean_y)

c = (2-6)*(81-92) + (4-6)*(93-92) + (8-6)*(97-92) + (10-6)*(98-92)
p = (2-6)*(2-6) + (4-6)*(4-6) + (8-6)*(8-6) + (10-6)*(10-6)
print(c)
print(p)
print(c/p)