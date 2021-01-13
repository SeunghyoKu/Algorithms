// 3진법 뒤집기
// https://programmers.co.kr/learn/courses/30/lessons/68935?language=javascript

function solution(n) {
    return parseInt(n.toString(3).split("").reverse().join(""), 3);
}

// 같은 문제를 파이썬으로도 풀었는데, 음.. ㅠ 슬퍼졌다.
