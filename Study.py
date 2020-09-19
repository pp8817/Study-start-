# 불리안: boolean

x = True
y = False

print(x)
print(y)

# 조건문: if Elif Else

if 2 > 1:
    print('Hello')

if not 1 > 2:
    print('Hello')

if 1 > 0 and 2 > 1:
    print('Hello')

if 0 > 0 or 2 > 1:
    print('Hello')

x = 3

if x > 5:
    print('Hello')
elif x == 3:
    print('Hi')
else:
    print('Bye')


# 함수: Function, def, return

def chat(name1, name2, age):
    print('%s: 안녕? 넌 몇 살이니?' % name1)
    print('%s: 나? 나는 %d살' % (name2, age))


chat('철수', '영희', 10)
chat('알렉스', '윤하', 30)


def dsum(a, b):
    result = a + b
    return result


d = dsum(4, 7)
print(d)


# 문제
# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 '안녕' 이라고 말해라
# 나이가 10살에서 20살 사이면 '안녕하세요' 라고 말해라
# 그 외에는 '안녕하십니까' 라고 말해라

def sayHello(name, age):
    if 20 >= age >= 10:
        print('안녕하세요,' + name)
    elif 10 > age:
        print('안녕,' + name)
    else:
        print('안녕하십니까,' + name)


sayHello('워니', 9)
sayHello('상민', 20)
sayHello('윤하', 30)

# 반복문: for, while

for i in range(3):
    print(i)  # i의 매커니즘 이해를 돕기 위해
    print('철수: 안녕 영희야 뭐해?')
    print('영희: 안녕 철수야, 그냥 있어.')

i = 0
while i < 3:
    print(i)  # i의 매커니즘 이해를 돕기 위해
    print('철수: 안녕 영희야 뭐해?')
    print('영희: 안녕 철수야, 그냥 있어.')
    i = i + 1  # i = (0, 1, 2, 3 '''') + 1 = (1, 2, 3, '''')

# break, continue

i = 0
while True:
    print(i)
    print('철수: 안녕 영희야 뭐해?')
    print('영희: 안녕 철수야, 그냥 있어.')
    i = i + 1

    if i > 2:
        break

# 위 코드와 다른 점 찾아보기

for i in range(100):
    print(i)
    print('철수: 안녕 영희야 뭐해?')
    print('영희: 안녕 철수야, 그냥 있어.')

    if i > 2:
        break

for i in range(3):
    print(i)
    print('철수: 안녕 영희야 뭐해?')
    print('영희: 안녕 철수야, 그냥 있어.')
    if i == 1:
        continue  # continue는 이것을 보자마자 첫번째로 돌아가라는 코드

    print('워니: 안녕 철수와 영희야!')

# 자료구조 List (자료 구조 부분은 복습 많이 하기)

x = [1, 2, 3, 4]  # 0, 1, 2, 3 순서
y = ['hello', 'world']
z = ['hello', 1, 2, 3]

print(x[2])  # 이러면 2번째 순서인 3이 출력됨

x[3] = 10  # 3번 위치에 있는 4를 10으로 교체
print(x)

num_elements = len(x)  # len은 리스트의 함수 개수를 세주는 코드
print(num_elements)

x = [4, 2, 1, 3]
print(x)

y = sorted(x)  # sorted는 리스트 속의 함수를 정렬 해주는 코드
print(y)

z = sum(x)  # sum은 리스트 안의 함수를 모두 더해주는 코드
print(z)

print(x.index(3))  # x.index는 3이라는 값이 어디에 위치해 있는지 알려줌

print(5 in x)  # x에 5가 있는지 물어보는 것, 5가 없으니 False가 출력 됨

# 응용

x = [4, 2, 3, 1]

for n in x:
    print(n)

if 5 in x:
    print('5가 있어요.')
else:
    print('5가 없어요.')

# 자료구조 Tuple

x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, 'hello', 'there')

print(x + y)
print('a' in y)
print(z.index(1))

# list 와 tuple 의 가장 큰 다른점은 튜플은 안의 값을 변경하지 못한다
# x[0] = 10 을 할 경우 list 의 경우에는 0번째의 값이 10으로 변경되지만 튜플은 오류가 뜬다.
# mutable(가변) vs inmutable(불변)

# 자료구조 Dictionary
# Dictionary 의 Key 값에는 불변하는 값만 들어갈 수 있음 (list 는 가변이기 때문에 못 들어감)

x = {
    'name': '상민',
    'age': 20,
    1: 'Hello'
}
print(x)
print(x['name'])
print(x['age'])
print(x[1])  # x의 1번 위치 값을 보여달라는 것이 아니라 1에 해당해준 'Hello'란 값을 보여달라.
print('name' in x)

print(x.keys())  # dictionary에 있는 모든 key 값을 보여달라.
print(x.values())  # dictionary에 있는 모든 values 값을 보여달라.

for key in x:
    print('key:' + str(key))  # str 안해주면 오류남. 이유는 알지?
    print('values:' + str(x[key]))

x['name'] = 'sangmin'  # values 값의 교체, key 값은 교체 불가함. 이유는 위에서 설명
x['school'] = '수원'  # 새로운 key와 values를 추가해주는 법
print(x)

# 문제
# 과일 갯수를 세는 코드를 짜봐라.
fruit = ['사과', '사과', '바나나', '바나나', '딸기', '키위', '복숭아', '복숭아', '복숭아']

d = {}

for f in fruit:
    if f in d:  # '사과' 라는 key 가 d 라는 딕셔너리에 들어있어?
        d[f] = d[f] + 1  # 그럼 '사과' 갯수를 하나 올려줘
    else:
        d[f] = 1  # 만약 '사과' 라는 애가 없으면, 그걸 딕셔너리에 넣고 밸류는 1로 만들어줘
print(d)


# 제일 처음에 있는 '사과' 가 입력이 된다면 d에는 '사과' 가 없기 때문에 else로 넘어간다.
# 그렇기 때문에 d에 '사과' 라는 key가 생성되고 values는 1이 입력이 된다.
# 다음 '사과' 가 입력된다면 d에는 '사과' 가 있기 때문에 d[f] = d[f] + 1이 적용 돼어서 d의 '사과' values 값은 2가 된다.


# 클래스, 오브젝트, 복습 중요 (여러번 돌려보기 이해 안된다.)
# 클래스 == 빵틀, 오브젝트 == 빵틀을 이용해 만들어낸 빵 이라고 이해하면 좋다

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print('안녕!' + to_name + '나는' + self.name)

    def introduce(self):
        print('내 이름은' + self.name + '그리고 나는' + str(self.age) + '살이야')


class Police(Person):  # Police 라는 클래스가 Person 이라는 클래스를 상속한다 -> class Police(Person)
    def arrest(self, to_arrest):
        print('넌 체포됐다,' + to_arrest)


class Programmer(Person):
    def program(self, to_program):
        print('다음엔 뭘 만들지? 아 이걸 만들어야겠다:' + to_program)


wonie = Person('워니', 20)
jenny = Police('제니', 21)
michael = Programmer('마이클', 22)

wonie.introduce()
jenny.arrest('워니')
michael.program('이메일 클라이언트')

# 패키지(어떤 기능을 구현하는 모듈들의 합, 라이브러리 == 패키지), 모듈(코드 들어있는 파일)

# animal package를 만들거임
# dog, cat modules
# dog, cat modules can say 'hi'
from animal import *  # animal 패키지가 갖고 있는 모듈을 다 불러와

d = Dog()
c = Cat()
d.hi()
c.hi()
