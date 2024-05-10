shopping_bag = {}

def buy(shopping_bag):
    
    while True:
        print(f'[구입]')
        item = input("상품명? ")

        if item == '':
            return False
    
        num = int(input("수량은? "))

    
        shopping_bag[item]=num

        print(f'장바구니에 {item} {str(num)}개가 담겼습니다.')
        print()
    
def show(shopping_bag):
    print(f'>>> 장바구니 보기: {shopping_bag}')
    print()

def find(shopping_bag):
    print(f'[검색]')
    check = input("장바구니에서 확인하고자 하는 상품은? ")

    if check in shopping_bag:
        find = shopping_bag[check]
        print(f'{check}(는) {find}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {check}은(는) 없습니다.')




while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
