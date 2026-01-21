


#import time
#count = 10

#while count > 0:
 #   print(count)
  #  count = count -1
   # time.sleep(1) # 1초대기

#print('발사!')

#count = 1
#while True:
 #   user_input = input('종료하려면 exit을 입력하세요:')
  #  if user_input == 'exit':
   #  print('프로그램 종료')
    # break
    #else:
    # count = count +1
     #print(count)
     #print('사용자 입력 : ' + user_input)

#print('프로그램 종료')
number = 0

while number < 11: #number가 11보다 작을 동안
    print(number)
    number += 1 #number = number+1 와 동일한 코드

    if number == 3 or number == 6 or number ==9:
        print('짝')
        continue #continue 만나면 밑으로 안내려가고 올라간다
    print(number)

    print('프로그램 종료')