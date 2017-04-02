# 곱셈 계산 프로그램
# 두 수의 곱을 구하는 프로그램
#
# 출력: 두 수의 곱과 계산 과정
#
# 1. 덧셈과 뺄셈 연산만을 이용해 꼬리재귀함수로 곱을 구함
# 2. 위 꼬리재귀 함수를 while문을 사용해 구현
# 3. double함수와 halve함수를 이용해 덧셈을 하는 횟수가 log n에비례하는 재귀함수로 곱을 구함
# 4. 위 재귀 함수를 꼬리재귀 함수로 구현
# 5. 위 꼬리재귀 함수를 while문을 사용해 구현
# 6. 러시아 농부 곱셈 방법을 이용한 재귀함수로 곱을 구함
# 7. 위 재귀 함수를 꼬리재귀 함수로 구현
# 8. 위 꼬리재귀 함수를 while문을 사용해 구현
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 2일 (version 1.0)

WRITE_CODE = False

# 1. 곱셈 함수(꼬리 재귀)
def mult1(m, n) :
	def loop(n, ans) :
		if 0 < n :
			return loop(n - 1, ans + m)
		else :
			return ans
		
	return loop(n, 0)

# 2. 곱셈 함수(while문)
def mult2(m, n) :
	ans = 0
	while 0 < n :
		ans += m
		n -= 1
		
	return ans

####################
#      수정 X       #
#  곱셈 함수 보조 함수  #
def double(n) :    #
	return n * 2   #
                   #
def halve(n) :     #
	return n // 2  #
####################

# 3. 빠른 곱셈 함수(재귀)
def fastmult1(m, n) :
	if 0 < n :
		if n % 2 == 0 :
			return fastmult1(double(m), halve(n))
		else :
			return m + fastmult1(m, n - 1)
	else :
		return 0

# 4. 빠른 곱셈 함수(꼬리 재귀)
def fastmult2(m, n) :
	def loop(m, n, ans) :
		if 0 < n :
			if n % 2 == 0 :
				return loop(double(m), halve(n), ans)
			else :
				return loop(m, n-1, ans + m)
		else :
			return ans
		
	return loop(m, n, 0)

# 5. 빠른 곱셈 함수(while문)=
def fastmult3(m, n) :
	ans = 0
	while 0 < n :
		if n % 2 == 0 :
			m, n = double(m), halve(n)
		else :
			ans += m
			n -= 1
			
	return ans

# 6. 러시아 농부 곱셈 함수(재귀)
def russianmult1(m, n) :
	def loop(m, n) :
		if 1 < n :
			if n % 2 == 0 :#(m * (n % 2)) + loop(m * 2, n // 2)
				return loop(m * 2, n // 2)
			else :
				return m + loop(m * 2, n // 2)
		else :#n == 1
			return m
	
	if 0 < n :
		return loop(m, n)
	else:
		return 0

# 7. 러시아 농부 곱셈 함수(꼬리 재귀)
def russianmult2(m, n) :
	def loop(m, n, ans) :
		if 1 < n :
			if n % 2 == 0 :#loop(m * 2, n // 2, ans + (m * (n % 2)))
				return loop(m * 2, n // 2, ans)
			else :
				return loop(m * 2, n // 2, ans + m)
		else :#n == 1
			return ans + m
		
	if 0 < n :
		return loop(m, n, 0)
	else :
		return 0

# 8. 러시아 농부 곱셈 함수(while문)
def russianmult3(m, n) :
	ans = 0
	while 1 < n :
		if n % 2 == 1 :#ans += m * (n % 2)
			ans += m
		m, n = m * 2, n // 2
	
	return ans + m


# 이 실행 부분은 이해하기 어려운 코드로 작성되어 있습니다.
# 입력에 따라 알맞은 함수를 부르게 되어있습니다.
# 채점을 위한 부분이니 그냥 넘어가세요
####################################
#              수정 X               #
#           실행 스크립트              #
funcMap = {                        #
	"mult1": mult1,                #
	"mult2": mult2,                #
	"fastmult1": fastmult1,        #
	"fastmult2": fastmult2,        #
	"fastmult3": fastmult3,        #
	"russianmult1": russianmult1,  #
	"russianmult2": russianmult2,  #
	"russianmult3": russianmult3,  #
}                                  #
function = input()                 #
m = int(input())                   #
n = int(input())                   #
                                   #
res = (funcMap.get(function))(m, n)#
if type(res) == int :              #
	print(res)                     #
####################################