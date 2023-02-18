function solution(strings, n) {
    let newStringbox = [];
    for (str of strings){
        newStringbox.push(str[n]+str);
    }
    var answer = newStringbox.sort().map((wrd) => wrd.replace(wrd.at(0),''));
    return answer;
}