import Foundation

func solution(_ s:String) -> [Int] {

    let arr = Array(s)
    var answer: [Int] = [-1]
    
    for i in 1..<arr.count {
        let temp = Array(arr[..<i].reversed())
        
        guard temp.contains(arr[i]) else { 
            answer.append(-1) 
            continue 
        }
        
        for j in 0..<temp.count {
            if temp[j] == arr[i] {
                answer.append(j+1)
                break
            }
        }
    }
    
    return answer
}