const [num, ...input] = require('fs').readFileSync('input.txt').toString().split('\n');

function solution1(input){
    let total = input.map(item => item.split('.')[1])

    let categories = new Set();
    total.map(item => categories.add(item))

    let categoriesLst = Array.from(categories).sort()
    
    answer = []

    for (let cate of categoriesLst){
        let categoryNum = total.filter(item => item === cate).length
        categoriesLst.map(item => {
            if(item === cate){
                answer.push(`${item} ${categoryNum}`)
            }
        })
    }
    return answer;
}

function solution2(input){
    let newObj = new Object();

    input.map(item => {
        const [ _ , extender] = item.split('.')
        newObj[extender] ? newObj[extender]++ : (newObj[extender] = 1)
    })

    let answer = [];

    Object.keys(newObj).sort().map(item => {
        answer.push(`${item} ${newObj[item]}`)
    })
    return answer.join('\n')
}


function solution3(input){
    const map = {};
    const sorted = [];
    
    for (let i = 0; i < input.length; i++) {
        const [ _ , extender] = input[i].split(".");
        map[extender] = (map[extender] || 0) + 1;
    }
    
    for (let key in map) {
        sorted.push([key + " " + map[key]]);
    }
    
    answer = sorted.sort();
    
    return answer.join("\n");
}

console.log(solution2(input))