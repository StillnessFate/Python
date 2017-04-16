# 과제 체크 함수
# 리스트에서 찾는 값과 가장 가까운 수의 인덱스를 반환하는 closest함수를 체크하는 함수
#
# 인자: function - 유효성의 확인할 closest함수
#       sort - 리스트의 정렬 여부 (이분탐색과 같이 리스트가 정렬된 상태에서만 동작할 경우에만 True)
# 반환값: 함수가 유효할 경우 True, 아닐 경우 False
#
# 1. 실행 시 런타임 오류가 발생할 경우에도 유효하지 않은 함수
# 2. key와 리스트의 범위에는 음수값도 포함
# 3. closest함수의 속도에 따라 변동될 수 있지만 하나의 함수를 체크하는 데 대략 10초 이내를 시간이 소요
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 16일 (version 1.0)

import random

def check_closest_function(function, sort = False, keyMin = -5000, keyMax = 5000, keyLoop = 100, listMin = -5000, listMax = 5000, listSize = 1000, listLoop = 100) : return (lambda f, sort, keyMin, keyMax, keyLoop, listMin, listMax, listSize, listLoop:list(map((lambda s, f, keyMin, keyMax, keyLoop:list(map((lambda s, key, f:(f(s, key) == None) if (s == []) else (abs(min(s, key = lambda x:abs(x - key)) - key) == abs(key - s[f(s, key)]))), [([s.sort(), s][1] if (sort) else s)] * (keyLoop + 1), random.sample(range(keyMin, keyMax), keyLoop) + [listMax], [f] * (keyLoop + 1))).count(False) == 0), [random.sample(range(listMin, listMax), listSize) for _ in range(listLoop)] + [[]], [f] * (listLoop + 1), [keyMin] * (listLoop + 1), [keyMax] * (listLoop + 1), [keyLoop] * (listLoop + 1))).count(False) == 0)(function, sort, keyMin, keyMax, keyLoop, listMin, listMax, listSize, listLoop)

# 기본
print(check_closest_function(seq_search_closest))
print(check_closest_function(bin_search_closest, True))