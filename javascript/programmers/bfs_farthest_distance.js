function solution(n, edge) {
  const graph = Array.from(Array(n + 1), () => []);

  for (const [start, dest] of edge) {
    graph[start].push(dest);
    graph[dest].push(start);
  }

  const distance = Array(n + 1).fill(0);
  distance[1] = 1;

  const queue = [1];
  while (queue.length > 0) {
    const start = queue.shift();

    for (dest of graph[start]) {
      console.log(start, dest);
      if (distance[dest] === 0) {
        queue.push(dest);
        distance[dest] = distance[start] + 1;
        console.log("distance = ", distance[dest]);
      }
    }
  }

  const max = Math.max(...distance);
  return distance.filter((value) => value === max).length;
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);
