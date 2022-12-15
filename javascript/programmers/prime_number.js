// 특정 수가 소수인지 확인하는 방법
// 어떤 소수도 N의 제곱근보다 큰 수로 나눌 수 없다는 점을 이용
// O(sqrt(n))
function is_prime(num) {
  for (let i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

console.log(is_prime(2));
console.log(is_prime(4));
console.log(is_prime(4));

// 1~N까지 모든 소수를 구하는 경우 효율적
// 에라토스테네스의 체
// 고대 그리스 수학자 에라토스테네스가 발견한 소수를 찾는 방법
// 범위 내 앞에 숫자부터 배수가 되는 값을 차례대로 제거해 나가는 방식
// 어떤 소수도 n의 제곱근보다 큰 수로 나눌 수 없다는 점을 이용하여
// 최대 수의 제곱근 이후의 숫자는 계산하지 않아도 된다.
// O(n log(log n))
function get_primes(num) {
  const prime = [false, false, ...Array(num - 1).fill(true)];

  for (let i = 2; i * i <= num; i++) {
    if (prime[i]) {
      for (let j = i * 2; j < num; j += i) {
        prime[j] = false;
      }
    }
  }
  return prime.filter((value) => value);
}

console.log(get_primes(56));
