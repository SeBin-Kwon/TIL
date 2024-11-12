import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    // 내림차순 정렬
    // m개씩 자르기, 남는건 버리기
    // 상자마다 min * m 가격구해서 더하기
    
    var answer = 0
    var sortedScore = score.sorted(by:>)
    // var price = 0
    var box = [Int]()
    for i in 0..<sortedScore.count {
        box.append(sortedScore[i])
        if box.count == m {
            answer += box.min()! * m
            box = [] 
        }
    }
    
    return answer
}