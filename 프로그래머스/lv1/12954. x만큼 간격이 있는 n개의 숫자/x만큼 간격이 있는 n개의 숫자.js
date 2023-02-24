function solution(x, n) {
    let count = 0
    gapInt = x
    answer = []
    do{
        answer.push(x);
        x+= gapInt;
        count++;
    }while(count<n)
    return answer
}