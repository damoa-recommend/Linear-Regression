import numpy as np

x = [2, 4, 6, 8, 10]
y = [81, 93, 91, 97, 98]

mean_x = np.mean(x)
mean_y = np.mean(y)

print('x 평균: ', mean_x)
print('y 평균: ', mean_y)

parent = sum([(i - mean_x)**2 for i in x])
children = sum([(x[idx]-mean_x) * (y[idx] - mean_y) for idx, value in enumerate(x)])
a = children / parent
b = mean_y - ( mean_x * a)

print('분자: ', children)
print('분모: ', parent)
print('기울기(a): ', a)
print('y 절편(b): ', b)
