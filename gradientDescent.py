import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

study_time = [2, 4, 6, 8, 10]
score = [81, 93, 91, 97, 98]

x_data = np.array(study_time)
y_data = np.array(score)

a = 0
b = 0

learn_rate = 0.01
epochs = 20000

for i in range(epochs):
  y_pred  = x_data * a + b # 예측값
  error = y_data - y_pred  # 실측값 - 예측값 = 오차
  
  a_diff = -(2 / len(x_data)) * sum(error * x_data)
  b_diff = -(2 / len(x_data)) * sum(error)  

  a = a - learn_rate * a_diff
  b = b - learn_rate * b_diff

  if not i % 100:
    print("epoch: %d, 기울기: %f, 절편: %f"%(i, a, b))


y_pred = a * x_data + b # 최종 예측값
plt.scatter(x_data, y_data) # 그래프에 점찍기
plt.plot(x_data, y_pred)
plt.show()