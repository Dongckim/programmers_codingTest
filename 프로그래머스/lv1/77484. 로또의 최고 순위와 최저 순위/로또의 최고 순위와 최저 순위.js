function isWin(lottos, win_nums){
    let isWinlotto = lottos.filter((word)=> word == 0 ? true : win_nums.includes(word))
    return isWinlotto
}
function isLose(lottos, win_nums){
    let isLoselotto = lottos.filter((word)=> win_nums.includes(word))
    return isLoselotto
}
function solution(lottos, win_nums){
    let rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[isWin(lottos, win_nums).length], rank[isLose(lottos, win_nums).length]]
}