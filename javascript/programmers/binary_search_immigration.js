function solution(n, times) {
  let left = 1;
  let right = Math.max(...times) * n; // => 최악의 시간

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    const personCount = times.reduce(
      (acc, time) => acc + Math.floor(mid / time),
      0
    );
    if (personCount < n) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return left;
}

console.log(solution(6, [7, 10]));
