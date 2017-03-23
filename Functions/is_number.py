# 문자열이 숫자인지 확인하는 함수
#
# 인자: str - 숫자인지 검사하는 문자열
# 반환값: 정수일 경우 1, 실수일 경우 2, 숫자가 아닐 경우 False
#
# 1. 숫자의 기준은 float() 함수로 처리 가능한지의 여부
# 2. 가장 앞에 '+'혹은 '-'기호가 붙은 정수나 '.'기호가 포함된 실수는 숫자
# 3. 0을 생략하고 첫번째 자리가 '.'기호여도 숫자
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 19일 (version 1.0)

def isNumber(str) :
    result=False
    try :
        float(str)
        result=2
        int(str)
        result=1
    except :
        pass

    return result