"""
----type----

int: 정수
float: 실수
str: 문자열
list: 리스트
기타 등등

----입력----
input()
콘솔에서 사용자가 입력한 값을 문자열로 return

----연산자----
할당 연산자 =

다중 할당, 동시 할당
[변수1], [변수2] = [값1], [값2]
[변수1] = [변수2] = [값1]

산술 연산자
+, -, *, /, //, %, **

#복합 대입 연산자
+=, -=, *=, /=, %=, //=

관계 연산자
==, !=, <, >, <=, >=

논리 연산자
and, or, not

----조건문----
if [논리 박스]:
 들여쓰기 ->
elif [논리박스]:
 들여쓰기 ->
else:
 들여쓰기 ->

----반복문----
while [논리상자]:
 들여쓰기 ->

for [변수] in [range([시작, 끝, 증감]) / [리스트]]:
 들여쓰기 ->


----함수----
def [함수이름]([인자값1], [인자값2], [인자값3]....):
 들여쓰기 ->

----리스트----
[]

"""

"""
----삼항연산자----

----f문자열----

----람다식----

----고차함수----

----union type----
def funciotn(value : int | str = " ") -> float | str

isinstance() -> 객체타입을 검사
issubclass() -> 클래스 계층 검사


---- 언패킹 ----
리스트 언패킹
data = [1,2,3,4]
a,b,c,d = data

튜플 언패킹
data = (1,2,3,4)
a,b,c,d = data


#함수 호쿨시 언패킹
def add(x, y, z):
    return x+y+z
args =[1,2,3]

add(*args)


#딕셔너리 언패킹
info={'name':1,'name2':2}

키언패킹
a,b = info
print(a, b)

키와 벨류 모두다 언패킹할려면 dict.items()를 써야 함. 

#다중 대입
a, b = 1, 2
#값 교환
a, b = b, a

#*을 이용한 언패킹
num = [1,2,3,4,5]
a, *b = num

*a, b = num

a, *b, c = num

#딕셔너리 병합
d1 = {'a':1, 'b':2}
d2 = {'a':1, 'b':2}


w =d1 | d2
print(**w)


---walrus Operator--- 할당 표현식 :=
표현식내에거 변수에 값을 할당하며 동시에 그 값을 사용
입력값 처리, 반복문 내 조건 감사, 리스트 컴프리헨션 최적화 등에 유용
# 기존 방식
n = len(data)
if n> 10:
    print(f"데이터가 너무 큽니다.{n}개")

#walrus operator 활용
if(n := len(data)) >10:
    print(f"데이터가 너무 큽니다.{n}개")
    
--- class ---

--- 제네릭 ---
타입을 매개변수로 받는다. 
다양한 타입에 대해 작동하도록 만든다. 
필수 타입은 아니지만 클래스나 함수에서 타입 힌트를 제공하고 타입 안정성을 높이는데 유용.

class Stack[T]:
    def __init__(self) 
    
--- 데코레이터 ---
함수나 메서드에 추가적인 기능을 "덧붙여" 주는 함수
코드의 중복을 줄이고, 함수나 메서드의 기능을 확장하거나 수정가능 

imoprt time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end= time.time()
        print(f"{func.__name__} 실행 시간: (end - start:.4f} 초")
        return result
    return wrapper

@timer
def compute():
    return sum(range(1000000))
    
print(compute())

---아이터레이터---


---시퀀스 패턴 매칭 ---
def math_sequence(seq):
    match seq:
        case [1,2,3]:
            return "리스트 1,2,3"
        case [x, *rest]:
            return "첫번째 값: {x}, 나머지 값들 {rest}"
        case _:
            return "다른 리스트"
            
math_sequence([1,2,3])
math_sequence([1,2,3,4,5])
math_sequence([7,8,9])

---가드 패턴--- case 구문에서 조건을 추가하여 세밀한 매칭을 할 수 있는 방식

def classify_number(n):
    #가드 조건 추가
    match n:
        case n if n<0:
            return "음수"
        case 0:
            return 0
        case n if n > 0:
            return "양수"
        case _:
            return "알수 없음"

print(classify_number(10))
print(classify_number(0))
print(classify_number(-10))
print(classify_number([1,2,3,4]))

---중첩 패턴--- 중첩된 데이터 구조를 처리할 수 있는 패턴 매칭
def describe_person(person):
    #중첩 패턴 매칭
    match person:
        case {"name":name, "age":age}:
            return f"{name}, {age}"
        case {"name":name, "age":age, "address":{"city":city}}:
            return f"{name}, {city}, {age}"
        case _:
            return "알 수 없는 정보"
print(describe_person({"name":"test", "age":10}))
print(describe_person({"name": "tst1", "age":20, "address":{"city":"seoul"}}))
print(describe_person("test"))

---one-Liner
한줄의 코드로 특정 동작을 수행하는 코드를 의미 
간결성, 표현력, 함수형 프로그래밍 스타일등을 강조할때 유용하지만, 때로는 가독성을 희생할 수 있다. 

람다 함수 활용
price_after_discount = lambda price :price *0.9
tax_callculator = lambda amount, rate =0.1: amount * (1+rate)

리스트 연산
numbers=[1,2,3,4,5]
squared=list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x%2==0, numbers))


딕셔너리 연산 원라이너
data = {('a', 1), ('b', 2), ('c', 3)}
dict_from_tuples= dict(data)
reversed_dict = {v: k for k, v in dict_from_tuples.items()"

리스트 플래트닝 
nest_list = [[1,2],[3,4],[5,6]]
flattended = [item for sublist in nested_list for item in sublis

조건부 딕셔너리 생성

복잡한 데이터 변환

문자열 처리 원라이너 

리스트 중복 제거 순서 유지 
"""
