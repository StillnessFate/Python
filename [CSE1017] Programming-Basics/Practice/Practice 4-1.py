# 최대공약수 계산 프로그램
# 두 수의 최대공약수를 구하는 프로그램
#
# 출력: 두 수의 최대공약수와 계산 과정
#
# 1. 유클리드 알고리즘을 이용한 재귀함수로 최대공약수를 구함
# 2. 이분 알고리즘을 이용한 꼬리재귀함수로 최대공약수를 구함
# 3. 위 꼬리재귀 함수를 while문을 사용해 구현
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 2일 (version 1.0)

def gcd1_1(m, n) :
	if n != 0 :
		print("gcd1_1", m, n)
		return gcd1_1(n, m % n)
	else:
		return abs(m)
	
def gcd1_2(m, n) :
	print("gcd1_2")
	
	def loop(m, n, k) :
		print("gcd1_2, loop", m, n, k)
		
		if not (m == 0 or n == 0) :
			if m % 2 == 0 and n % 2 == 0 :
				return loop(m // 2, n // 2, k * 2)
			elif m % 2 == 0 and n % 2 == 1 :
				return loop(m // 2, n, k)
			elif m % 2 == 1 and n % 2 == 0 :
				return loop(m, n // 2, k)
			elif m <= n :
				return loop(m, (n - m) // 2, k)
			else :
				return loop(n, (m - n) // 2, k)
		else :
			if m == 0 :
				return abs(n)#n * k
			else :#n == 0
				return abs(m * k)
		
	return loop(m, n, 1)

def gcd1_3(m, n) :
	print("gcd1_3")
	
	k = 1
	while not (m == 0 or n == 0) :
		print("gcd1_3, while", m, n, k)
		
		if m % 2 == 0 and n % 2 == 0 :
			m, n, k = m // 2, n // 2, k * 2
		elif m % 2 == 0 and n % 2 == 1 :
			m = m // 2
		elif m % 2 == 1 and n % 2 == 0 :
			n = n // 2
		elif m <= n :
			n = (n - m) // 2
		else:
			m, n = n, abs((n - m) // 2)
			
	if m == 0 :
		return abs(n)#n * k
	else :#n==0
		return abs(m * k)

print(gcd1_1(18, 48))
print(gcd1_2(18, 48))
print(gcd1_3(18, 48))	