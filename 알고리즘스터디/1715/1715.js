const path = process.platform === 'linux' ? "/dev/stdin" : "input.txt";
const [num, ...input] = require('fs').readFileSync(path).toString().split('\n').map(data => +data);

function solution1(num, input){
    let answer = 0
    while(input.length > 1){
        input.sort((a,b)=> a-b);
        let sum = input.shift() + input.shift();
        input.push(sum)
        answer += sum
    }

    return answer
}

class PriorityQueue {
    constructor() {
      this.heap = [];
    }
      
    swap(a, b) {
        const temp = this.heap[a];
        this.heap[a] = this.heap[b];
        this.heap[b] = temp;
    }
  
    push(value) {
      const { heap } = this;
      heap.push(value);
      let index = heap.length - 1;
      let parent = Math.floor((index - 1) / 2);
  
      while (index > 0 && heap[index] < heap[parent]) {
        this.swap(index, parent);
        index = parent;
        parent = Math.floor((index - 1) / 2);
      }
    }
  
    pop() {
      const { heap } = this;
      if (heap.length <= 1) {
        return heap.pop();
      }
  
      const output = heap[0];
      heap[0] = heap.pop();
      let index = 0;
  
      while (index * 2 + 1 < heap.length) {
        let left = index * 2 + 1;
        let right = index * 2 + 2;
        let next = index;
  
        if (heap[left] < heap[next]) {
          next = left;
        }
  
        if (right < heap.length && heap[right] < heap[next]) {
          next = right;
        }
  
        if (index === next) {
          break;
        }
  
        this.swap(index, next);
        index = next;
      }

      return output;
    }
}

function solution2(num, input){
    const queue = new PriorityQueue();
    let count = 0;

    input.forEach(card => {
    queue.push(card);
    });
      
    while (queue.heap.length > 1) {
    const sum = queue.pop() + queue.pop();
    queue.push(sum);
    count += sum;
    }
    return count
}

console.log(solution1(num, input))