function solution(a, b) {
    let createDate = '2016'+'-'+`${a}`+'-'+`${b}`
    let week = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    let dayOfWeek = week[new Date(createDate).getDay()];
    return dayOfWeek;
}