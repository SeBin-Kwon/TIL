import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var dic = [String: [(Int, Int)]]()
    var rank = [(Int, Int)]()
    var answer = [Int]()
    var visited = [String: Int]()
    
    for (i, n) in plays.enumerated() {
        rank.append((i,n))
    }
    rank.sort { return $0.1 > $1.1 }
    
    for i in rank {
        dic[genres[i.0], default: []].append(i)
        visited[genres[i.0], default: 0] += i.1
    }
    
    var sortedVisit = visited.sorted { $0.value > $1.value }
    
    for (g, _) in sortedVisit {
        var cnt = 0
        if visited[g]! == 0 {
            continue
        }
        for d in dic[g]! {
            answer.append(d.0)
            cnt += 1
            visited[genres[d.0]]! = 0
            if cnt == 2 {
                break
            }
        }   
    }
    
    return answer
}