function solution(price, money, count) {
    let startpoint = 0
    do{
        startpoint+=count
        count--
    }while(count >= 0)
    return money > startpoint*price ? 0 : startpoint*price - money
}
