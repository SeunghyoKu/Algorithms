//자바스크립트 사용
//파이썬으로만 풀다가 최근 JavaScript를 공부하면서 왠지 이걸로도 풀 수 있을 거 같아 풀어보았습니다.

function solution(arr)
{
    //새로운 답을 저장할 answer라는 배열을 만듭니다.
    var answer = [];    
    
    //입력 받은 array의 길이 만큼 반복한다
    for (var i = 0; i<arr.length; i++) {
        //만약 answer에 가장 마지막으로 넣은 값과 i를 비교하여 만약 두 값이 다르다면!!!!
        //i항을 아까 만들어둔 answer 에 push 합니다.
        if (answer[answer.length - 1] !== arr[i]) {
            answer.push(arr[i]);
        }       
    }
    //연속된 숫자가 없는 새로운 배열인 answer를 리턴합니다.
    return answer;
}


/* 다른 사람의 풀이

function solution(arr)
{
    return arr.filter((val,index) => val != arr[index+1]);
}

filter를 사용하였다.
*?
