import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var answer = [Int]()
    let sameCnt = Set(lottos).intersection(Set(win_nums)).count
    let winCnt = sameCnt + lottos.filter { $0 == 0 }.count
    
    for num in [winCnt, sameCnt] {
        switch num {
            case 6:
            answer.append(1)
            case 5:
            answer.append(2)
            case 4:
            answer.append(3)
            case 3:
            answer.append(4)
            case 2:
            answer.append(5)
            case 1, 0:
            answer.append(6)
            default:
            break
        }
    }
    
    return answer
}