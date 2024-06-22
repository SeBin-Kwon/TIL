import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    var answer = 0
    var visited = [Bool](repeating: false, count: dungeons.count)
    
    func dfs(_ fatigue: Int, _ count: Int = 0) {
        if answer < count {
            answer = count
        }
        for i in 0..<dungeons.count {
            if !visited[i] && dungeons[i][0] <= fatigue {
                visited[i] = true
                dfs(fatigue - dungeons[i][1], count + 1)
                visited[i] = false
            }   
        }
    }
    
    dfs(k)
    
    return answer
}