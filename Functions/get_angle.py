def get_angle(x1, y1, x2, y2) :
    dx = x2 - x1
    dy = y2 - y1
    rad = math.atan2(dy, dx)
    degree = rad * (180 / math.pi)
    if degree < 0 :
        degree += 360
    return degree