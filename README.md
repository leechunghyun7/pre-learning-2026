# pre-learning-2026
IOT개발자 과정 사전학습 리포지토리

## 1일차
과정소개

학습 리포지토리 생성

- 마크다운 학습
  1. 제목
   ```markdown
   # 제목1
   ## 제목2
   ### 제목3
   #### 제목4
   ##### 제목5
   ###### 제목6
   <|-- 주석(HTML주석 동일) -->
   ```

   2. 목록
   ```markdown
   - 목록
   * 목록
   1.숫자목록
   2.숫자목록
   ```

   3. 기본문법 - 링크, 이미지

       ```markdown
      [네이버](https://naver.com)

      ![이미지](이미지 url)
       ## 사이즈 조절 이미지
       src : 이미지 URL
       width : 이미지넓이 픽셀단위 지정
       <img src="이미지URL" width="400">
      ```
   
      -[네이버](https://naver.com)

      -![이미지](https://naverpa-phinf.pstatic.net/MjAyNjAxMDZfNjUg/MDAxNzY3Njc1OTQ1NzQ1.LUDf36_DqwqfFNOVFr3bA2BMNefn1oGd9iv_Lry60g8g.1ZuVNZBSKtH7Wx01NAAL6BdXF9HJ7jW0mZyvvw8W15og.JPEG/0_342x228_176767594573317555301678645804685.jpg)
      - <img src="https://naverpa-phinf.pstatic.net/MjAyNjAxMDZfNjUg/MDAxNzY3Njc1OTQ1NzQ1.LUDf36_DqwqfFNOVFr3bA2BMNefn1oGd9iv_Lry60g8g.1ZuVNZBSKtH7Wx01NAAL6BdXF9HJ7jW0mZyvvw8W15og.JPEG/0_342x228_176767594573317555301678645804685.jpg" width="200">
      -이미지와 링크의 차이는 !로 시작하는지 밖에 없음
  
-<img width="750" height="585" alt="image" src="https://github.com/user-attachments/assets/fc0d64e6-85dd-4df9-8c4f-b6289c02d7ee" />

4.기본문법 - 가로줄
```markdown
---
```
---
5.기본문법 - 코드블럭
 -소스코드를 작성할 때 코드하이라이팅, 영역표시 때 사용
 -백틱(`)을 세번 후 표시언어를 입력 또는 한번(인라인 코드블럭)
 ```python
print('Hello python')
 ```

-일반적인 문장에서 한 단어를 강조하고 싶을때 `인라인 코드블럭`을 사용

6.강조 및 밑줄
 ```markdown
*,~,_,html u사용, i 이탤릭
```
- 문장을 작성할 시 **강조**, ~~취소선~~, __강조__,<u>밑줄</u>,<i>이태릭</i> 을 사용할 수 있습니다.




  -깃허브 로컬리포지토리 생성
  1.git FOR Windows 설치
   -https://git-scm.com/에서 'install for windows' 버튼 클
   -Git for windows/x64 setup 클릭
   -Git 설치 옵션은 기본 그대로 사용 가능 변경하지 말것
   -cmd, powershell 에서 `git --version`, 'git -v'  확인
  2.Github Desktop 설치
   -https://desktop.github.com/download/ d\에서 다운로드 클릭, 설치
   -계정 브라우저 연동
  3. 리포지토리 클론
   - github Desktop 메뉴 Clone Repository 클릭
   - github.com탭에서 저장소 검색, 선택
   - Local path 지정 후 '클론' 버튼 클릭
 
  -visual studio code 설치
   1.https://code.visualstudio.com/ Download for windows 버튼 클릭
   2.설치 `C|DEV?EDE?MICROSOFT VS CODE`에 설치
   3.Extension > korean pack for visual studio code 설치후 재시작

  -추가 설치 프로그램
  1. Notepad++ 에디터 - https://notepad-plus-plus.org/downloads/
  2.  픽픽 - https://picpick.net/
     
     -**파이썬** 개발환경 설정
        1. https://www.python.org/ 에서 Download의 python 3.1x.x버튼을 클
        2. Add python.exe to PATH 체크 활성화 후
        3.Installer > Customize installation 클릭
        4.Documentation 체크 해제, for all users 체크 활성화 다음
        5.Advanced options 에서 Install python 3.1x for all users 체크
        6.경로 변경후 설치<img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/2f3d3b8e-c984-4816-9364-c1f9136051d8" />
        8.setup was successful 에서 Disable path length limit 클릭 (필수!)
        <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/1de9f7bc-0bc9-4cbd-9ca5-406c35ed39a1" />




  -프로그램 개발 개념
