function solution(numbers, direction) {
    if(direction == "right"){
        for(let i=0; i < numbers.length; i++){
            let dir_num = numbers[numbers.length-1]
            numbers.splice(0, 0, dir_num)
            return numbers.slice(0,numbers.length-1,)
        }
    }else{
        for(let i=0; i < numbers.length; i++){
            let dir_num = numbers[0]
            numbers.splice(numbers.length, 0, dir_num)
            return numbers.slice(1,numbers.length)
        }
    }
}