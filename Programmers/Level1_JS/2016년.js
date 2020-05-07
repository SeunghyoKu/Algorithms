// 일전에 Python으로 풀 때도 이용했던 방법.

function solution(a, b) {
    var answer = '';
    var sum_date = 0;
    var day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE','WED','THU'];
    var date = [31,29,31,30,31,30,31,31,30,31,30,31];
    
    for (var i=0; i<a-1; i++) {
        sum_date += date[i];
    }
    sum_date = sum_date + b - 1;
    
    return day[sum_date%7];
}

// Date 함수 사용
function solution(a,b) {
  return new Date(2016,a-1,b).toString(0,3).toUpperCase();
}
