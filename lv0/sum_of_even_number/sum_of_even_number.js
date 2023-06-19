function solution(n) {
    let answer = 0;
    for (let i = 1; i <= n; i++) {
        if (i % 2 === 0) {
            answer += i;
        }
    }
    return answer;
}

let result = solution(10);
console.assert(result === 30, `solution(10) === 30 is incorrect. The return value of solution(10) is ${result}.`);
