def read_single_digit(num, l):
   num = str(num)
   if num.find('1', l)!=-1:
      print("일", end=' ')
   elif num.find('2', l)!=-1:
      print("이", end=' ')
   elif num.find('3', l)!=-1:
      print("삼", end=' ')
   elif num.find('4', l)!=-1:
      print("사", end=' ')
   elif num.find('5', l)!=-1:
      print("오", end=' ')
   elif num.find('6', l)!=-1:
      print("육", end=' ')
   elif num.find('7', l)!=-1:
      print("칠", end=' ')
   elif num.find('8', l)!=-1:
      print("팔", end=' ')
   elif num.find('9', l)!=-1:
      print("구", end=' ')

def read_number(num):
   read_single_digit(num, 0)
   read_single_digit(num, 1)
   read_single_digit(num, 2)

num = int(input("세 자리 정수 입력: "))

read_number(num)
