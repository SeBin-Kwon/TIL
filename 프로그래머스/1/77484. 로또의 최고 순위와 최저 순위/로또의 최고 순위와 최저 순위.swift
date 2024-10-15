import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    let sameCnt = Set(lottos).intersection(Set(win_nums)).count
    let winCnt = sameCnt + lottos.filter { $0 == 0 }.count
    
    return [min(7-winCnt,6), min(7-sameCnt,6)]
}