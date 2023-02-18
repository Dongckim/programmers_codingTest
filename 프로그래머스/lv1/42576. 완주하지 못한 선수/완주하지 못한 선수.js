/*function solution(pp, cpl){
    pp.sort()
    cpl.sort()
    while (pp.length) {
        let pPop = pp.pop()
        if (pPop !== cpl.pop()) 
        return pPop
    }
}*/

function solution(pp,cpl){
    let key = new Map()
    for(let i = 0; i < cpl.length; i++){
        if(!key.has(cpl[i])){
            key.set(cpl[i],1)
        }else{
            key.set(cpl[i], key.get(cpl[i])+1)
        }
    }
    
    for(let i = 0; i < pp.length; i++){
        if(!key.has(pp[i])){
            return pp[i]
        }else{
            let count = key.get(pp[i])
            if(count == 0){
                return pp[i]
            }else{
                key.set(pp[i], count -1)
            }
        }
    }
}

