import numpy as np

# y = ax + b 예측값 계산
def predict(a_b, study_time):
  return a_b[0] * study_time + a_b[1]

def mse(predict_scores, scores):
  return ((predict_scores - scores) ** 2).mean()

def mse_val(predict_scores, score):
  return mse(np.array(predict_scores), np.array(score))

temp_a_bs = [[0, 80.6], [1.5, 80.6], [1.8, 80.6], [1.9, 80.6], [3, 80.6], [4, 80.6], [5, 80.6]]

for a_b in temp_a_bs:
  print('기울기: %f, y절편: %f'%(a_b[0], a_b[1]))
  
  study_time = [2, 4, 6, 8, 10]
  score = [81, 93, 91, 97, 98]
  predict_scores = []

  for i, val in enumerate(study_time):
    p = predict(a_b, val)
    predict_scores.append(p)
    # print("공부시간: %f, 실제점수: %f, 예측점수: %f"%(val, score[i], p))

  print("MSE 값: ", mse_val(predict_scores, score))
  print()