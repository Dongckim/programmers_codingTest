function solution(sizes) {
   let numBiggerBox = [] 
   let numSmallerBox = []
   for (eachSizes of sizes){
       [size1, size2] = eachSizes
        size1 > size2 ? numBiggerBox.push(size1) : numBiggerBox.push(size2)
        size1 < size2 ? numSmallerBox.push(size1) : numSmallerBox.push(size2)
    }
    return numBiggerBox.sort((a,b)=> b-a)[0]*numSmallerBox.sort((a,b)=>b-a)[0]
}
