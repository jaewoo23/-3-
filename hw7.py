shopping_bag = {}

print(f'[구입]')

while True:
    item = input("상품명? ")

    if item == '':
        print()
        break
    
    num = int(input("수량은? "))

    
    shopping_bag[item]=num

    print(f'장바구니에 {item} {str(num)}개가 담겼습니다.')
    print()

print(f'>>> 장바구니 보기: {shopping_bag}')
print()
print(f'[검색]')
check = input("장바구니에서 확인하고자 하는 상품은? ")

find = shopping_bag[check]

print(f'{check}은(는) {find}개 담겨 있습니다.')
