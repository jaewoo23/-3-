
def display_multiplication_table() :
    i = 1

    for i in range(2, 11, 4):
        num = i
        while i<=9:
            for y in range(1, 10,1):
            
                print(f'{num} x {y} = {num*y:2d}\t{num+1} x {y} = {(num+1)*y:2d}\t{num+2} x {y} = {(num+2)*y:2d}\t{num+3} x {y} = {(num+3)*y:2d}')
                i=i+1

            if y==9:
                print(' ')
    


display_multiplication_table()