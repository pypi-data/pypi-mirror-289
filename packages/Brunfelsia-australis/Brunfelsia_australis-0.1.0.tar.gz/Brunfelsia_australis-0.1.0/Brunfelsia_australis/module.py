

def find_closest_day(r, g, b):

    import numpy as np

    # 1日目から8日目のRGB値をNumPy配列に変換
    day_1 = np.array([114, 68, 190]).reshape(-1, 1)
    day_2 = np.array([118, 91, 193]).reshape(-1, 1)
    day_3 = np.array([156, 136, 228]).reshape(-1, 1)
    day_4 = np.array([158, 163, 236]).reshape(-1, 1)
    day_5 = np.array([207, 191, 238]).reshape(-1, 1)
    day_6 = np.array([234, 230, 244]).reshape(-1, 1)
    day_7 = np.array([235, 232, 245]).reshape(-1, 1)
    day_8 = np.array([240, 235, 250]).reshape(-1, 1)

    # 入力されたRGB値をNumPy配列に変換
    input_color = np.array([r, g, b]).reshape(-1, 1)

    # コサイン類似度を計算
    cos_day_1 = np.dot(day_1.T, input_color)[0][0] / (np.linalg.norm(day_1) * np.linalg.norm(input_color))
    cos_day_2 = np.dot(day_2.T, input_color)[0][0] / (np.linalg.norm(day_2) * np.linalg.norm(input_color))
    cos_day_3 = np.dot(day_3.T, input_color)[0][0] / (np.linalg.norm(day_3) * np.linalg.norm(input_color))
    cos_day_4 = np.dot(day_4.T, input_color)[0][0] / (np.linalg.norm(day_4) * np.linalg.norm(input_color))
    cos_day_5 = np.dot(day_5.T, input_color)[0][0] / (np.linalg.norm(day_5) * np.linalg.norm(input_color))
    cos_day_6 = np.dot(day_6.T, input_color)[0][0] / (np.linalg.norm(day_6) * np.linalg.norm(input_color))
    cos_day_7 = np.dot(day_7.T, input_color)[0][0] / (np.linalg.norm(day_7) * np.linalg.norm(input_color))
    cos_day_8 = np.dot(day_8.T, input_color)[0][0] / (np.linalg.norm(day_8) * np.linalg.norm(input_color))

    list_cos = [cos_day_1, cos_day_2, cos_day_3, cos_day_4, cos_day_5, cos_day_6, cos_day_7, cos_day_8]

    # コサイン類似度が最も高い日を出力
    max_color = np.argmax(list_cos)

    if max_color == 0:
        return print('1日目')
    elif max_color == 1:
        return print('2日目')
    elif max_color == 2:
        return print('3日目')
    elif max_color == 3:
        return print('4日目')
    elif max_color == 4:
        return print('5日目')
    elif max_color == 5:
        return print('6日目')
    elif max_color == 6:
        return print('7日目')
    else:
        return print('8日目')


