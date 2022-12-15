function combination(numbers, n) {
  if (n === 1) {
    return numbers.map((number) => [number]);
  }
  const result = [];
  numbers.forEach((fixed, index, arr) => {
    const rest = numbers.slice(index + 1);

    const combis = combination(rest, n - 1);
    const combine = combis.map((v) => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
}
function solution(numbers) {
  return [
    ...new Set(
      combination(numbers, 2)
        .map((results) => {
          let sum = 0;
          results.forEach((result) => (sum += result));
          return sum;
        })
        .sort((a, b) => a - b)
    ),
  ];
}

console.log(solution([2, 1, 3, 4, 1]));
