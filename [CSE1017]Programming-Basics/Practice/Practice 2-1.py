# 시험점수 평균 계산 프로그램
# 시험점수의 평균을 계산해주는 프로그램
#
# 입력: 시험점수 - 1이상 100이하 정수만 허용
# 출력: 전체 과목 수, 평균점수, 과락 과목 수
#
# 1. 60미만은 평균에 포함시키지 않고 과락으로 간주
# 2. 전체 과목의 수에 과락 과목은 포함하지 않음
# 3. 0을 입력할 때까지 반복입력을 받음
# 4. 소수점 첫째 자리까지 반올림하여 출력
# 5. 평균 점수와 과락 과목 수는 0 이상일 때에만 출력
# 6. 출력할 때에 각각의 항목을 한줄씩 나누어 출력
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 16일 (version 1.0)

def getScore() :
	temp = input()
	if temp.isdigit() :
		return int(temp)
	else :
		return -1

def printScoreAverage(scoreCount, totalScore, failedCount) :
	print(scoreCount)
	if 0 < scoreCount :
		print(round(totalScore / scoreCount, 1))
	if 0 < failedCount :
		print(failedCount)

def scoreAverage() :
	scoreCount = 0
	failedCount = 0
	totalScore = 0
	numTemp = 0
	
	while True :
		numTemp = getScore()
		if 0 < numTemp :
			if 60 <= numTemp :
				if numTemp <= 100 :
					totalScore += numTemp
					scoreCount += 1
			else :
				failedCount += 1
		elif numTemp == 0 :
			break
	
	printScoreAverage(scoreCount, totalScore, failedCount)

scoreAverage()