//그리디 알고리즘은 매 선택에서 지금 이 순간 가장 최적의 답을 선택하는 알고리즘
//최적해를 보장하지 않는다.

// 이 문제에서 가장 큰 수가 될 수 있는 값을 하나씩 구해도 되지만
// 숫자의 자릿수가 최대 1,000,000이므로 하나씩 구하는 것은 효율적이지 않다.

function solution(number, k) {
  const stack = [];
  let count = 0;
  for (let num of number) {
    while (count < k && stack[stack.length - 1] < num) {
      stack.pop();
      count += 1;
    }
    stack.push(num);
  }

  while (count < k) {
    stack.pop();
    count += 1;
  }

  return stack.join("");
}
