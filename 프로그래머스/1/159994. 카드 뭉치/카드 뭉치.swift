import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var (card1, card2) = (cards1, cards2)
    var answer = [String]()
    
    for i in 0..<goal.count {
        if let first = card1.first {
            if goal[i] == first {
                answer.append(card1.removeFirst())
                continue
            }
        }
        if let first = card2.first {
            if goal[i] == first {
               answer.append(card2.removeFirst())
            }
        }
    }
    
    if answer == goal {
        return "Yes"
    } else {
        return "No"
    }
}