#날짜를 년월일(yyyy.mm.dd)의 형태로 입력받아, 일월년(dd-mm-yyyy)의 형태로 출력하는 프로그램을 작성해보자

year, month, date = input().split(".")
print(date+"-"+month+"-"+year)
