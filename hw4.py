def rep_char(who, num):
    
    print(who*num)



def draw_line_string(who):
    num = len(who)

    return num

who = input("Input his/her name: ")

wel = "Welcome to Seoul."

if (len(who)>len(wel)):
    num = len(who)
else :
    num = len(wel)
    

num = num*2

draw_line_string(who)

rep_char('-', num)

print(f'Hello {who},\nWelcome to Seoul.')

rep_char('-', num)
