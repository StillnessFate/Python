# 문자열이 특정 문자 집합으로 이루어져 있는지 확인하는 함수
#
# 인자: str - 특정 문자 집합으로 이루어져 있는지 확인할 문자열
#       elements - 문자 집합(문자열)
# 반환값: 문자열이 elements 문자 집합으로 이루어져 있는 경우 True, 아닐 경우 False
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 3일 (version 1.0)

# 방법 1
def consist(str, elements) :
    result = True
    for x in str:
        if x not in elements :
            result = False
            break

    return result

# 방법 2
def consist(str, elements) :
    return str.strip(elements) == ''