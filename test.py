print("This is a test commit!!")

# 1. 변수와 자료형
a = 10
b = 3.14
c = "Hello"
d = True
print(a, b, c, d)

# 2. 사용자 입력 받기와 출력하기
name = input("이름을 입력하세요: ")
print("안녕하세요,", name)

# 3. 조건문 (if, elif, else)
score = 85
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
else:
    print("C학점")

# 4. 반복문 (for)
for i in range(5):
    print("for 반복:", i)

# 5. 반복문 (while)
count = 0
while count < 3:
    print("while 반복:", count)
    count += 1

# 6. 리스트 다루기
fruits = ["사과", "바나나", "포도"]
fruits.append("오렌지")
print(fruits)
print(fruits[1])

# 7. 함수정의와 호출
def add(x, y):
    return x + y

result = add(5, 7)
print("함수 결과:", result)

# 8. 문자열 다루기
text = "Python is fun!"
print(text.upper())
print(text.replace("fun", "awesome"))

# 9. 딕셔너리 사용하기
person = {"이름": "홍길동", "나이": 25}
print(person["이름"])
person["직업"] = "학생"
print(person)

# 10. 예외처리 (try-except)
try:
    num = int(input("숫자를 입력하세요: "))
    print("입력한 숫자:", num)
except ValueError:
    print("숫자가 아닙니다.")