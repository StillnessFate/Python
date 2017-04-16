# 탐색 및 출력 프로그램
# 자료를 탐색하고 값를 출력하는 프로그램
#
# 출력: 찾은 인덱스 값, 조건에 맞추어 처리된 문서 파일
#
# 1. 텍스트 파일을 읽어서 찾는 문자열이 마지막으로 등장하는 위치번호를 형식에 맟추어 "result.txt" 파일에 출력하는 함수를 구현
# 2. 텍스트 파일을 읽어서 찾는 문자열이 등장하는 모든 위치번호를 형식에 맟추어 "result.txt" 파일에 쓰는 함수를 구현
# 3. 텍스트 파일을 읽어서 찾는 문자열이 등장하는 모든 위치번호와 찾은 문자열의 수를 형식에 맟추어 "result.txt" 파일에 출력하는 함수를 구현
# 4. 텍스트 파일을 읽어서 한 줄에 한 문장씩 오도록 재편성 하고, 모든 문장과 그 수를 형식에 맟추어 "result.txt" 파일에 출력하는 함수를 구현 (문장과 문장 사이에 빈 줄로 한 줄씩 띄어야 한다)
# 5. 텍스트 파일을 읽어서 한 줄에 한 문장씩 오도록 재편성 하고, 찾는 문자열이 포함된 문장과 그 수, 그리고 각각 문장에서 찾은 문자열의 수와 전체 찾은 문자열의 수를 형식에 맟추어 "result.txt" 파일에 출력하는 함수를 구현 (문장과 문장 사이에 빈 줄로 한 줄씩 띄어야 한다)
#
# 작성자: 강민석
# 작성날짜: 2017년 4월 16일 (version 1.0)

import os
'''
if __name__ == "__main__":
    os.system('python data/Mark.py')
'''
inputfilename = "data/article.txt"
resfilename = "result.txt"

############ 윗 부분은 수정하지 마세요 ############

import sys
if 3 <= sys.version_info.major :
    LOW_VERSION = False
else :
    LOW_VERSION = True

def find_split_index(str, *keys) :
    indexList = []
    for key in keys:
        temp = str.find(key)
        if 0 <= temp :
            indexList.append(temp)

    if indexList != [] :
        idx = min(indexList)
        while (idx + 1 < len(str)) and (str[idx + 1] == '\'' or str[idx + 1] == '\"') :
             idx += 1
    else :
        idx = None

    return idx

def trim_sentence(str) :
    str = str.strip()
    str = str.strip('\n')
    return str

def version_unicode(str) :
    if LOW_VERSION :
        str = str.decode('utf8')
    return str

# 실습 1
def find_last(fileName, key) :
    inFile = open(fileName, 'r') #encoding='UTF8'
    outFile = open("result.txt", 'w')
    text = inFile.read()
    text_u = version_unicode(text)
    key_u = version_unicode(key)

    pos = text_u.rfind(key_u)
    if 0 <= pos :
        outFile.write(key + " is at " + str(pos) + ".\n")
    else :
        outFile.write(key + " is not found.\n")

    inFile.close()
    outFile.close()
    print("done")

# 실습 2
def find_all(fileName, key) :
    inFile = open(fileName, 'r') #encoding='UTF8'
    outFile = open("result.txt", 'w')
    text = inFile.read()
    text_u = version_unicode(text)
    key_u = version_unicode(key)

    pos = text_u.find(key_u)
    if 0 <= pos :
        while 0 <= pos :
            outFile.write(key + " is at " + str(pos) + "\n")
            pos = text_u.find(key_u, pos + 1)
    else :
        outFile.write(key + " is not found.\n")
        
    inFile.close()
    outFile.close()
    print("done")

# 실습 3
def find_all_count(fileName, key) :
    inFile = open(fileName, 'r') #encoding='UTF8'
    outFile = open("result.txt", 'w')
    text = inFile.read()
    text_u = version_unicode(text)
    key_u = version_unicode(key)

    findCount = 0

    pos = text_u.find(key_u)
    if 0 <= pos :
        while 0 <= pos :
            outFile.write(key + " is at " + str(pos) + "\n")
            findCount += 1
            pos = text_u.find(key_u, pos + 1)
    else :
        outFile.write(key + " is not found.\n")

    outFile.write(str(findCount))

    inFile.close()
    outFile.close()
    print("done")

# 실습 4
def one_sentence_per_line(fileName):
    inFile = open(fileName, 'r') #encoding='UTF8'
    outFile = open("result.txt", 'w')
    text = inFile.read()

    sentenceCount = 0

    keyIndex = find_split_index(text, '.', '?')
    while keyIndex != None :
        sentence = text[:(keyIndex + 1)]
        sentence = trim_sentence(sentence)
        outFile.write(sentence +"\n\n")

        sentenceCount += 1

        text = text[(keyIndex + 1):]
        keyIndex = find_split_index(text, '.', '?')

    if text != "" :
        sentence = trim_sentence(text)
        outFile.write(sentence +"\n\n")

        sentenceCount += 1

    outFile.write("문장이 총 " + str(sentenceCount) + "개")
    
    inFile.close()
    outFile.close()
    print("done")

# 실습 5
def find_all_sentence(fileName, key) :
    inFile = open(fileName, 'r') #encoding='UTF8'
    outFile = open("result.txt", 'w')
    text = inFile.read()

    sentenceCount = 0
    totalFindCount = 0
    findCount = 0

    keyIndex = find_split_index(text, '.', '?')
    while keyIndex != None :
        sentence = text[:(keyIndex + 1)]
        sentence = trim_sentence(sentence)
        findCount = sentence.count(key)
        if 0 < findCount :
            outFile.write("'" + key + "'이(가) " + str(findCount) + "번 등장\n")
            outFile.write(sentence +"\n\n")

            sentenceCount += 1
            totalFindCount += findCount

        text = text[(keyIndex + 1):]
        keyIndex = find_split_index(text, '.', '?')

    if text != "" :
        sentence = trim_sentence(text)
        findCount = sentence.count(key)
        if 0 < findCount :
            outFile.write("'" + key + "'이(가) " + str(findCount) + "번 등장\n")
            outFile.write(sentence +"\n\n")

            sentenceCount += 1
            totalFindCount += findCount

    outFile.write("'" + key + "'이(가) " + str(sentenceCount) + "개 문장에서 " + str(totalFindCount) + "번 등장")

    inFile.close()
    outFile.close()
    print("done")