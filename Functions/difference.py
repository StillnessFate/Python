# 두 수의 차이를 수하는 함수
#
# 인자: n1, n2 - 차이를 비교할 두 수
# 반환값: 두 수의 차이
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 16일 (version 1.0)

# 방법 1
def difference(n1, n2) :
	return abs(n1 - n2)

# 방법 2
def difference(n1, n2) :
	result = None
	if n1 < n2 :
		result = n2 - n1
	else :
		result = n1 - n2

	return result