def intersect(A, B, C, D) : # 직선 교차 체크
    def ccw(A, B, C) :
        return ((C[1] - A[1]) * (B[0] - A[0])) > ((B[1] - A[1]) * (C[0] - A[0]))
    return (ccw(A, C, D) != ccw(B, C, D)) and (ccw(A, B, C) != ccw(A, B, D))