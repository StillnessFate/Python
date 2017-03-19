# 윤년 계산 프로그램
# 입력받은 연도가 윤년인지를 계산해주는 프로그램
#
# 입력: 연도 - 정수만 허용
# 출력: 입력받은 연도, 윤년인지의 여부
#
# 1. 항상 올바른 값이 입력된다고 가정
# 2. 윤년인지의 여부는 True & False로 출력
# 3. 입력받은 연도가 음수이면 윤년인지의 여부는 0을 출력
# 4. 출력할 때에 각각의 항목을 띄어쓰기로 구분하여 한 줄에 출력
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 16일 (version 1.0)

def isLeapyear(year) :
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) :
		return True
	else :
		return False

def main() :
	leapyear = 0
	year = int(input()) #No Exception Handling
	
	if 0 <= year :
		leapyear = isLeapyear(year)
	
	print(year, leapyear)

main()