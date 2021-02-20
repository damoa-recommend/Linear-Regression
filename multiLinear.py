import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

study_time = [2, 4, 6, 8, 10]
class_tile = [0, 4, 2, 3, 4]
score = [81, 93, 91, 97, 98]

x1_data = np.array(study_time)
x2_data = np.array(class_tile)
y_data = np.array(score)

a1 = 0
a2 = 0
b = 0

learn_rate = 0.01
epochs = 20000

for i in range(epochs):
  y_pred = a1 * x1_data + a2 * x2_data + b # 예측값
  error = y_data - y_pred  # 실측값 - 예측값 = 오차
  
  a1_diff = -(2 / len(x1_data)) * sum(error * x1_data)
  a2_diff = -(2 / len(x2_data)) * sum(error * x2_data)
  b_diff = -(2 / len(x1_data)) * sum(error)

  a1 = a1 -learn_rate * a1_diff
  a2 = a2 -learn_rate * a2_diff
  b = b -learn_rate * b_diff

  if not i % 100:
    print("epoch: %d, 기울기1: %f, 기울기2: %f 절편: %f"%(i, a1, a2, b))

import statsmodels.api as statm
import statsmodels.formula.api as statfa

X = [[x1_data[idx], x2_data[idx]] for idx, value in enumerate(study_time)]
Y = score

X_1=statm.add_constant(X)
results=statm.OLS(score,X_1).fit()

hour_class=pd.DataFrame(X,columns=['study_hours','private_class'])
hour_class['Score']=pd.Series(score)

model = statfa.ols(formula='Score ~ study_hours + private_class', data=hour_class)

results_formula = model.fit()

a, b = np.meshgrid(np.linspace(hour_class.study_hours.min(),hour_class.study_hours.max(),100),
                   np.linspace(hour_class.private_class.min(),hour_class.private_class.max(),100))

X_ax = pd.DataFrame({'study_hours': a.ravel(), 'private_class': b.ravel()})
fittedY=results_formula.predict(exog=X_ax)

fig = plt.figure()
graph = fig.add_subplot(111, projection='3d')

graph.scatter(hour_class['study_hours'],hour_class['private_class'],hour_class['Score'],
              c='blue',marker='o', alpha=1)
graph.plot_surface(a,b,fittedY.values.reshape(a.shape),
                   rstride=1, cstride=1, color='none', alpha=0.4)
graph.set_xlabel('study hours')
graph.set_ylabel('private class')
graph.set_zlabel('Score')
graph.dist = 11

plt.show()