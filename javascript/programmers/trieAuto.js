class Node {
    constructor(value = "") {
        this.value = value;
        this.children = new Map();
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
        }
    }

    has(string) {
        let currentNode = this.root;
        let count = 0;
        for (const char of string) {
            if (!(currentNode.children.size > 1)) {
                return count;
            }
            currentNode = currentNode.children.get(char);
            count += 1;
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
console.log(solution(["go", "gone", "guild"]))
console.log(solution(["abc", "def", "ghi", "jklm"]))