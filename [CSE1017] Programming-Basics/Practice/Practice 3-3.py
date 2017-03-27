# 안전한 제곱근 구하기 프로그램
# 입력받은 값의 제곱근을 구하는 프로그램
#
# 입력: 임의의 숫자 - 유효한 정수 혹은 실수만 허용
# 출력: 입력받은 숫자, 제곱근
#
# 1. 유효한 값을 입력받을 때까지 계속 입력받음
# 2. 가장 앞에 '+'혹은 '-'기호가 있다면 유효하지 않은 값으로 취급
# 3. 입력받은 값이 유효할 경우 입력된 값과 제곱근을 미리 주어진 양식에 맞추어 출력
# 4. 출력을 한 이후에는 계속 진행할것인지를 묻고 답변에 따라 처리
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 23일 (version 1.0)

import math

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

def print_result(num, sqrt):
	print(num, "의 제곱근은", sqrt, "입니다.")

def check_float(x) :
	checkNumber = is_number(x)
	if 0 < checkNumber and x[0] != '+' and 0 <= float(x) :
		return checkNumber
	else :
		return False
	
def stop() :
	cont = input('계속하시겠습니까? (y/n) ')
	while not (cont == 'y' or cont == 'n'):
		cont = input('계속하시겠습니까? (y/n) ')
	
	return cont == 'n'

def safe_sqrt():
	print("제곱근을 구해드립니다.")
	print("0이상의 수를 입력하세요.")
	
	while True :
		temp = input("수를 입력하세요.\n")
		check = check_float(temp)
		if 0 < check :
			if check == 1 :
				num = int(temp)
			else :
				num = float(temp)
			
			sqrt = round(math.sqrt(num), 4)
			print_result(num, sqrt)
			
			if stop() :
				break
	
	print("안녕히 가세요.")
	
safe_sqrt()