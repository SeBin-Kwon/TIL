import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var (card1, card2) = (cards1, cards2)
    
    for g in goal {
        if let first = card1.first {
            if g == first {
                card1.removeFirst()
                continue
            }
        }
        if let first = card2.first {
            if g == first {
               card2.removeFirst()
                continue
            }
        }
        return "No"
    }
    return "Yes"
}