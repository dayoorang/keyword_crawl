from konlpy.tag import Kkma

text = '액면분할이란? 액면분할이란 주식의 액면가액을 일정한 분할된 비율로 나눠서 총 주식 수를 여러개로 증가시키는 일을 말한다. 예를 들어서 액면가액 10,000원짜리 1주를 2개로 나누면 5,000원짜리'
kkma = Kkma()

tokens_kkma = kkma.nouns(text)
print(tokens_kkma)