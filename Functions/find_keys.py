# 문자열에서 여러 값을 찾는 함수
#
# 인자: str - 값을 찾을 문자열
#       keys - 찾을 값들(문자열)
# 반환값: 찾은 값들의 위치의 리스트(각각의 값들이 첫번째로 등장하는 위치)
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 16일 (version 1.0)

def find_keys(str, *keys) :
	indexList = []
	for key in keys:
		temp = str.find(key)
		if temp != -1 :
			indexList.append(temp)

	return indexList