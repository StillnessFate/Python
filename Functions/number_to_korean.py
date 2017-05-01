# 자연수를 한글 발음법으로 변환하는 함수
#
# 인자: num - 변환할 자연수(문자열 or 정수)
# 반환값: 변환된 한글 발음 문자열
#
# 1. 최대 72자리 수까지 변환 가능(천무량대수)
# 2. 입력받은 수가 올바르지 않을 경우 빈 문자열('') 반환
#
# 작성자: 강민석
# 작성날짜: 2017년 5월 2일 (version 1.0)

def number_to_korean(num, unitDivision = False) :
	number_to_korean.words = {'0': '', '1': '일', '2': '이', '3': '삼', '4': '사', '5': '오', '6': '육', '7': '칠', '8': '팔', '9': '구'}
	number_to_korean.unit1 = {0: '', 1: '십', 2: '백', 3: '천'}
	number_to_korean.unit2 = {0: '', 1: '만', 2: '억', 3: '조', 4: '경', 5: '해', 6: '자', 7: '양', 8: '구', 9: '간', 10: '정', 11: '재', 12: '극', 13: '항하사', 14: '아승기', 15: '나유타', 16: '불가사의', 17: '무량대수'}

	result = ''
	validNumbers = 0
	
	if type(num) == int :
		num = str(num)

	if type(num) == str :
		if num.isdigit() and (len(num) <= 72) :
			num = num.lstrip('0')
			if num == '' :
				result = '영'
			else :
				index = len(num) - 1
				for x in num :
					if x != '0' :
						if x != '1' :
							result += number_to_korean.words[x]
						result += number_to_korean.unit1[index % 4]
						validNumbers += 1

					if (index % 4 == 0) and (0 < validNumbers) :
						if x == '1' :
							result += number_to_korean.words[x]
						result += number_to_korean.unit2[index // 4]
						if unitDivision :
							result += ' '
						validNumbers = 0
					index -= 1

	return result.strip()