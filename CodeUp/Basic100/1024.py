#단어를 하나 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.


#'B''o''y' 이런 식으로 문제에서는 답을 원해서.. 어떤 방법으로 할까 하다가.. 그냥 프린트에 ""를 포함해서 출력해주었다.
#다른 방버이 있었을 지도..

word = list(input())
for i in range(len(word)):
  print("'"+word[i]+"'")
