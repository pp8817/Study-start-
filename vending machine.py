# 자판기를 만들거임
# 콜라, 사이다, 물 파는 자판기임
# 각각의 가격은 1000, 1500원, 500원임
# 거스름 돈도 줄 수 있게 만들거임

print('음료를 파는 자판기 입니다.')
A = int(input('넣을 돈을 입력하세요(숫자만):'))

print('콜라는 1번, 사이다는 2번, 물은 3번입니다.')
B = input('원하시는 음료의 번호를 입력해주세요:')

if B == '1번':
    print('선택하신 음료는 콜라입니다.')
    print('가격은 1000원입니다.')
    if A >= 1000:
        print('음료가 나왔습니다. 거스름돈은',A-1000 , '원입니다')
    elif A < 1000:
        print('돈이', 1000-A, '원 부족합니다.' )

if B == '2번':
    print('선택하신 음료는 사이다입니다.')
    print('가격은 1500원입니다.')
    if A >= 1500:
        print('음료가 나왔습니다. 거스름돈은',A-1500 , '원입니다')
    elif A < 1500:
        print('돈이', 1500-A, '원 부족합니다.' )

if B == '3번':
    print('선택하신 음료는 콜라입니다.')
    print('가격은 500원입니다.')
    if A >= 500:
        print('음료가 나왔습니다. 거스름돈은',A-500 , '원입니다')
    elif A < 500:
        print('돈이', 500-A, '원 부족합니다.' )

# 계속 업그레이드 할 예정
# one day
