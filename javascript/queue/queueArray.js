class Queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }

    enqueue(value) {
        this.queue[this.rear++] = value;
    }

    dequeue() {
        const value = this.queue[this.front];
        delete this.queue[this.front];
        this.front += 1;
        return value;
    }
    peek() {
        return this.queue[this.front];
    }
    size() {
        return this.rear - this.front;
    }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
console.log(queue.queue);
console.log('max', Math.max(...queue.queue));
console.log(queue.peek());
console.log(queue.size());
queue.dequeue();
queue.dequeue();
console.log('max2', Math.max(...queue.queue));
console.log(queue.peek());
console.log(queue.size());
console.log(queue);
