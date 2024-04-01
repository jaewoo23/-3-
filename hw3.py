
def get_fixed_price(what, price):

    global rate
    
    fix = price/(1-0.01*rate)
    
    print(what, "상품의 정가는 ",int(fix), "원")
    
    


rate = int(input("할인율은?"))

aprice = int(input("A 상품의 할인된 가격은?"))

bprice = int(input("B 상품의 할인된 가격은?"))

get_fixed_price('A', aprice)

get_fixed_price('B', bprice)
