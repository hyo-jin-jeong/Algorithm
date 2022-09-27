const work = [2, 2, 2, 2];

console.log(work.reduce((p, c, i) => {
    console.log(p, c, i)
    return p * c
}));