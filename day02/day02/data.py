

#정수형
int_val = 10
#실수형
pi = 3.141592
# 파이썬에서 문자열은 ',' 둘 다 사용
# C, C++, C# JAVA 등은 홑따운표랑 쌍따옴표가 다르게 동작
name = 'Hugo'
#불형
IS_STUDENT = False #True
#False는 0과 동일 , True는 0이외의 모든 숫자를 이야기함


print(int_val)
print("Hello" + name)
print(name + str(int_val)) # int_val은 숫자형이므로 문자열로 합치고자 하면 문자열형으로 바꿔야 함

print("Pi의 값은")
print(IS_STUDENT)

name = '성명건'
age = 49
height = 178
print('이름: ' + name+ ', 나이 : ' + str(age) + ', 키: '+str(height))