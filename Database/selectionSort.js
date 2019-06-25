function selectionSort(array) {
  for (var i = 0; i< array.length; i++) {
    //현재까지의 최솟값이 들어있는 인덱스를 저장
    //일단은 i의 값을 최솟값으로 저장
    var lowestnumberindex = i;
    for (var j = i + 1; j < array.length; j++) {
      if (array[j] < array[lowestnumberindex]) {
        //최솟값을 찾아 저장한다.
        lowestnumberindex = j;
      }
    }
    //최솟값이 이미 올바른 위치(i)에 있는 것은 아닌가?
    //그렇지 않다면, 최솟값과 최솟값이 있어야할 자리를 서로 바꾼다.
    if (lowestnumberindex != i) {
      var temp = array[i];
      array[i] = array[lowestnumberindex];
      array[lowestnumberindex] = temp;
    }
  }
  return array;
}
