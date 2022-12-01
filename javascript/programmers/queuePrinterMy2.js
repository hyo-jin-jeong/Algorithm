class Queue {
  constructor() {
    this.values = [];
    this.front = 0;
    this.rear = 0;
  }
  enqueue(value) {
    this.values[this.rear++] = value;
  }
  dequeue() {
    const deleteValue = this.values[this.front];
    delete this.values[this.front++];
    return deleteValue;
  }
  peek() {
    return this.values[this.front];
  }
  size() {
    return this.rear - this.front;
  }
}

function solution(priorities, location) {
  let count = 0;
  const queue = new Queue();

  for (let i = 0; i < priorities.length; i++) {
    queue.enqueue([priorities[i], i]);
  }

  priorities.sort((a, b) => b - a);

  while (true) {
    const printValue = queue.dequeue();
    if (printValue[0] === priorities[count]) {
      count += 1;
      if (printValue[1] === location) {
        return count;
      }
    }
    queue.enqueue(printValue);
  }
}

console.log(solution([2, 1, 3, 2], 2));
console.log(solution([1, 1, 9, 1, 1, 1], 0));
