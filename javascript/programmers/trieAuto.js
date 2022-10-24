//1. trie구조를 사용하여 하나의 노드에 정점을 나타내는 value, 간선을 나타내는 children, 해당 정점을 지나가는 단어 개수 저장
//2. 루트 노드부터 차례대로 자식노드로 내려오면서 해당 정점을 지나가는 단어의 개수가 1개 이하이면 count 값 반환 
//3. 1 초과이면 자식 노드로 내려감 
class Node {
    constructor(value = "") {
        this.value = value;
        this.children = new Map();
        this.count = 0;
    }
}

class Trie {
    constructor() {
        this.root = new Node();
    }

    insert(string) {
        let currentNode = this.root;

        for (const char of string) {
            if (!currentNode.children.has(char)) {
                currentNode.children.set(
                    char,
                    new Node(currentNode.value + char)
                );
            }
            currentNode = currentNode.children.get(char);
            currentNode.count += 1;

        }
    }

    has(string) {
        let currentNode = this.root;
        let count = 0;
        for (const char of string) {
            count += 1;
            if (!(currentNode.children.get(char).count > 1)) {
                return count;
            }
            currentNode = currentNode.children.get(char);

        }
        return count;

    }
}

function solution(words) {
    let count = 0;
    const trie = new Trie();
    for (const word of words) {
        trie.insert(word);
    }
    for (const word of words) {
        const value = trie.has(word);
        count += value;
    }
    return count
}

console.log("1번 답", solution(["go", "gone", "guild"]));
console.log("2번 답", solution(["abc", "def", "ghi", "jklm"]));
console.log("3번 답", solution(["word", "war", "warrior", "world"]));