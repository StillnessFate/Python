# 정수 입력 확인 프로그램
# 입력받은 값이 정수인지를 계산해주는 프로그램
#
# 입력: 임의의 숫자 - 정수만 허용
# 출력: 입력받은 숫자
#
# 1. 정수를 입력받을 때까지 계속 입력받음
# 2. 가장 앞에 '+'혹은 '-'기호가 있어도 정수로 취급
# 3. 입력받은 값이 정수일 경우 입력받은 값을 출력하고 종료
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 23일 (version 1.0)

def is_number(str) :
	result=False
	try :
		float(str)
		result=2
		int(str)
		result=1
	except :
		pass

	return result
	
def get_int_signed(message):
	temp = input(message)
	while not (is_number(temp) == 1):
		temp = input(message)
		
	return int(temp)

print(get_int_signed("정수를 입력하시오\n"))