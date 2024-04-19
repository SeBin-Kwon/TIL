import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    var answer = 0
    
    func dfs(_ i:Int, _ total:Int, _ answer:inout Int) {
        if i == numbers.count {
            if total == target {
                answer += 1
            }
            return
        }
        dfs(i+1,total+numbers[i],&answer)
        dfs(i+1,total-numbers[i],&answer)
        return
    }
    
    dfs(0,0,&answer)
    return answer
}