# 정렬 프로그램
# 정수 리스트를 정렬하는 프로그램
#
# 출력: 정렬된 리스트
#
# 1. 삽입정렬의 insert0함수를 재귀 함수로 구현
# 2. 위 재귀 함수를 꼬리재귀 함수로 구현 (insert1)
# 3. 위 꼬리재귀 함수를 while문을 사용해 구현 (insert)
# 4. 위 insert함수를 이용한 삽입정렬 isort0함수를 꼬리재귀 함수로 구현 (isort1)
# 5. 위 꼬리재귀 함수를 while문을 사용해 구현 (isort)
# 6. 위 함수를 for문을 사용해 구현 (isort)
# 7. 합병정렬의 merge1함수를 꼬리재귀 함수로 구현
# 8. 위 꼬리재귀 함수를 while문을 사용해 구현 (merge)
# 9. for문을 사용해 버블 정렬을 구현 (bsort)
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 9일 (version 1.0)

# 1
def insert0(x, ss) :
		if ss != [] :
			if x <= ss[0] :
				return [x] + ss
			else :
				return [ss[0]] + insert0(x, ss[1:])
		else :
			return [x]

# 2
def insert1(x, ss) :
	def loop(ss, left) :
		if ss != [] :
			if x <= ss[0] :
				return left + [x] + ss
			else :
				return loop(ss[1:], left + [ss[0]])
		else :
			return left + [x]

	return loop(ss, [])

# 3
def insert(x, ss) :
	left = []
	while ss != [] :
		if x <= ss[0] :
			return left + [x] + ss
		else :
			ss, left = ss[1:], left + [ss[0]]
			
	return left + [x]

'''
def isort0(s):
	if s!=[]:
		return insert(s[0], isort0(s[1:]))
	else:
		return []
'''

# 4
def isort1(s) :
	def loop(s, ss) :
		if s != [] :
			return loop(s[1:], insert(s[0], ss))
		else :
			return ss
		
	return loop(s, [])

'''
# 5
def isort(s) :
	ss = []
	while s != [] :
		s, ss = s[1:], insert(s[0], ss)
	return ss
'''

# 6
def isort(s) :
	ss = []
	for _ in s:
		s, ss = s[1:], insert(s[0], ss)
		
	return ss

# 7
def merge1(left, right) :
	def loop(left, right, ss) :
		if not (left == [] or right == []) :
			if left[0] <= right[0] :
				ss.append(left[0])
				return loop(left[1:], right, ss)
			else :
				ss.append(right[0])
				return loop(left, right[1:], ss)
		else :
			return ss + left + right

	return loop(left, right, [])

# 8
def merge(left, right) :
	ss = []
	while not (left == [] or right == []) :
		if left[0] <= right[0] :
			ss.append(left[0])
			left = left[1:]
		else :
			ss.append(right[0])
			right = right[1:]
			
	return ss + left + right

'''
def msort0(s) :
	if len(s) > 1 :
		mid = len(s) // 2
		return merge(msort0(s[:mid]), msort0(s[mid:]))
	else :
		return s
'''

# 9
def bsort(s) :
	for k in range(len(s)) :
		for i in range(len(s) - 1) :
			if s[i] > s[i + 1]:
				s[i], s[i + 1] = s[i + 1], s[i]
				
	return s

'''
print(bsort([3, 5, 4, 2]))
'''