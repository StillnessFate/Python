# 대출 상환금 계산 서비스
# 대출금 상환금액을 계산해주는 프로그램
#
# 입력: 원금(principal) - 백만이상 정수만 허용
#       상환기간(years) - 1이상정수만 허용
#       연이자율(interestRate) - 0.0에서 100.00 사이의 부동소수점수만 허용
# 출력: 연상환금액, 월상환금액, 상환금액의 총계
#
# 1. 미리 주어진 양식에 맞추어 출력
# 2. 모든 값은 정수 형태로 출력
# 3. 입력값 유효성 체크는 하지 않음
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 9일 (version 1.0)

print("대출 상환금 계산 서비스에 오신걸 환영합니다.")

principal = int(input("대출원금이 얼마인가요? 백만원 이상만 계산해 드립니다. "))
years = int(input("상환기간은 몇년인가요? "))
interestRate = float(input("이자율은 몇%인가요? "))

repaymentYears = int((((1 + (interestRate / 100)) ** years) * principal * (interestRate / 100)) / (((1 + (interestRate / 100)) ** years) - 1))
repaymentMonth = int(repaymentYears / 12)
repaymentTotal = int(repaymentYears * years)

print("대출 상환금 내역을 알려드리겠습니다.\n")

print("1년에 한번씩 상환하신다면 매년 {0} 원씩 지불하셔야 합니다.".format(repaymentYears))
print("1달에 한번씩 상환하신다면 매월 {0} 원씩 지불하셔야 합니다.".format(repaymentMonth))
print("상환완료시까지 총 상환금액은 {0} 원 입니다.".format(repaymentTotal))

print("저희 서비스를 이용해주셔서 감사합니다.")
print("또 들려주세요.")