# 코드 정리 프로그램
#
# 인자: path - 정리할 파이썬 소스파일
#       tabSize - 탭의 크기(공백 수)
#
# 1. 개인용 코드 자동 정리 프로그램
# 2. 문법상 오류가 없는 코드만을 대상으로 할 것
# 3. 정리된 소스파일은 <기존 파일명>_arrange 에 저장됨(확장자 포함)
#
# 작성자: 강민석
# 작성날짜: 2017년 5월 2일 (version 1.0)

(
	STATE_NORMAL,
	STATE_STRING,
	STATE_ANNOTATION,
) = range(3)

def code_arrange(path, tabSize) :
	f_in = open(path, 'r', encoding = 'UTF8')
	temp = path.rpartition('.')
	outFileName = temp[0] + '_arrange' + temp[1] + temp[2]
	f_out = open(outFileName, 'w')

	state = STATE_NORMAL
	stringCharacter = ''
	lineAnnotation = False
	lastCodeCharacter = ''
	continuousApostrophe = 0
	newLineStack = 0

	line = f_in.readline()
	while line != "" :
		arrangedLine = ""
		tabs = 0
		spaces = 0
		codeArea = False
		codeStartIndex = 0
		backSlash = False
		lineLen = len(line)

		if (state == STATE_ANNOTATION) and lineAnnotation :
			state = STATE_NORMAL
		for idx, val in enumerate(line) :
			if state == STATE_NORMAL :
				if not codeArea :
					if val == '\t' :
						tabs += 1
					elif val == ' ' :
						spaces += 1
					else :
						arrangedLine += '\t' * (tabs + (spaces // tabSize))
						codeArea = True
						codeStartIndex = idx

				if codeArea :
					if val == '#' :
						lineAnnotation = True
						state = STATE_ANNOTATION
						arrangedLine += val
					elif val in ['\'', '\"'] :
						if val == '\'' :
							continuousApostrophe += 1
						if continuousApostrophe == 3 :
							lineAnnotation = False
							state = STATE_ANNOTATION
							continuousApostrophe = 0
						else :
							stringCharacter = val
							state = STATE_STRING
						arrangedLine += val
					elif val == ',' :
						arrangedLine += val
						if  (idx + 1 < lineLen) and (line[idx + 1] not in [' ', '\r', '\n']) :
							arrangedLine += ' '
					elif val in ['+', '-', '*', '-', '<', '>', '!'] :
						if (codeStartIndex <= idx - 1) and (line[idx - 1] not in [' ', '(', '[', '\n']) :
							arrangedLine += ' '
						arrangedLine += val
						if (lastCodeCharacter not in ['+', '-', '*', '-', '=', '(', '[', ',', '\n']) and ((idx + 1 < lineLen) and (line[idx + 1] not in ['=', ' ', '\r', '\n'])) :
							arrangedLine += ' '
					elif val == '=' :
						if (codeStartIndex <= idx - 1) and (line[idx - 1] not in [' ', '+', '-', '*', '-', '<', '>', '!', '=']) :
							arrangedLine += ' '
						arrangedLine += val
						if (idx + 1 < lineLen) and (line[idx + 1] not in ['=', ' ']) :
							arrangedLine += ' '
					elif val == ':' :
						if ((codeStartIndex <= idx - 1) and (line[idx - 1] != ' ')) and ((idx + 1 < lineLen) and (line[idx + 1] in ['\r', '\n'])) :
							arrangedLine += ' '
						arrangedLine += val
					else :
						arrangedLine += val
			elif state == STATE_STRING :
				if backSlash :
					backSlash = False
				elif val == '\\' :
					backSlash = True
				elif val == stringCharacter :
					state = STATE_NORMAL

				if val == '\'' :
					continuousApostrophe += 1

				arrangedLine += val
			elif state == STATE_ANNOTATION :
				if not lineAnnotation :
					if val == '\'' :
						continuousApostrophe += 1
						if continuousApostrophe == 3 :
							state = STATE_NORMAL
							continuousApostrophe = 0
					else :
						continuousApostrophe = 0

				arrangedLine += val

			if val != ' ' :
				lastCodeCharacter = val
			if val != '\'' :
				continuousApostrophe = 0

		arrangedLine = arrangedLine.rstrip(' \n')
		if arrangedLine != "" :
			f_out.write('\n' * newLineStack)
			f_out.write(arrangedLine)
			newLineStack = 0
			
		if line[-1] == '\n' :
			newLineStack += 1

		line = f_in.readline()

	f_in.close()
	f_out.close()