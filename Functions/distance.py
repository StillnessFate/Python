import math

# 방법 1
def distance(x1, y1, x2, y2) : # 두점간의 거리를 구하는 function
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 방법 2
def distance(x1, y1, x2, y2) :
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))