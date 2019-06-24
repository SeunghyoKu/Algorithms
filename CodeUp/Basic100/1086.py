#그림 파일 저장용량 계산하기
#w, h, b 가 공백을 두고 입력된다.
#필요한 저장 공간을 MB 단위로 바꾸어 출력한다. (단, 소수점 셋째 자리에서 반올림해 둘 째 자리까지 출력하고 단위 MB를 공백을 두고 출력한다.)

w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

mbsize = w * h * b / (8 * 1024 * 1024)

print('%0.2f' %mbsize, "MB")
