def length_dir(length, dir) : #degree
    rad = math.pi * (dir / 180.0)
    x = length * math.cos(rad)
    y = length * math.sin(rad)
    return (x, y)