import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var dict = [String:Int]()
    var answer = [Int]()
    var score = 0
    for i in 0..<name.count {
        dict[name[i]] = yearning[i]
    }
    for i in photo {
        score = 0
        for j in  i {
            if let person = dict[j] {
                score += person
            }
        }
        answer.append(score)
    }
    return answer
}

// 사진 별 추억 점수
// 인물의 그리움 점수 모두 합산 == 추억 점수
// 사진들 추억 점수를 오름차순으로 리턴
// 이름 : 점수 딕셔너리 저장 -> for문 돌면서 딕셔너리 검색 및 점수 합산