#------------------------------------
# 과제-2-커피자동주문.py
#------------------------------------

cafe_menu = '''
[ 커피 자동주문 머신 메뉴 ]
----------------------------------
- 아메리카노:   2500원
- 카페라떼:     3000원
- 카푸치노:     3000원

원하시는 커피와 잔수를 입력하세요.
----------------------------------
'''
print(cafe_menu)

total = 0
ame_price = 2500
latte_price = 3000
cappu_price = 3000

ame_cnt = int(input('아메리카노 몇잔? '))
latte_cnt = int(input('카페라떼 몇잔? '))
cappu_cnt = int(input('카푸치노 몇잔? '))
total = ( ame_cnt * ame_price ) + ( latte_cnt * latte_price ) + ( cappu_cnt * cappu_price )

print(f'지불할 총 금액은 {total}원 입니다.')
   
pay = int(input('돈을 넣어주세요~ '))
if pay < total:
    print(f'입력한 금액이 부족합니다. {total - pay}원을 넣어주세요.')
elif pay > total:
    print(f'거스름돈은 {pay - total}원 입니다.')
else:
    print(f'감사합니다.Have a nice coffee time~')
