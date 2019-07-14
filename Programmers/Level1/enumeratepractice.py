#예전에 풀었던 날짜 출력 문제와 같다.
#연습문제를 풀다가 발견함!
#enumerate()를 사용해서 풀 수 있길래 풀어보았다.


#enumerate 는 for문을 쓸 때 range와달리 몇 번째 반복문인지 확인할 수 있다.
#즉, range와 달리 2가지 이상의 것을 반복할 수 있다.

days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i, day in enumerate(days):
    print('{}월의 날짜수는 {}일 입니다.'.format(i+1, day))
