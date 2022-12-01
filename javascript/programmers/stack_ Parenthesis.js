function solution(s) {
  let stack = [];
  if (!s || s[0] === ")") {
    return false;
  }
  for (value of s) {
    if (value === "(") {
      stack.push(value);
      continue;
    }
    if (!stack.length) {
      return false;
    }
    stack.pop();
  }

  return stack.length === 0;
}

console.log(solution("()()"));
console.log(solution("(())()"));
console.log(solution("(()("));
