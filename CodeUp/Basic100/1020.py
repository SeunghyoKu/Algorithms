#주민등록번호를 입력받아 형태를 바꿔 출력해보자.
#주민등록번호 앞 6자리와 뒤 7자리가 "-"로 구분되어 입력된다.
#"-"를 제외한 주민번호 13자리를 모두 붙여 출력한다.


#왜 앞 문제보다 더 쉬운 거 같지
#그냥 문자열 두개를 합쳐서 보여주면 된다.
infofirst, infosecond = input().split("-")
personalinfo = infofirst+infosecond
print(personalinfo)
