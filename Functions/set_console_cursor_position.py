# 콘솔창의 커서를 이동시키는 함수
#
# 인자: x - 커서를 이동시킬 x좌표
#       y - 커서를 이동시킬 y좌표
# 반환값: 성공하면 0이 아닌 값을 반환
#
# 1. SetConsoleCursorPosition의 래핑 함수입니다. (Windows API)
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 19일 (version 1.0)

from ctypes import *

class COORD(Structure):
    pass
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def set_console_cursor_position(x, y) :
    STD_OUTPUT_HANDLE = -11
    stdHandle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    return windll.kernel32.SetConsoleCursorPosition(stdHandle, COORD(x,y))