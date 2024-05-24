import os
import pickle

def input_scores():
    s = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total/len(s)



def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

filename = 'score.bin'
line = []

if os.path.exists(filename): #파일 있음
    file = open(filename, 'rb')
    file.close()

    
    with open('score.bin', 'rb') as file:
        line = pickle.load(file)
    
    print(f'[파일 읽기]')

    print('\n[점수 출력]\n개인점수: ', end='')
    show_scores(line)
    avg = get_average(line)
    print(f'평균: {avg:.1f}')
    

else:
    file = open(filename, 'wb') #파일없음
    file.close()

    print("[점수 입력]")


    with open('score.bin', 'wb') as file:
        scores = input_scores()
        pickle.dump(scores, file)
    
    print('\n[점수 출력]\n개인점수: ', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')

