function intersection(first_array, second_array) {
  var result = [];
  for (var i = 0; i < first_array.length; i++) {
    for (var j = 0; j < second_array.length; j++) {
      if (first_array[i] == second_array[j]) {
        result.push(first_array[i]);
        break;
      }
    }
  }
  return result;
}

//break 를 집어넣어서 교집합을 찾으면 빠르게 안쪽 루프를 빠져나올 수 있다.
