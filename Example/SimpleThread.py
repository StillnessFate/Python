# 스레드를 생성해서 1초마다 "Thread is running!" 문자열을 출력한다
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 19일 (version 1.0)

import time
import threading

class ThreadClass(threading.Thread):
    def run(self):
        while True:
            print("Thread is running!")
            time.sleep(1)


workThread = ThreadClass()
workThread.start()