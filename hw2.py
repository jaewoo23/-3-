def exchange(result) :
   n500 = result//500
   n100 = (result%500)//100
   n50 = ((result%500)%100)//50
   n10 = ((result%500)%100)%50//10

   print("500원 동전의 개수 : ",n500)
   print("100원 동전의 개수 : ",n100)
   print("50원 동전의 개수 : ",n50)
   print("10원 동전의 개수 : ",n10) 

def get_integer():
   n = int(input("동전으로 교환하고자 하는 금액은? "))
   return n

result = get_integer()
exchange(result)
