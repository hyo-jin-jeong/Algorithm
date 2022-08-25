//1. 같은 장르끼리 묶자
//2. 묶인 노래들을 재생 순으로 정렬
//3. 노래를 2개까지 자르는 작업
//4. 자른 것들을 배열로 반환
// 프로그래머스 코딩 광탈방지 A to Z 풀이

//flat()은 하위 배열을 합칠 때 사용
//flatMap은 flat과 map을 합침 -> 조건을 주어 하위 배열을 합칠 수 있다.
//고차함수를 활용하자!! 
function solution(genres, plays) {
    const hashTable = new Map();

    genres.forEach((genre, index, array) => {
        const data = hashTable.get(genre) || { total: 0, songs: [] };
        const play = plays[index];
        hashTable.set(genre, {
            total: data.total + play,
            songs: [...data.songs, { play, index }]
                .sort((a, b) => b.play - a.play)
                .slice(0, 2)
        })
    })
    return [...hashTable]
        .sort((a, b) => b[1].total - a[1].total)
        .flatMap((item) => item[1].songs)
        .map((song) => song.index);
}


console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]));