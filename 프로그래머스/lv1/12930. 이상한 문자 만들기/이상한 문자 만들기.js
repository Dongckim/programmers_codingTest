function solution(s) {
    return s.split(' ').map((word,index)=> [...word].map((letter,idx)=> idx%2==0 ? letter.toUpperCase() : letter.toLowerCase()).join('')).join(' ')
}