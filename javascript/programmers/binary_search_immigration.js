// 제한 사항의 값이 너무 큰 경우 로그시간으로 풀어야 겠다는 생각을 하자 -> 이진 탐색
// 이 문제는 특 정 값을 찾는 것이 아니다.
// 이 문제가 바라는 것은 최소 몇 분에 모든 심사가 끝나는지? 찾는 것 -> 조건에 맞는 값을 찾음
// => 이런 문제를 결정문제라고 함 = 이진 탐색 = 파라메트릭 서치(Parametric Search)

// 최소 1분에서 10억분 사이 * n 사이
// 면접관들이 해당 시간 안에 몇명을 처리 할 수 있는가?
// 처리 가능한 입국자가 n보다 작다면 시간을 늘리고, 입국자 수가 n 보다 크다면 시간을 줄인다.
// 면접관이 시간대비 몇 명을 처리 할 수 있는가?
// 시간 / 심사시간 = 심사관 당 처리 가능 한 입국자 수
// 프로그래머스 자바스크립트 강의 해설
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
